# Benchora CLI Reference

All commands accept `--db <path>` (env: `BENCHORA_DB`). Default: `benchora.db`.

## `benchora run`
Run a benchmark suite and capture a report.

```bash
benchora run --suite core
benchora run --suite mutation --out results.json
```
| Flag | Default |
|------|---------|
| `--suite <name>` | `core` |
| `--out <path>` | `<suite>-<timestamp>.json` |

## `benchora report`
Summarize a saved report to stdout.

```bash
benchora report core-20260722-120000.json
```

## `benchora baseline`
Promote a report to a named baseline.

```bash
benchora baseline nightly --from core-20260722-120000.json
```

## `benchora compare`
Diff a current report against a stored baseline.

```bash
benchora compare nightly --current results.json
benchora compare nightly --current results.json --regression-threshold-pct 3.0
```
| Flag | Default |
|------|---------|
| `--current <path>` | (required) |
| `--regression-threshold-pct <PCT>` | `5.0` / `BENCHORA_REGRESSION_THRESHOLD_PCT` |

## `benchora mutate`
Run mutation testing via `cargo mutants`.

```bash
benchora mutate --package phenotype-xdd-lib
benchora mutate --package my-crate --file src/auth.rs --min-score 80
```
| Flag | Default |
|------|---------|
| `--package <pkg>` | (all) |
| `--file <path>` | (all files) |
| `--min-score <PCT>` | (none) |
| `--output <dir>` | `mutants-out` |

## `benchora list`
List stored baselines, reports, or mutation results.

```bash
benchora list baselines
benchora list reports
```
| Arg | Default |
|-----|---------|
| `<kind>` | `baselines` |
