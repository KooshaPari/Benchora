#!/usr/bin/env python3
"""Executable finite-state coordination experiment, NOT an LLM leaderboard.

Six deterministic dispatch policies share one task generator, worker calculation,
operation budget and external end-state evaluator. Seeded scheduling simulates
asynchrony. The actual Python workers mutate in-memory environments; no model,
network, Git repository or user filesystem is used. Logical ticks are NOT seconds.
"""
from __future__ import annotations
from dataclasses import dataclass, field
import argparse, collections, hashlib, json, random
from pathlib import Path

TOPOLOGIES = ('single', 'independent_best_of', 'blackboard', 'delegation', 'action_vote', 'manager')
FAULTS = ('none', 'stale_observation', 'duplicate_delivery', 'worker_drop', 'false_completion', 'evaluator_tamper')
TASKS = ('independent', 'shared_counter', 'dependency_chain')
CONTROLS = ('unchecked', 'versioned_idempotent', 'versioned_recovery')


def sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


@dataclass
class Env:
    values: dict
    versions: dict
    receipts: set = field(default_factory=set)
    attempted_tamper: int = 0


def task(seed, kind, n=12):
    rng = random.Random(seed)
    initial = {str(i): rng.randrange(1, 10) for i in range(n)} if kind == 'independent' else {'total': rng.randrange(1, 10)}
    jobs = []
    for i in range(n):
        jobs.append({'id': str(i), 'key': str(i) if kind == 'independent' else 'total',
                     'delta': rng.randrange(1, 8), 'depends': [str(i-1)] if kind == 'dependency_chain' and i else []})
    expected = initial.copy()
    for j in jobs:
        expected[j['key']] += j['delta']
    return {'kind': kind, 'initial': initial, 'jobs': jobs, 'expected': expected}


def evaluate(env, spec):
    # This evaluator never trusts acknowledgements and is not candidate-writable.
    return env.values == spec['expected'] and env.receipts == {j['id'] for j in spec['jobs']}


def apply(env, action, policy):
    if action['kind'] == 'tamper':
        env.attempted_tamper += 1
        return 'TAMPER_REJECTED'
    if action['kind'] == 'false':
        return 'UNVERIFIED' if policy != 'unchecked' else 'ACK_ONLY'
    key, jid = action['key'], action['job']
    if policy != 'unchecked':
        if jid in env.receipts:
            return 'ALREADY_COMMITTED'
        if not set(action['depends']) <= env.receipts:
            return 'DEPENDENCY_REJECTED'
        if env.versions[key] != action['version']:
            return 'STALE_REJECTED'
    env.values[key] = action['value']
    env.versions[key] += 1
    env.receipts.add(jid)
    return 'COMMITTED'


