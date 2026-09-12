# Benchora PR 107 scorecard repair plan

## Status and scope

This is a planning artifact only. It authorizes no source, workflow, scorer,
threshold, pull-request, scanner, or hosted-check change.

| Field                      | Value                                                                                                                                                                                                                                                                                                                                                                                                    |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Owning repository          | `KooshaPari/Benchora`                                                                                                                                                                                                                                                                                                                                                                                    |
| Published PR               | [#107](https://github.com/KooshaPari/Benchora/pull/107)                                                                                                                                                                                                                                                                                                                                                  |
| Published head             | `668ceed3368b26b32a57e8318c787d9e64a8a173`                                                                                                                                                                                                                                                                                                                                                               |
| Base at inspection         | `8520ca49db1d4da3e42fea2a11c243aff9112eb4`                                                                                                                                                                                                                                                                                                                                                               |
| Owner role                 | Benchora maintainer assigned a future scorecard-only change                                                                                                                                                                                                                                                                                                                                              |
| Phenotype-registry linkage | Local registry routing packet: `/Users/kooshapari/CodeProjects/Phenotype/repos/phenotype-registry/docs/sessions/20260908-researchledger-corpus-audit-routing/` (repository-relative path: `docs/sessions/20260908-researchledger-corpus-audit-routing/`). This owner artifact is committed on an unpublished temporary branch in `/tmp/benchora-107-prep.9U2QCl`; neither path is a hosted Benchora URL. |

The observations below are historical snapshots, not claims about current
hosted state. The last read-only snapshot found the repaired CI gates and
mutation jobs successful; the 88-Pillar scorecard failed at `32/88` against a
threshold of `35`; SonarCloud was failed; and Infisical Sync was queued.

## Established cause

`scripts/scorecard_ci.py` scores file-name heuristics. Three existing Benchora
controls are real but uncounted by those heuristics:

| Pillar        | Existing evidence                                                                        | Current recognition gap                        | Proposed recognition                                                             |
| ------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------------------------------------------- |
| FORMATTING    | `.prettierrc.json`                                                                       | Only `.prettierrc` or `rustfmt.toml` count     | Also recognize `.prettierrc.json`                                                |
| SHIPPING      | `release-plz.toml`, `.github/workflows/release.yml`, `.github/workflows/release-plz.yml` | Only `.releaserc` or `release.config.js` count | Recognize a known release configuration together with an actual release workflow |
| RELEASE_NOTES | `CHANGELOG.md`                                                                           | Only paths named `*release*note*` count        | Recognize root `CHANGELOG.md` as release notes                                   |

The current scorer report was independently reproduced at `32/88`. If, and
only if, those three predicates are implemented and tested as stated, the
arithmetic projection is `35/88`. That projection is UNVERIFIED until the
changed scorer runs in CI.

## Proposed future repair

1. Change only the three predicates in `scripts/scorecard_ci.py`:
   - formatting: include `.prettierrc.json`;
   - shipping: require an existing recognized release configuration and a
     release workflow rather than treating an arbitrary filename as shipping;
   - release notes: include root `CHANGELOG.md`.
2. Add focused positive and negative fixture tests, proposed as
   `tests/test_scorecard_ci.py`. Each fixture must prove a qualifying artifact
   is credited and its absence is not credited. The shipping fixture must
   prove that a configuration file without a release workflow is insufficient.
3. Run the scorecard against the repository and preserve its JSON result. The
   acceptance target is at least `35/88` under the unchanged threshold `35`.

## Dependencies and acceptance gates

| Gate             | Required evidence                                                                                                                                                                                        | Authority / disposition                                     |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Scorer semantics | Focused positive and negative fixture tests                                                                                                                                                              | Benchora maintainer                                         |
| Threshold result | Fresh local and hosted scorecard report at unchanged threshold                                                                                                                                           | Benchora maintainer and CI                                  |
| SonarCloud       | External provider finding reviewed through its documented process                                                                                                                                        | Authorized SonarCloud owner only; no dismissal implied here |
| Infisical Sync   | Fresh hosted result after its queued state resolves                                                                                                                                                      | Workflow/secrets owner; no manual dispatch implied here     |
| Registry linkage | Registry packet: `phenotype-registry/docs/sessions/20260908-researchledger-corpus-audit-routing/`; preserve the local committed/unpublished qualification until this owner artifact has a published path | Root/Mill coordinator                                       |

## Non-goals and limits

- Do not lower the threshold, suppress the scorecard failure, or add empty
  files solely to gain points.
- Do not claim unrelated enterprise or application pillars for this Rust CLI.
- Do not treat a passed local check as hosted CI success.
- Do not dismiss SonarCloud or any scanner finding without the authorized
  provider-specific disposition process.
