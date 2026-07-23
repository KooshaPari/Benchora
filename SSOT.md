# SSOT — Benchora

> Single source of truth index for agents, CI soft gates, and phenotype auditors.
> Spec ID: `BENCH-002`.

## Canonical documents

| Concern | Source of truth | Notes |
|---------|-----------------|-------|
| Product contract / traces | [`SPEC.md`](./SPEC.md) | `BENCH-NNN` IDs; `@trace` markers |
| Architecture (auditor root) | [`ARCHITECTURE.md`](./ARCHITECTURE.md) | Canonical path auditors check |
| Architecture (detail) | [`docs/ARCHITECTURE.md`](./docs/ARCHITECTURE.md) | Full crate map + data flow |
| API surface | [`docs/API_REFERENCE.md`](./docs/API_REFERENCE.md) | Public API reference |
| This index | [`SSOT.md`](./SSOT.md) | Doc + config pointers |
| Agent operating notes | [`AGENTS.md`](./AGENTS.md), [`CLAUDE.md`](./CLAUDE.md) | Branch / AgilePlus mandate |
| Contribute / quality loop | [`CONTRIBUTING.md`](./CONTRIBUTING.md) | fmt / clippy / test / bench |
| Security reporting | [`SECURITY.md`](./SECURITY.md) | Vulnerability disclosure |
| Changelog / semver | [`CHANGELOG.md`](./CHANGELOG.md) | Keep a Changelog |
| License | [`LICENSE`](./LICENSE) | MIT |
| Audit baseline grade | [`audit_scorecard.json`](./audit_scorecard.json) | Phenotype registry sweep v2 |
| Score lift plan | [`docs/SCORECARD.md`](./docs/SCORECARD.md) | WORK_DAG for next lifts |
| Intent / boundary | [`docs/intent/Benchora.md`](./docs/intent/Benchora.md), [`docs/boundary/Benchora.md`](./docs/boundary/Benchora.md) | Registry-propagated |
| FR coverage soft gate | [`trace-gate.toml`](./trace-gate.toml) | `min_coverage`, `strict_mode = false` |
| Dependency policy | [`deny.toml`](./deny.toml) | cargo-deny |
| Toolchain pin | [`rust-toolchain.toml`](./rust-toolchain.toml) | Stable channel pin |

## Runtime configuration (no org secrets)

| Knob | Default | Purpose |
|------|---------|---------|
| `BENCHORA_DB` / `--db` | `./benchora.db` | SQLite path for baselines + report metadata |
| Criterion / `cargo bench` | crate `[[bench]]` targets | Statistical benches |
| CI `RUSTFLAGS` | `-D warnings` | Treat warnings as errors in Actions |

Secrets (API tokens, cloud creds) are **out of scope** for local bench/CLI use.
Do not commit `.env` files with credentials; `benchora.db` is local state.

## Traceability scheme

- Prefer **`BENCH-NNN`** in specs, rustdoc, and PR bodies (`CONTRIBUTING.md`).
- CI may also run the reusable phenotype **FR coverage** soft gate
  (`trace-gate.yml`); treat failures as informational unless the workflow is
  later flipped to hard-fail.

## Update rule

When adding a new top-level process doc or env knob, update **this file** in
the same PR so auditors and agents keep a single index.
