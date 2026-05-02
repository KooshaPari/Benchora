# Benchora — Workspace Operating Notes

## Project Overview

Benchora is a Rust benchmarking and performance-testing framework for the Phenotype ecosystem — criterion-based load testing, regression tracking, and metrics.

- **Stack**: Rust
- **Package**: `gauge` (criterion-based + proptest + quickcheck)
- **Edition**: 2021

## Build & Test

```bash
cargo build     # Build the library and binaries
cargo test      # Unit tests
cargo bench     # Run criterion benchmarks (needs -- BENCHMARK_NAME)
cargo check      # Type/lint check
```

## Code Quality

- `cargo clippy` — linting
- `cargo deny check` — dependency audit (advisories, licenses, sources)
- `cargo fmt` — formatting
- No new `unsafe` without explicit safety comments
- Max function: 50 lines, max cognitive complexity: 15

## Governance

- Reference: `~/.claude/CLAUDE.md` (global baseline)
- Reference: `AgilePlus/CLAUDE.md` ( Phenotype org governance)
- Cargo-deny CI: `.github/workflows/cargo-deny.yml`
- CLAUDE.md required for all Phenotype org repos
- Fork-aware: if upstream benching patterns exist, consider contributing upstream first
