# Verification Profiles Index

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Verification is selected from the change classification. Do not run every profile on every task.

## Base profile

Always start with [`GENERAL.md`](GENERAL.md).

## Primary surface profiles

| Surface | Profile |
|---|---|
| `FRONTEND` | [`FRONTEND.md`](FRONTEND.md) |
| `BACKEND` | [`BACKEND.md`](BACKEND.md) |
| `SHARED` | [`SHARED.md`](SHARED.md) |
| `DATA` | [`DATA.md`](DATA.md) |
| `INFRA` / `CI_CD` | [`INFRA_CI.md`](INFRA_CI.md) |
| `TOOLING` / `DOCS_EVIDENCE` | [`TOOLING_DOCS.md`](TOOLING_DOCS.md) |

## Cross-cutting annexes

| Flag | Annex |
|---|---|
| `AUTH_SECURITY` | [`SECURITY_AUTH.md`](SECURITY_AUTH.md) |
| `PERFORMANCE`, `CONCURRENCY`, `CACHE_STATE`, `EXTERNAL_PROVIDER`, `OBSERVABILITY` | [`RELIABILITY_PERFORMANCE.md`](RELIABILITY_PERFORMANCE.md) |
| `PERSISTENCE`, `MIGRATION` | `DATA.md` in addition to the primary profile |
| `PUBLIC_CONTRACT` | `SHARED.md` plus relevant producer/consumer primary profiles |
| `PRODUCTION` | `INFRA_CI.md` plus relevant application profile |

## Selection rule

`GENERAL + primary surface + triggered cross-cutting annexes`

The task contract freezes the planned profile set. If APPLY discovers a new material surface/flag, STOP and amend rather than silently weakening or expanding verification.

## Verification ladder

Profiles choose from the common ladder in `schemas/CLAIM_RECEIPT.md`:

```text
IDENTITY
→ STATIC
→ BUILD
→ FOCUSED_TEST
→ PATH_PROOF
→ INTEGRATION_CONTRACT
→ LIVE_BEHAVIOR
→ DEPLOYED_ARTIFACT
→ EXHAUSTIVE_BOUNDED_NEGATIVE
→ JUDGMENT
```

Use the lowest level that directly establishes each claim; do not confuse a lower-level receipt with a higher-level claim.
