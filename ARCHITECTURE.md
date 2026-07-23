# Architecture — Benchora

> **Canonical root file** for phenotype auditors (`raw.docs.files.ARCHITECTURE`).
> Spec: `BENCH-002`. Detailed layout: [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md).
> API surface: [`docs/API_REFERENCE.md`](./docs/API_REFERENCE.md).

## Purpose

Benchora is a Rust benchmarking + xDD toolkit. Library crate: `phenotype_xdd_lib`
(`src/lib.rs`). CLI binary: `benchora` (`src/bin/benchora.rs`).

## Layers (summary)

```text
CLI (bin/benchora) → src/cli/* (run/report/baseline/compare/list/mutate)
                   → SQLite baselines (BENCHORA_DB / --db)
                   → domain / mutation / property / contract / spec
benches/           → Criterion harnesses
```

## Config (no org secrets)

Full table + precedence: [`SPEC.md`](./SPEC.md) / [`SSOT.md`](./SSOT.md) (`BENCH-003`).

| Knob | Default | Role |
|------|---------|------|
| `BENCHORA_DB` / `--db` | `benchora.db` | SQLite baselines + report metadata |
| `BENCHORA_REGRESSION_THRESHOLD_PCT` / `--regression-threshold-pct` | `5.0` | `compare` fail gate |

## Quality gates

`cargo fmt` / `clippy -D warnings` / `test` / `build --release` / `deny`, plus soft
`docs-canonical` and FR `trace-gate` jobs. See [`SSOT.md`](./SSOT.md).