def run_one(spec, topology, control, fault, seed, budget=128, width=4, trace=False):
    if topology not in TOPOLOGIES or control not in CONTROLS or fault not in FAULTS:
        raise ValueError('Invalid experiment treatment')
    if budget < 1 or width < 1:
        raise ValueError('Nonpositive budget or width')
    # Independent copies receive a SPLIT total budget, not four full budgets.
    if topology == 'independent_best_of':
        copies = min(width, budget)
        base, remainder = divmod(budget, copies)
        affected_copy = seed % copies
        trials = [run_one(spec, 'single', control, fault if i == affected_copy else 'none', seed * 31 + i,
                          base + (i < remainder), 1, trace) for i in range(copies)]
        winner = min(range(copies), key=lambda i: (not trials[i]['success'], trials[i]['operations'], i))
        chosen = dict(trials[winner])
        chosen.update(topology=topology, control=control, fault=fault, seed=seed, width=copies,
                      budget=budget, winner=winner, fault_injected=any(t['fault_injected'] for t in trials),
                      affected_copy=affected_copy if fault != 'none' else None,
                      operations=sum(t['operations'] for t in trials),
                      logical_ticks=max(t['logical_ticks'] for t in trials),
                      messages=sum(t['messages'] for t in trials) + copies,
                      evaluator_calls=copies,
                      duplicate_attempts=sum(t['duplicate_attempts'] for t in trials),
                      rejected=sum(t['rejected'] for t in trials),
                      total_attempted_tamper=sum(t['total_attempted_tamper'] for t in trials),
                      recovery_events=sum(t['recovery_events'] for t in trials),
                      copies=[{k:v for k,v in t.items() if k!='trace'} for t in trials])
        return chosen
    active_width = 1 if topology == 'single' else width
    env = Env(dict(spec['initial']), {k:0 for k in spec['initial']})
    jobs = spec['jobs']; byid = {j['id']:j for j in jobs}
    rng = random.Random(seed)
    pending, ack, active = {}, set(), set(range(active_width))
    history = {k:[(0,v)] for k,v in spec['initial'].items()}
    attempts = collections.Counter(); counts = collections.Counter()
    events = []; used = 0; tick = 0; injected = False; messages = 0
    restart_due = None; recovery_events = 0
    def log(event):
        events.append({'tick': tick, **event})
    while tick < budget * 4 and used < budget:
        tick += 1
        if restart_due is not None and tick >= restart_due:
            active.add(0); restart_due = None; recovery_events += 1
            log({'worker': 0, 'recovery': 'simulated_restart_state_retained'})
        # Commit in reproducible randomized completion order, retaining stale snapshots.
        ready = [w for w,a in pending.items() if a['due'] <= tick]
        rng.shuffle(ready)
        for w in ready:
            a = pending.pop(w); j=byid[a['job']]
            status = apply(env, a, control); counts[status] += 1
            log({'worker':w,'action':a,'result':status})
            if status in {'COMMITTED','ALREADY_COMMITTED','ACK_ONLY'}:
                ack.add(j['id'])
            if status == 'COMMITTED':
                history[j['key']].append((env.versions[j['key']],env.values[j['key']]))
            if a.get('duplicate'):
                # Delivery is an additional mutation opportunity, but not a model proposal.
                duplicate_status=apply(env,a,control); counts[duplicate_status]+=1
                log({'worker':w,'duplicate_delivery':True,'action':a,'result':duplicate_status})
            if topology in {'manager','delegation','action_vote'}:
                messages += 1
        if len(ack) == len(jobs) and not pending:
            break
        busy_jobs = {a['job'] for a in pending.values()}
        idle = sorted(active - pending.keys())
        if not idle and not pending and restart_due is None:
            break
        for w in idle:
            if used >= budget:
                break
            candidates = [j for j in jobs if j['id'] not in ack and set(j['depends']) <= ack]
            if topology in {'manager','action_vote'}:
                candidates = [j for j in candidates if j['id'] not in busy_jobs]
            if topology == 'delegation':
                candidates = [j for j in candidates if int(j['id']) % active_width == w or
                              (control == 'versioned_recovery' and int(j['id']) % active_width not in active)]
            if not candidates:
                continue
            j = candidates[0]
            # All strategies use the same action calculation. Blackboard workers
            # choose from the same acknowledged state without exclusive claims.
            version,value=env.versions[j['key']], env.values[j['key']]
            mode='write'; duplicate=False
            if not injected and tick >= 2 and fault != 'none':
                injected = True
                if fault == 'worker_drop':
                    active.remove(w); log({'worker':w,'fault':'worker_drop'})
                    if control == 'versioned_recovery':
                        if not active:
                            restart_due = tick + 3
                        else:
                            recovery_events += 1
                            log({'recovery': 'unavailable_shard_claims_released', 'worker': w})
                    continue
                if fault == 'stale_observation':
                    version,value=history[j['key']][0]
                elif fault == 'duplicate_delivery':
                    duplicate=True
                elif fault == 'false_completion':
                    mode='false'
                elif fault == 'evaluator_tamper':
                    mode='tamper'
            price = len(active) if topology == 'action_vote' else 1
            if used + price > budget:
                continue
            used += price; attempts[j['id']] += 1
            if topology in {'manager','delegation'}: messages += 1
            if topology == 'action_vote': messages += len(active)
            a={'job':j['id'],'key':j['key'],'version':version,'value':value+j['delta'],
               'depends':j['depends'],'kind':mode,'due':tick+rng.randint(1,3), 'duplicate':duplicate}
            pending[w]=a;busy_jobs.add(j['id'])
            if topology == 'action_vote': break
        if not pending and restart_due is None and all(not [j for j in jobs if j['id'] not in ack and set(j['depends'])<=ack and
                        (topology != 'delegation' or int(j['id']) % active_width == w or
                         (control == 'versioned_recovery' and int(j['id']) % active_width not in active))] for w in active):
            break
    # Drain in-flight work already charged to the budget. No uncharged new action.
    for w,a in sorted(pending.items(),key=lambda kv:kv[1]['due']):
        tick=max(tick,a['due']);status=apply(env,a,control);counts[status]+=1
        log({'worker':w,'action':a,'result':status,'drain':True})
        if status in {'COMMITTED','ALREADY_COMMITTED','ACK_ONLY'}:ack.add(a['job'])
        if a.get('duplicate'):
            ds=apply(env,a,control);counts[ds]+=1;log({'worker':w,'action':a,'duplicate_delivery':True,'result':ds})
    good=evaluate(env,spec)
    result={'topology':topology,'control':control,'fault':fault,'task':spec['kind'],'seed':seed,
            'budget':budget,'width':active_width,'operations':used,'messages':messages,
            'logical_ticks':tick,'evaluator_calls':1,'success':good,
            'claimed_complete':len(ack)==len(jobs),'false_success':len(ack)==len(jobs) and not good,
            'duplicate_attempts':sum(max(0,v-1) for v in attempts.values()),
            'rejected':sum(v for k,v in counts.items() if k.endswith('REJECTED') or k=='UNVERIFIED'),
            'total_attempted_tamper':env.attempted_tamper,
            'fault_injected':injected,'recovery_events':recovery_events,'final_values':env.values,'received_jobs':sorted(env.receipts),
            'expected_values':spec['expected'],'task_sha256':sha(spec),'trace_sha256':sha(events)}
    if trace:result['trace']=events
    return result


