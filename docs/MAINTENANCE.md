# CI workflow fixes (2026-07-05)

Three workflow reds identified in audit `a40421011d2dbd6fc` resolved:

## 1. `.github/workflows/audit.yml` — rustsec/audit-check SHA re-pin

- Pinned SHA `69361f4c6cee81593d1f8db7f211e6312d330eaa` was rejected (no longer
  present in upstream `rustsec/audit-check`).
- Re-pinned to verified stable SHA `3ae01282e2311f82d96cc2181b31c4fbe3dd00c0`
  (last upstream release on `main`; tagged v2 in upstream README).
- Commit: `ci(audit): re-pin rustsec/audit-check to 3ae01282 (v2)`

## 2. `.github/workflows/bench-gate.yml` — invalid `cargo mutants` flag

- `cargo mutants` v27.x no longer accepts `--minimum-pass-rate`.
- Only `--minimum-test-timeout` is a stable CLI flag; mutation score gating
  happens via the JSON report (or via `--fail-fast` semantics).
- Removed the offending line. Mutation score threshold continues to be enforced
  by a downstream parser / annotation step (NOT removed — see BEN-SOTA-002).
- Commit: `ci(bench-gate): remove invalid --minimum-pass-rate flag (cargo mutants v27.x)`

## 3. `.github/workflows/docs.yml` — transient GH Pages deploy failure

- First deploy run returned *"Deployment failed, try again later"* (known
  intermittent GH Pages backend error).
- Re-dispatched via `gh workflow run`; second run `28738598083` completed
  green at `2026-07-05T11:03:57Z`.
- No code change required; docs deploys continue to use current pinned action
  SHAs (`actions/checkout@9c091bb2…`, `actions/setup-node@4c8b55a0…`,
  `actions/configure-pages@045bfe01…`, `actions/upload-pages-artifact@fc324d35…`,
  `actions/deploy-pages@cd2ce8fc…`).

## Branch

All changes landed on branch `fix/benchora-workflow-reds`. PR opens from this
branch into `main`.
