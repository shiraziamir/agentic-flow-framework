# Verification Profiles Index

**Version:** 1.2  
**Updated:** 2026-09-09T10:40:00Z

Verification is selected from change classification. Do not run every profile on every task.

## Verification vs production readiness

These answer different questions:

```text
verification/  → What receipts directly establish this task/change claim?
production/    → What operating bar must this project meet to build/deploy/observe/recover securely?
```

A task can be verification-complete while the project still has production gaps. A production profile does not replace code-path/behavior verification.

When a material task can affect production posture, use both routers lazily: selected verification profiles here + only affected profiles from `production/00_INDEX.md`.

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

| Flag / kind | Annex / extra |
|---|---|
| `AUTH_SECURITY` | [`SECURITY_AUTH.md`](SECURITY_AUTH.md) |
| `PERFORMANCE`, `CONCURRENCY`, `CACHE_STATE`, `EXTERNAL_PROVIDER`, `OBSERVABILITY` | [`RELIABILITY_PERFORMANCE.md`](RELIABILITY_PERFORMANCE.md) |
| `PERSISTENCE`, `MIGRATION` | `DATA.md` in addition to primary profile |
| `PUBLIC_CONTRACT` | `SHARED.md` plus relevant producer/consumer primary profiles |
| `PRODUCTION` | `INFRA_CI.md` plus relevant application profile; additionally consult project production profile |
| `DEPENDENCY_SUPPLY_CHAIN` or material `DEPENDENCY` | [`DEPENDENCY_SUPPLY_CHAIN.md`](DEPENDENCY_SUPPLY_CHAIN.md) |
| load-bearing `TEST_ONLY` | primary profile + `test-mutation-proof` Skill when practical |

## Selection rule

```text
GENERAL + primary surface + triggered cross-cutting annexes
```

Task contract freezes the planned set. If APPLY discovers a new material surface/flag, STOP and amend rather than silently weakening/expanding verification.

## Verification ladder

Profiles choose from `schemas/CLAIM_RECEIPT.md`:

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

Use the lowest level that directly establishes each claim; a lower-level receipt never inherits a stronger claim.

## Extensibility

The primary-surface vocabulary is intentionally small. A target project may define project-local profiles (native mobile/desktop, embedded, ML/data-pipeline, protocol-specific clients, etc.) when materially different verification semantics exist. They must preserve the same claim/receipt/reporting/STOP-amendment authority rather than creating a second policy system.