def experiment(seeds=20,budget=128):
    rows=[]
    for seed in range(seeds):
        for kind in TASKS:
            spec=task(seed,kind)
            for topology in TOPOLOGIES:
                for control in CONTROLS:
                    for fault in FAULTS:
                        rows.append(run_one(spec,topology,control,fault,seed,budget))
    groups=collections.defaultdict(list)
    for row in rows: groups[(row['topology'],row['control'],row['task'])].append(row)
    aggregate=[]
    for (top,ctl,kind), group in sorted(groups.items()):
        aggregate.append({'topology':top,'control':ctl,'task':kind,'runs':len(group),
                          'successes':sum(r['success'] for r in group),
                          'false_successes':sum(r['false_success'] for r in group),
                          'mean_operations':sum(r['operations'] for r in group)/len(group),
                          'mean_logical_ticks':sum(r['logical_ticks'] for r in group)/len(group)})
    return {'experiment_id':'EG-W6-COORDINATION-REFERENCE','kind':'finite_state_simulation',
            'not_llm_benchmark':True,'seeds':seeds,'runs':len(rows),'budget_per_run':budget,
            'limits':['Workers use a deterministic arithmetic policy; no language model or provider.',
                      'Logical ticks are not measured deployment latency.',
                      'Dispatch policies and fault mechanisms are this simulator\'s definitions, not universal topologies.',
                      'Equal budgets are ceilings; report actual operations and selection costs.',
                      'These results test protocol behavior, not intelligence, paper reproduction or production scaling.'],
            'fault_exposure': 'At most one designated proposal/worker fault per outer run; best-of injects into one copy only.',
            'recovery_scope': 'Worker unavailable before dispatch; state retained; no crash durability or real-process recovery tested.',
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'aggregate':aggregate,'results':rows}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--seeds',type=int,default=20)
    p.add_argument('--output',type=Path,required=True);args=p.parse_args()
    if not 1<=args.seeds<=100: raise SystemExit('seeds must be 1..100')
    report=experiment(args.seeds);args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in {'results','aggregate'}},indent=2))
    print(json.dumps(report['aggregate'],indent=2))

if __name__=='__main__':main()
