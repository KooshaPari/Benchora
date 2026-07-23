# SCORECARD / WORK_DAG — Benchora

Baseline: [`audit_scorecard.json`](../audit_scorecard.json) — **overall 82, grade B**
(generated 2026-06-24, auditor v2 Rust-corrected).

No prior `WORK_DAG` / governance SCORECARD lived in-repo; this file is the
working lift plan. Prefer **docs + soft CI evidence** before large refactors.
Skip tasks that require org secrets (cloud API keys, private registry tokens).

## Current grade breakdown (lowest first)

| Pillar | Score | Gap theme | Secrets? |
|--------|------:|-----------|----------|
| L8 Compliance | 30 | SSOT missing; weak process evidence | No |
| L17 I18n/A11y | 45 | N/A-ish for Rust CLI; low ROI | No |
| L19 Memory | 45 | Python-biased auditor; Rust RAII already | No |
| L15 API Surface | 50 | No OpenAPI; CLI/rustdoc under-indexed | No |
| L20 Config | 50 | Env/config surface under-documented | No |
| L24 Migration | 50 | Deprecation / migrate notes thin | No |
| L26 Event Driven | 55 | Not a queue product; optional adapter docs | No |
| L28 Cost Efficiency | 55 | Batching/pagination N/A for bench CLI | No |
| L4 Observability | 65 | Canonical docs were 6/8 | No |
| L14 Data Layer | 70 | SQLite present; migration story soft | No |
| L16 Frontend | 70 | Docs site only | No |
| L29 Monitoring | 70 | Health/metrics soft evidence | No |
| L27 Infrastructure | 75 | No Dockerfile / compose | No |
| L13 Logging | 75 | Structured logging sparse | No |
| L3 Agent Loop | 80 | CLI exists now; keep help stable | No |

High pillars (skip for lift): L5/L9/L25 = 100; L1/L10 = 95; L2/L11/L12/L23/L30 ≥ 90.

## READY gaps — highest % upside (no org secrets)

1. **L8 Compliance (+ SSOT/ARCHITECTURE)** — largest absolute gap; flips auditor
   `SSOT: false` and completes canonical doc set → also lifts **L4**.
2. **L20 Config** — document + soft-check env knobs (`BENCHORA_DB`, clap globals).
3. **L27 Infrastructure** — add a minimal multi-stage `Dockerfile` for
   `cargo build --release` / CLI smoke (no registry secrets).
4. **L29 Monitoring** — soft evidence: document CLI exit codes + optional
   `--health` / report JSON schema note; no Prometheus org stack required.
5. **L15 API Surface** — expand rustdoc + `benchora --help` contract test
   (assert subcommands); skip full OpenAPI unless HTTP lands.

Deferred / low ROI without product change: L17, L19 (auditor mismatch), L26/L28
(event/cost pillars not core to Criterion CLI).

## WORK_DAG — next 4 tasks

```text
[DONE/PR] T1 docs+CI  ARCHITECTURE.md + SSOT.md + docs-canonical soft gate
              │
              ▼
[READY]   T2 config   Expand SPEC/SSOT config section + clap env snapshot test
              │
              ▼
[READY]   T3 infra    Minimal Dockerfile + `make docker-smoke` (no push secrets)
              │
              ▼
[READY]   T4 monitor  Exit-code / report-schema soft evidence in docs + unit assert
```

| ID | Task | Pillars | Est. lift | Blockers |
|----|------|---------|-----------|----------|
| T1 | Canonical SSOT + ARCHITECTURE + soft docs CI | L8, L4 | High | None (this PR) |
| T2 | Config surface tests + SPEC env table sync | L20, L8 | Med | After T1 |
| T3 | Dockerfile + local smoke target | L27, L30 | Med | None |
| T4 | Monitoring soft evidence (exit codes / schema) | L29, L4 | Med | None |

## Lane claim rule

Claim **one** READY task per PR on `feat/benchora-audit-lift-N`. Do not merge
from scout agents unless explicitly asked. Update this DAG when a lane lands.
