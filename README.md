<!-- AI-DD-META:START -->
<!-- This repository is planned, maintained, and managed by AI Agents only. -->
<!-- Slop issues are expected and intentionally present as part of an HITL-less -->
<!-- /minimized AI-DD metaproject of learning, refining, and building brute-force -->
<!-- training for both agents and the human operator. -->
![Downloads](https://img.shields.io/github/downloads/KooshaPari/Benchora/total?style=flat-square&label=downloads&color=blue)
![GitHub release](https://img.shields.io/github/v/release/KooshaPari/Benchora?style=flat-square&label=release)
![License](https://img.shields.io/github/license/KooshaPari/Benchora?style=flat-square)
![AI-Slop](https://img.shields.io/badge/AI--DD-Slop%20Expected-orange?style=flat-square)
![AI-Only-Maintained](https://img.shields.io/badge/Planned%20%26%20Maintained%20by-AI%20Agents%20Only-red?style=flat-square)
![HITL-less](https://img.shields.io/badge/HITL--less%20AI--DD-metaproject-yellow?style=flat-square)

> ⚠️ **AI-Agent-Only Repository**
>
> This repo is **planned, maintained, and managed exclusively by AI Agents**.
> Slop issues, rough edges, and AI artifacts are **expected and intentionally
> present** as part of an **HITL-less / minimized AI-DD** metaproject focused
> on learning, refining, and brute-force training both the agents and the
> human operator. Bug reports and contributions are still welcome, but please
> expect AI-generated code, comments, and documentation throughout.
<!-- AI-DD-META:END -->

## Work State

| Field | Value |
|---|---|
| Status | ACTIVE (repo unarchived) |
| Crate version | `0.2.0` in `Cargo.toml` — **no git tag / GitHub Release yet** |
| crates.io | **Not published** (crate name `benchora` is free; do not use `cargo install benchora`) |
| Install path | from source — see [Install](#install) |
| Scorecard | ~82 / B (`audit_scorecard.json`) |
| Focus | T0 — install/publish honesty + release-attestation hygiene |

Progress: `████████░░` ~80% feature surface (CLI + library + benches) — **not** release/publish complete.

> Honest gap: local `cargo test` / `cargo build` are green; end-user install is
> path/git only until a tagged release and crates.io publish land (T1).

[![CI](https://github.com/KooshaPari/Benchora/actions/workflows/ci.yml/badge.svg)](https://github.com/KooshaPari/Benchora/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

# Benchora

Rust benchmarking and xDD testing toolkit for the Phenotype ecosystem — Criterion
harnesses, a `benchora` CLI, SQLite-backed baselines, mutation-coverage tracking,
and reusable xDD utilities.

## Install

**Not on crates.io yet.** Install from a clone (preferred one-liner):

```bash
cargo install --path . --locked
```

Or from GitHub without cloning first:

```bash
cargo install --git https://github.com/KooshaPari/Benchora --locked
```

Requires a recent Rust stable toolchain (`rustfmt` + `clippy`; see `rust-toolchain.toml`).
MSRV intent: 1.75+.

After install, the `benchora` binary is on your `PATH`.

## Quick Start

```bash
git clone https://github.com/KooshaPari/Benchora
cd Benchora
cargo build --locked
cargo test --locked

# Criterion benches
cargo bench --bench my_benchmark
cargo bench --bench phenotype_xdd_lib_bench

# CLI (from build tree)
cargo run --release --locked --bin benchora -- run --suite my_benchmark --out ./reports
cargo run --release --locked --bin benchora -- baseline --from ./reports/my_benchmark-*.json nightly
cargo run --release --locked --bin benchora -- compare --current ./reports/my_benchmark-*.json nightly
cargo run --release --locked --bin benchora -- list
```

The `--db` flag (or `BENCHORA_DB`) points the CLI at a SQLite file; default `./benchora.db`.

## Key Features

- **Criterion bench harnesses** (`my_benchmark`, `phenotype_xdd_lib_bench`)
- **`benchora` CLI** — `run`, `report`, `baseline`, `compare`, `list`, `mutate`
- **SQLite-backed baseline store** with sha256-pinned integrity hashes
- **Regression detection** — configurable threshold; non-zero exit for CI gates
- **Mutation coverage** — set-based line + branch tracking; `mutation_score` is `Option<f64>`
- **xDD utilities** — property strategies, contract verifier, spec parser/validator
- **Library + binary** — lib is `phenotype_xdd_lib`; CLI is the `benchora` bin

## CLI

| Subcommand | Purpose |
|---|---|
| `benchora run --suite <name> --out <dir>` | Execute a bench suite and write a report |
| `benchora report <report.json>` | Summarize a report to stdout |
| `benchora baseline --from <report.json> <name>` | Promote a report to a named baseline |
| `benchora compare --current <report.json> <baseline>` | Diff a report against a baseline |
| `benchora list [reports\|baselines\|mutations]` | List stored SQLite entries |
| `benchora mutate` | Run mutation testing via `cargo mutants` |

## Publish / release readiness (T0 → T1)

| Item | Today | T1 |
|---|---|---|
| Crate version | `0.2.0` in tree | Keep CHANGELOG ready; cut `v0.2.0` only when releasing |
| crates.io | Not published | `cargo publish` after tag + CHANGELOG section |
| GitHub Release | None | Tag + attach attested artifacts |
| cargo-dist | Not configured | Optional; release workflow builds `benchora` explicitly |

Do **not** treat the GitHub “release” badge as proof of a crates.io package.

## Documentation

- [SPEC.md](./SPEC.md) — framework contract (`@trace BENCH-001`)
- [docs/getting-started.md](./docs/getting-started.md) — local build/test
- [docs/slsa.md](./docs/slsa.md) — release attestation notes
- [CHANGELOG.md](./CHANGELOG.md) — Keep a Changelog

## Contributing

PRs welcome. See [CONTRIBUTING.md](./CONTRIBUTING.md). Verify locally (`cargo test --locked`,
`cargo clippy --all-targets -- -D warnings`) — GitHub Actions billing may soft-fail runners.

## License

MIT — see [`LICENSE`](./LICENSE).
