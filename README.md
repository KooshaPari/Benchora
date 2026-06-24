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
> **Work state:** ACTIVE · **Progress:** `████████░░ 80%`
> Rust benchmarking + xDD testing framework (**Benchora**); CLI, baseline store, mutation coverage, multi-suite benches · updated 2026-06-23

# Benchora

## State

Progress: `[████████░░] 80%` — Rust benchmarking + xDD testing framework, **CLI ready**, mutation coverage math audited.

_Updated 2026-06-23 — DAG-002 mutation-math fix landed; coverage is now set-based; mutation score returns `None` for empty trackers._

[![CI](https://github.com/KooshaPari/Benchora/actions/workflows/ci.yml/badge.svg)](https://github.com/KooshaPari/Benchora/actions)
[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Benchmarking and performance testing framework** — Rust-based benchmarking suite for the Phenotype ecosystem.

## Project Overview

Benchora provides performance benchmarking, load testing, and metrics collection for Phenotype projects.

## Key Features

- **Criterion-based bench harness** (`my_benchmark`, `phenotype_xdd_lib_bench`)
- **`benchora` CLI** with five subcommands: `run`, `report`, `baseline`, `compare`, `list`
- **SQLite-backed baseline store** with sha256-pinned integrity hashes
- **Regression detection** — 5 % threshold surfaces as non-zero exit for CI gates
- **Mutation testing coverage** with set-based line + branch tracking (no double-counting)
- **xDD utilities** — property strategies (`valid_uuid`, `valid_email`, `bounded_int`, …), contract verifier, spec parser/validator
- **Reusable as a library** — `phenotype_xdd_lib` exposes the modules; CLI is a thin wrapper

## Mutation-coverage guarantees

`MutationTracker::coverage` and `MutationTracker::branch_coverage` divide **distinct** lines/branches hit by the file's effective LOC. Repeated execution of the same line cannot inflate coverage past 100 %. `MutationTracker::mutation_score` returns `Option<f64>` — `None` for empty trackers, `Some(ratio)` otherwise — so callers cannot accidentally report a perfect score on a pristine run.

## Quick Start

```bash
# Setup
cd Benchora
cargo build

# Run benchmarks (criterion standard harness)
cargo bench --bench my_benchmark
cargo bench --bench phenotype_xdd_lib_bench

# Run the full test suite (covers DAG-002 mutation-math regression)
cargo test

# Use the benchora CLI
cargo run --release -- run     --suite my_benchmark --out ./reports
cargo run --release -- baseline --from ./reports/my_benchmark-*.json nightly
cargo run --release -- compare  --current ./reports/my_benchmark-*.json nightly
cargo run --release -- list
```

The `--db` flag (or `BENCHORA_DB` env var) points the CLI at a SQLite file for baselines + report metadata; default `./benchora.db`.

## Documentation

- [SPEC.md](./SPEC.md) — Project specification

## Traceability

`/// @trace BENCH-001`

## Description

Rust benchmarking framework (**Benchora**) for the Phenotype ecosystem — criterion-based bench harness, SQLite-backed report + baseline store, sha256-pinned regression tracking, and the `benchora` CLI (`run | report | baseline | compare | list`).

## CLI

The `benchora` binary is the entry point. Five subcommands:

- `benchora run --suite <name> --out <report.json>` — execute a bench suite and write a report
- `benchora report <report.json>` — summarize a report to stdout
- `benchora baseline --from <report.json> <name>` — promote a report to a named baseline (sha256-pinned)
- `benchora compare --current <report.json> <baseline>` — diff a report against a baseline
- `benchora list [reports|baselines]` — list stored entries in the SQLite state DB

The state DB is configured via `--db <path>` (default `./benchora.db`).

## Install

`cargo build --release` (adds the `benchora` binary to `target/release/`) or `cargo install --path .` for a stable install. Requires Rust 1.75+ (see `rust-toolchain.toml`).

## Usage

Run benches: `cargo bench`. Run unit tests: `cargo test`. See `SPEC.md` for the framework contract and `@trace BENCH-001` markers for requirement traceability.

## Contributing

PRs welcome. See `CONTRIBUTING.md`. New bench harnesses follow the existing `criterion` group layout; new metrics exporters go under a dedicated adapter crate.

## License

MIT — see [`LICENSE`](./LICENSE).
