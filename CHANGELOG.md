# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- README Work State made honest: crate version `0.2.0` exists in-tree but is
  **not** tagged and **not** published to crates.io.
- Install docs now lead with `cargo install --path . --locked` (git install
  documented as alternate). Removed any implication that `cargo install benchora`
  works from crates.io.
- Release attestation workflow no longer soft-fails empty binary staging
  (`find … || true` / `if-no-files-found: warn`); requires `target/release/benchora`.
- Getting-started docs corrected from stale `gauge` crate naming to `benchora` /
  `phenotype_xdd_lib`.

### Notes for first release (T1 — do not cut yet)

When cutting `v0.2.0`:

1. Move this Unreleased section under `## [0.2.0] - YYYY-MM-DD`.
2. Tag `v0.2.0` and create a GitHub Release (attestation workflow attaches artifacts).
3. `cargo publish` to crates.io.
4. Update README install to prefer `cargo install benchora --locked`.

## [0.2.0] — pending

Working tree version in `Cargo.toml`. No git tag or crates.io publish yet.

[Unreleased]: https://github.com/KooshaPari/Benchora/compare/main...HEAD
