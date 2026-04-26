# AGENTS.md — Benchora

Rust benchmarking and performance-testing framework for the Phenotype ecosystem — criterion-based benchmarks, regression tracking, metrics.

## Repository identity

- Language: Rust (see `rust-toolchain.toml`).
- Entry point: `Cargo.toml` (root).
- Source: `src/`. Benchmarks: `benches/`. Tests: `tests/`.
- Spec: `SPEC.md`.

## Build & test (verified from README)

```bash
cargo build
cargo test
cargo bench
```

Pre-commit hooks: `.pre-commit-config.yaml` is committed; run `pre-commit install` when contributing.

## Governance

- Spec: `SPEC.md`.
- Code of Conduct: `CODE_OF_CONDUCT.md`.
- License: see `LICENSE`.
- Traceability tag: `/// @trace BENCH-001` (per README).

## Commit & branch convention

- Conventional Commits.
- Branch: `<type>/<topic>`.

## Agent guardrails

- Benchmark results are non-deterministic — never assert exact numbers in tests; use criterion's regression detection.
- Keep `benches/` runnable on stable Rust; do not gate benchmarks on nightly-only features.
