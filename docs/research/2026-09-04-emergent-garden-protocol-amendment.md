# Proposed Wave 3 amendment to the coordination pilot

Status: protocol amendment for review, not an implemented experiment or measured topology ranking.

Applies to [the existing pilot](emergent-garden-agent-coordination-pilot.md) in draft PR #106. Work tracking: [AgilePlus #1073](https://github.com/KooshaPari/AgilePlus/issues/1073).

Canonical evidence: [ResearchLedger Wave 3](https://github.com/KooshaPari/ResearchLedger/blob/8c271fd6765b01c6a6a6339d7273199a48e06334/docs/corpora/emergent-garden/research/WAVE-3-COMMENTS-AND-SYNTHESIS.md), with [primary-source depth](https://github.com/KooshaPari/ResearchLedger/blob/8c271fd6765b01c6a6a6339d7273199a48e06334/docs/corpora/emergent-garden/research/WAVE-3-PRIMARY-SOURCES.md).

## Source-scope amendment

The original pilot refers to Wave 1 sources. This proposed amendment adds the versioned Wave 3 clarification and primary-method records; it does not retroactively declare the amendment accepted or a run compliant with an unreviewed protocol.

The creator qualifies the optimizer comparison, corrects a normalized-tanh interpretation, distinguishes script search from RL, acknowledges stronger conventional AoE baselines, and records historical differences in tool/vision configuration. The primary methods distinguish observer, actuator, environment, memory and evaluator choices. Those are experimental controls, not a recommendation to add agents.

## Keep six topologies

Retain single agent, best-of-independent, append-only blackboard, direct delegation, action-level collaboration and manager/worker. Do not add a new topology after seeing results without a protocol revision. A conventional deterministic baseline should also be included where the task admits one; it is a comparator, not a new multi-agent topology.

## Five confounder controls

1. **Representation and optimization:** compare equivalent parameterizations with matched initialization and update scales, not merely equal numeric hyperparameters. Record code, prompt, scaffold and model-weight changes separately.
2. **Actuation and observation:** hold tool primitives, permissions, observation radius/freshness, vision availability and simulator speed constant or explicitly factor them. New tools must not masquerade as coordination gain.
3. **Evaluator integrity:** freeze held-out tasks and trusted output parsing. Reject candidate-authored fake tool outcomes, altered tests and evaluator-redefining messages. Novelty and acceptance are separate scores.
4. **Resource accounting:** retain failed, invalid and timed-out attempts in the denominator. Include evaluator calls, retries, context, tokens, wall time and operator work. Archive maintenance is not free.
5. **Versioned source and environment:** pin repository, task, release, model, tool, evaluator and initial-state revisions. A current README must not replace the configuration actually used by an older trial.

## Additional negative controls

An agent claims completion without an observed result; a reflection is reintroduced as a fact; an attractive but evaluator-irrelevant output is proposed; a task change silently widens permissions; a candidate modifies its evaluator; a stale retrieved skill assumes an unavailable tool; a duplicate result is delivered; and a supposed rollback cannot reverse an external side effect.

Record detected, contained, recovered, unknown and silently propagated outcomes separately. A no-change decision can be correct. Unknown outcomes should not be coerced into success.

## Independent numerical checks already executed elsewhere

ResearchLedger performed two bounded checks motivated by the activation correction. The normalized-tanh identity held across 8,001 points with maximum absolute error `2.220446049250313e-16`. In a 33-sample, 200-step scalar gradient-descent toy, matched parameterization/rates produced zero prediction difference; an equal-rate negative control produced `0.136395047283144` final maximum difference.

These results support controlling parameterization. They are not Benchora coordination results, do not establish optimizer superiority, and do not satisfy the live pilot's acceptance gate.

## Reporting and acceptance

Report per-task distributions and resource-normalized trade-offs, not one showcase. Include null, single-agent-dominant, independent-best-of-dominant, communication-harm and inconclusive outcomes. Keep correctness and authority floors explicit. A selected research archive and a promoted production incumbent use different criteria.

Before implementation, review this amendment with the original protocol, define the task corpus, freeze the result schema, and create a bounded implementation work package. No model/provider calls, environment deployment, benchmark implementation, merge or release is performed by this documentation amendment.
