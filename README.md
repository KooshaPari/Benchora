> **Work state:** SCAFFOLD · **Progress:** `███░░░░░░░ 30%`
> Rust benchmarking framework (gauge); scaffold + bench harness, pre-1.0 · updated 2026-06-02

# gauge

## State

Progress: `[███░░░░░░░] 30%` — pre-1.0 Rust benchmarking scaffold.

_Updated 2026-06-08 — audit pass._

[![CI](https://github.com/KooshaPari/Benchora/actions/workflows/ci.yml/badge.svg)](https://github.com/KooshaPari/Benchora/actions)
[![License](https://img.shields.io/badge/license-Proprietary-lightgrey)](LICENSE)

**Benchmarking and performance testing framework** — Rust-based benchmarking suite for the Phenotype ecosystem.

## Project Overview

Benchora provides performance benchmarking, load testing, and metrics collection for Phenotype projects.

## Key Features

- Rust benchmarking with criterion
- Load testing utilities
- Performance regression tracking
- Metrics collection and reporting

## Quick Start

```bash
# Setup
cd Benchora
cargo build

# Run benchmarks
cargo bench

# Run tests
cargo test
```

## Documentation

- [SPEC.md](./SPEC.md) — Project specification

## Traceability

`/// @trace BENCH-001`

## Description

Rust benchmarking framework (`gauge`) for the Phenotype ecosystem — criterion-based bench harness, load testing, and performance regression tracking.

## Install

`cargo build` (adds `cargo-bench` harness). Requires a recent stable Rust toolchain (see `rust-toolchain.toml`).

## Usage

Run benches: `cargo bench`. Run unit tests: `cargo test`. See `SPEC.md` for the framework contract and `@trace BENCH-001` markers for requirement traceability.

## Contributing

PRs welcome. See `CONTRIBUTING.md`. New bench harnesses follow the existing `criterion` group layout; new metrics exporters go under a dedicated adapter crate.

## License

Proprietary — Phenotype Ecosystem. Internal use only. (Replace with `MIT — see ./LICENSE` once the LICENSE file is committed.)
