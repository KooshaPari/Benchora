# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- README Install prefers `cargo install benchora --locked` after crates.io publish of `0.2.0`.
- Work State reflects tagged Release + published crate.

## [0.2.0] - 2026-07-19

First tagged release. Crate version matches `Cargo.toml`. Git tag `v0.2.0`,
GitHub Release, and crates.io publish (`benchora` 0.2.0) are complete.

### Changed

- CI `cargo test` is now gating (`continue-on-error` removed from the test job).
- Standalone `cargo-deny` workflow no longer soft-fails (aligned with CI deny job).
- README Work State: crate version `0.2.0` prepared for tag/Release (T1) and
  crates.io (T2).
- Install docs led with `cargo install --path . --locked` until crates.io
  publish; post-publish README prefers `cargo install benchora --locked`.
- Release attestation workflow no longer soft-fails empty binary staging
  (`find … || true` / `if-no-files-found: warn`); requires `target/release/benchora`.
- Getting-started docs corrected from stale `gauge` crate naming to `benchora` /
  `phenotype_xdd_lib`.
- Action SHA pins: `actions/checkout` unified to v7.0.0 where pinned.

### Operator notes

See [docs/guides/cutting-a-release.md](docs/guides/cutting-a-release.md) for the
next version cut. `v0.2.0` tag, Release, and crates.io publish are done.

[Unreleased]: https://github.com/KooshaPari/Benchora/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/KooshaPari/Benchora/releases/tag/v0.2.0
