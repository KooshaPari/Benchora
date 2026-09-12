# Agent Coordination Topology Pilot

**Research origin:** Emergent Garden nested-corpus campaign `eg-nested-corpus-2026-09`  
**Canonical evidence:** `KooshaPari/ResearchLedger#81`  
**State:** proposed experiment; not implemented or reproduced  
**Owner:** Benchora experiment contract and result comparison only

## Decision sought

Determine which coordination topology produces the best verified task outcomes under a constant task corpus, model/tool budget, starting state, and evaluator.

The pilot tests a concrete correction to the assumption that adding agents or communication monotonically improves a system. The source corpus contains both generative successes and negative evidence: shared-artifact interference, stale state, expensive duplicated work, unsafe generated actions, and controlled Mindcraft work that treats action-level collaboration as an intervention rather than a default.

## Source boundary

Use only claims and sources frozen in the Wave 1 ResearchLedger source manifest. The current evidence includes:

- Mindcraft's task and safety contracts;
- the MineCollab paper pointer on action-level collaboration;
- the `agent_prompts` shared-artifact experiments;
- `fractalsearch` recursive code modification against an external objective;
- `AgentsOfEmpires` tournament, heartbeat, result, recording, and incumbent-retention loop.

This document does not claim those experiments were reproduced by Benchora.

## Hypotheses

### H1 — Structured collaboration beats unstructured shared state

Action-level or manager-mediated collaboration will reduce conflicting writes and stale-state actions relative to an unconstrained shared blackboard.

### H2 — Best-of independent attempts remains competitive

For decomposable coding tasks, independent attempts plus deterministic selection may match or beat interactive multi-agent coordination at lower coupling cost.

### H3 — More agents have a non-monotonic return

Past a task-dependent width, additional agents increase duplicated work, contention, cost, and evaluator burden faster than success probability.

### H4 — Environment/tool reliability dominates some model differences

Injected stale observations or tool failures will erase or reverse topology advantages unless the system has explicit recovery and evidence semantics.

### Null and contrary hypotheses

- topology has no material effect after controlling for token and wall-clock budgets;
- observed gains come from more total compute rather than coordination;
- a single strong agent dominates every multi-agent condition;
- shared communication helps only on tasks with true cross-agent dependency;
- manager mediation adds latency without improving correctness.

## Experimental conditions

1. **Single agent** — one agent owns the task end to end.
2. **Best-of independent** — multiple isolated attempts; deterministic evaluator selects the result.
3. **Shared append-only blackboard** — agents read a common log and append findings; no direct messaging.
4. **Direct delegation** — agents may assign bounded subtasks and return typed results.
5. **Action-level collaboration** — agents propose or select the next action against shared state.
6. **Manager/worker** — one coordinator owns plan, authority, and integration; workers receive bounded work packages.

Do not add a seventh topology after observing results without recording a protocol amendment.

## Task corpus

Start with a small coding/research corpus containing at least:

- one independent bug-fix task;
- one task with two separable modules;
- one task requiring a shared schema or interface decision;
- one repository-research task with conflicting evidence;
- one task with an intentionally unreliable tool or stale observation;
- one task where a correct answer is to make no change.

Every task needs hidden acceptance checks and a declared maximum authority scope.

## Controls

Hold constant where technically possible:

- model/provider and version;
- total token or monetary budget;
- maximum wall time;
- tool set and filesystem permissions;
- repository/environment starting snapshot;
- context supplied at start;
- retry, timeout, and cancellation policy;
- evaluator and hidden tests;
- checkpoint interval;
- operator-intervention policy.

Where a topology inherently changes total calls or elapsed time, report the difference instead of normalizing it away.

## Measurements

### Outcome

- hidden-test/task correctness;
- mandatory-requirement coverage;
- invalid or unnecessary changes;
- terminal task state;
- success after injected failure.

### Coordination

- duplicate work ratio;
- conflicting-write count;
- stale-state actions;
- unresolved dependency count;
- messages/blackboard entries per accepted contribution;
- integration rework;
- manager bottleneck time.

### Cost and latency

- model calls and tokens;
- monetary cost;
- wall time;
- time to first valid artifact;
- evaluator calls;
- operator interventions.

### Safety and evidence

- actions outside declared authority;
- generated-code execution attempts;
- rollback success;
- checkpoint recoverability;
- trace completeness;
- evidence-to-decision linkage;
- secrets or private-data exposure.

## Failure injection

Run at least these negative controls:

1. deliver one stale observation;
2. return one plausible but incorrect tool result;
3. make one worker unavailable after accepting work;
4. create two tasks that contend for the same file;
5. remove communication while retaining the same agent count;
6. retain communication but reduce width to one;
7. insert one evaluator-irrelevant attractive artifact;
8. inject one instruction that requests action outside authority.

The system must record whether the fault was detected, contained, recovered, or silently propagated.

## Evidence bundle

Each run must preserve:

- immutable task and starting-state IDs;
- topology and agent-role configuration;
- model/provider versions and budgets;
- tool and permission manifest;
- messages, blackboard records, proposed actions, accepted actions, and rejections;
- checkpoints and rollback operations;
- generated artifacts and diffs;
- evaluator inputs and outputs;
- hidden-test result envelope;
- injected faults;
- operator interventions;
- terminal status and resource accounting.

Store bulky or sensitive run data outside Git. Commit only schemas, fixtures safe for publication, aggregate results, hashes, and source pointers.

## Analysis

For each topology report distributions, not one showcase run. Separate:

- success attributable to topology;
- success attributable to extra compute;
- task-topology interaction;
- model-topology interaction;
- tool/environment failures;
- evaluator uncertainty;
- unrecovered protocol violations.

A topology is not preferred merely because it wins the mean. Report tails, catastrophic outcomes, recovery, cost, and evidence completeness.

## Acceptance rule

A topology may be recommended only when:

1. mandatory correctness and safety floors do not regress;
2. the advantage reproduces across more than one task class;
3. cost and latency trade-offs are quantified;
4. negative-control behavior is understood;
5. evidence is bound to immutable configuration and artifacts;
6. a simpler single-agent or best-of-independent alternative does not dominate it.

Valid outcomes include:

- topology-specific advantage;
- single-agent dominance;
- best-of-independent dominance;
- manager bottleneck;
- communication harm;
- task-dependent mixed result;
- no material difference;
- inconclusive because the evaluator or environment is unreliable.

## Non-goals

- implementing an agent runtime inside Benchora;
- selecting a universal fleet coordination topology;
- reproducing Minecraft or Age of Empires environments;
- proving the Emergent Garden corpus has one philosophy;
- changing Agentora, thegent, Helios, or Tracera contracts before results exist;
- treating creator demonstrations as Benchora benchmark results.

## Proposed output paths

```text
experiments/agent-coordination-topology/
  protocol.yaml
  tasks/
  fixtures/
  schemas/
  runners/
  results/<run-id>/
  aggregate.json
  REPORT.md
```

Actual implementation requires a separate approved work package after this document and its source manifest are reviewed.
