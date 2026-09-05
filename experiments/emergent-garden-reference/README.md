# Emergent Garden finite-state reference experiment

Work tracking: [AgilePlus #1073](https://github.com/KooshaPari/AgilePlus/issues/1073). Research origin: ResearchLedger #81, Wave 6. This is separate from the unexecuted language-agent protocol in Benchora #106.

## Scope

An executable deterministic arithmetic-worker simulation tests dispatch, state consistency and recovery. It is not an LLM leaderboard, deployment latency measurement, real-process crash test, or reproduction of a creator demonstration. No provider, network, game or hardware dependency is used by the runner.

Six dispatch policies, three 12-job task classes, six fault states, three control states and twenty seeds yield 6,480 outer trials. Each outer trial has a 128-calculation ceiling. Independent best-of splits that ceiling across copies and records extra evaluator calls. Only one designated fault is injected per outer run, including independent best-of. An earlier development version's unfair per-copy fault exposure was corrected before the reported run.

## Local execution result

| Control | Trials | Correct end states | False completion claims |
| --- | ---: | ---: | ---: |
| unchecked | 2160 | 1178 | 862 |
| versioned_idempotent | 2160 | 2040 | 0 |
| versioned_recovery | 2160 | 2160 | 0 |

False completion is a subset of failures. No operation ceiling was exceeded. The versioned/idempotent case prevents false completion but leaves 120 failed trials when a sole worker or fixed shard owner is lost. Explicit recovery reassigns abandoned work or restarts the lone logical worker while retaining environment state. This is not durable recovery after a real crash.

The runner source SHA-256 is `c4f59e2a16a93ddfb001f906f71c49b941bc64f2de1a9f2874f4af8e8034de99`. Local full-result JSON SHA-256 is `e274eb378a1328cf6d3add0ba4bb77b2d2b44d01eb5c36cef3afca8d77204a61`. Hosted workflow artifacts provide a separate rerun receipt; do not assume success merely because a workflow was launched.

## Reproduce

```bash
python3 -m unittest discover -s experiments/emergent-garden-reference -p 'test*.py' -v
python3 experiments/emergent-garden-reference/run_coordination_reference.py --seeds 20 --output /tmp/eg-reference.json
```

The workflow verifies unique treatment coverage and operation ceilings, then retains all trial records and source/result hashes. Its tests fail closed, including through the log pipeline.

## Interpretation and limits

A manager that prevents overlapping ownership of a job can still dispatch different jobs that modify the same key from stale snapshots. Task ownership and object-version checks solve different problems. Safety and progress after loss are also different properties.

Workers calculate correct arithmetic except for the injected protocol faults. Action voting is a deterministic emulation, not a noisy independent model ensemble. Tamper rejection follows from a deliberately narrow action interface, not resistance to arbitrary candidate code. Fault injection happens before dispatch with retained state; no network partitions, crash-after-commit ambiguity, storage loss or real thread races are tested. Logical ticks are not seconds. Equal ceilings do not mean equal actual compute; operations, messages and evaluator calls are reported.

These fixture results do not establish a universally best topology or production reliability. Benchora #106 remains a separately gated live model experiment. No production runtime, model/provider calls, releases, default-branch changes or merges are included.
