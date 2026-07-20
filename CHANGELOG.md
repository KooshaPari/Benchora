# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0] - 2026-07-19

First tagged release candidate. Crate version matches `Cargo.toml`. Cut the
`v0.2.0` git tag and GitHub Release when ready; crates.io publish is T2.

### Changed

- CI `cargo test` is now gating (`continue-on-error` removed from the test job).
- Standalone `cargo-deny` workflow no longer soft-fails (aligned with CI deny job).
- README Work State made honest: crate version `0.2.0` exists in-tree but is
  **not** tagged and **not** published to crates.io until operators cut the tag.
- Install docs lead with `cargo install --path . --locked` (git install as
  alternate). Removed any implication that `cargo install benchora` works from
  crates.io.
- Release attestation workflow no longer soft-fails empty binary staging
  (`find … || true` / `if-no-files-found: warn`); requires `target/release/benchora`.
- Getting-started docs corrected from stale `gauge` crate naming to `benchora` /
  `phenotype_xdd_lib`.
- Action SHA pins: `actions/checkout` unified to v7.0.0 where pinned.

### Operator notes (tag + publish)

See [docs/guides/cutting-a-release.md](docs/guides/cutting-a-release.md).

1. Tag `v0.2.0` and create a GitHub Release (attestation workflow attaches artifacts).
2. T2: `cargo publish` to crates.io.
3. After crates.io succeeds, update README install to prefer
   `cargo install benchora --locked`.

[Unreleased]: https://github.com/KooshaPari/Benchora/compare/v0.2.0...HEAD
[0.2.0]: https://github.com/KooshaPari/Benchora/releases/tag/v0.2.0
