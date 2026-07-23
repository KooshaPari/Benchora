# Benchora

Phenotype ecosystem component — Rust benchmarking + xDD toolkit
(library `phenotype_xdd_lib`, CLI `benchora`).

## Traceability

| ID | Requirement |
|----|-------------|
| BENCH-001 | Core product contract: Criterion benches, xDD utilities, CLI run/report/baseline/compare |
| BENCH-002 | Governance surface: canonical ARCHITECTURE + SSOT index + scorecard WORK_DAG |
| BENCH-003 | Config surface: documented env/clap knobs + soft contract test for `BENCHORA_DB` defaults |

```text
/// @trace BENCH-001
/// @trace BENCH-002
/// @trace BENCH-003
```

## Runtime configuration (env / clap)

Public knobs only — no org secrets. Soft evidence: `tests/config_env_contract_test.rs`.

| Knob | Clap flag | Default | Purpose |
|------|-----------|---------|---------|
| `BENCHORA_DB` | `--db` (global) | `benchora.db` | SQLite path for baselines + report / mutation metadata |
| `BENCHORA_REGRESSION_THRESHOLD_PCT` | `--regression-threshold-pct` | `5.0` | `compare` regression fail gate (percent) |

### Precedence

| Setting | Order (highest wins) |
|---------|----------------------|
| DB path | `--db` → `BENCHORA_DB` → default `benchora.db` |
| Regression threshold | `--regression-threshold-pct` → `BENCHORA_REGRESSION_THRESHOLD_PCT` → value stored in DB → `5.0` |

When adding a knob, update this table, [`SSOT.md`](./SSOT.md), and the contract test in the same PR.

## Sources of truth

See [`SSOT.md`](./SSOT.md) and [`ARCHITECTURE.md`](./ARCHITECTURE.md).
Score lift plan: [`docs/SCORECARD.md`](./docs/SCORECARD.md).
