# Agentic Flow Framework — English Reader Guide

**Reader-guide version:** 1.5  
**Updated:** 2026-09-09T10:04:00Z  
**Canonical source of truth:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

This is a synchronized reader-facing guide. If it conflicts with `ARCHITECTURE.md`, the architecture file wins.

## Core idea

> Durable project memory; disposable, high-quality working context.

Version 1.5 adds another invariant:

> A claim may be no broader than the identified, current receipt that directly establishes it.

The framework separates task authority, implementation, verification and judgment so reports describe observed reality rather than agent confidence.

## Material task lifecycle

For HIGH-risk work:

```text
REQUEST
→ DRAFT TASK
→ REVIEW DRAFT
→ FREEZE
→ SEPARATE APPLY AUTHORIZATION
→ APPLY
→ VERIFY + REALITY REPORT
→ BLIND-SPOT / INDEPENDENT CLOSURE
→ CHECKPOINT
```

MEDIUM and EVIDENCE_ONLY governance remain lighter where risk permits, but source-of-truth, durable identity, STOP-before-scope-creep, no invented evidence and bounded reporting remain invariant.

## Classify engineering surface before verification

Material work uses a primary surface:

```text
FRONTEND
BACKEND
SHARED
DATA
INFRA
CI_CD
TOOLING
DOCS_EVIDENCE
```

plus cross-cutting flags such as security/auth, persistence, public contract, cache, concurrency, external provider, performance, migration, observability and production.

Verification is selected lazily:

```text
GENERAL
+ primary surface
+ only triggered cross-cutting annexes
```

Classification should use actual dependency/contracts/project-graph evidence when possible. A file in a frontend directory can still be a SHARED/PUBLIC_CONTRACT change if multiple consumers depend on it.

## Draft review is verification-design review

Before APPLY, the task freezes:

- observable goal and DoD;
- affected consumers/systems/environments;
- planned closure claims;
- minimum receipt required for each claim;
- selected verification profiles;
- important checks intentionally not required;
- STOP/reclassification/escalation conditions.

`prompts/workflow/REVIEW_DRAFT.md` challenges this design before implementation begins.

## Claim truth and verification ladder

Material statements use:

```text
OBSERVED
DERIVED
INFERRED
UNKNOWN
CONTRADICTED
```

Verification ladder:

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

A lower rung cannot support a stronger claim by narrative alone.

Examples:

```text
source/config exists        != runtime behavior
unit/component test         != frontend user flow
HTTP 200                    != durable persistence
screenshot                  != working interaction
mock success                != real boundary compatibility
CI green                    != every relevant test/job executed
repository commit           != deployed artifact
reviewer/model approval     != underlying behavioral receipt
```

Global language such as `all`, `none`, `no regressions`, `secure`, `fully tested`, `nothing else` requires a named finite universe plus exhaustive method. Otherwise narrow the report.

## Surface verification

### FRONTEND

For user-visible claims use browser/user interaction at the real rendered surface. Check applicable console/network errors, loading/error/empty/permission states, frontend API-client contract and visual/accessibility semantics when claimed. A screenshot proves a state, not a flow.

### BACKEND

Verify at the handler/service/repository boundary appropriate to the claim. Include relevant validation, authz/tenant paths, errors, timeout/retry/idempotency, provider behavior and persistence. HTTP success alone is not a durable-state receipt.

### SHARED / PUBLIC CONTRACT

Mechanically find affected consumers where possible. Test/build consumers as well as producer. Type compatibility does not automatically prove runtime serialization/protocol compatibility; exercise real boundary/client code for contract claims where practical.

### DATA

Verify representative existing data, migration behavior, durable write/read, constraints, partial failure, idempotency and rollback/restore boundary. A migration file or clean empty DB is not sufficient for production-shaped migration claims.

### INFRA / CI_CD

Verify exact target environment, plan/rendered diff, identity/permissions, trigger/branch conditions, artifact handoff and deployed artifact. Green CI can include skipped/neutral checks; report what actually ran.

### SECURITY / AUTH

Check relevant negative/unauthorized/tenant/ownership paths and the actual trust boundary. Standards coverage must name the standard/version/requirement; functional success alone is not a security receipt.

### RELIABILITY / PERFORMANCE

Use comparable baseline/treatment methodology, repeated measurements where variance matters and explicit cache/retry/timeout/concurrency/provider/log-query boundaries.

## Blind-spot audit

For HIGH/evidence-complex MEDIUM closure or broad claims, `blind-spot-audit` challenges common false-complete paths:

```text
wrong/stale ref or environment
unexpected surface/consumer
cache/mock/fallback bypass
passing test that never executes changed code
weaker proxy replacing frozen gate
frontend hidden console/error-state gap
backend authz/transaction/retry gap
shared consumer/contract gap
data migration/rollback/idempotency gap
infra/CI skipped stage or artifact mismatch
security negative-path omission
flaky/racy/performance methodology gap
global report wording beyond checked universe
reviewer judgment used as missing behavioral evidence
```

## Independent review

Preferred direct-access review order reduces anchoring:

```text
frozen task/DoD/classification
→ actual diff/source
→ raw receipts/checks
→ independent falsifying checks
→ executor narrative last
```

Review independence can range from self-review hygiene to a cold same-model session or a cold different-model/human review. Reviewer output is `JUDGMENT`; it cannot manufacture missing runtime evidence.

## Reality-reflecting reports

Use `schemas/STATUS_REPORT.md` and `schemas/EVIDENCE_PACKET.md`.

Reports identify repository ref, artifact/environment when relevant, exact checks/counts, checks not executed, known failures, unknowns and residual risk.

Prefer:

```text
128/128 required tests passed at commit abc123.
Browser flows A/B passed in testenv X.
Production deployment was not checked.
```

not:

```text
Everything is good; no regressions.
```

## Deterministic lint

Structured JSON artifacts, or YAML when PyYAML is installed, can be mechanically checked:

```bash
python3 scripts/verification_lint.py <task/evidence/report files>
```

It catches mechanical contradictions such as VERIFIED-without-evidence, missing evidence refs, stale head refs, receipt below frozen minimum, DoD PASS without receipt and verified global claims without exhaustive bounded evidence. Semantic sufficiency still requires project verification and judgment.

## Model/token efficiency

Semantic routing remains:

```text
T0 deterministic/mechanical
T1 cheap read-only discovery/partition
T2 standard bounded execution
T3 judgment/high-risk review
```

Use cheap workers only when the same acceptance bar can be preserved and checked. Keep all verification profiles, historical tasks and judgments out of standing context; load only what current classification/risks require.

## Cold history and storytelling

Completed tasks, classifications, reports, evidence, judgments, usage, execution ledger, retrospectives and stories remain cold. On-demand `project-retrospective` reconstructs audit-grade history; `project-storytelling` converts bounded evidence into architecture narrative/case study/self-branding without making raw history permanent coding context.

## Start here

1. `README.md`
2. `ARCHITECTURE.md`
3. matching `prompts/bootstrap/*`
4. `DRAFT_TASK.md`
5. `REVIEW_DRAFT.md`
6. current task + classified verification profiles + triggered skills only
7. `APPLY_TASK.md`
8. `VERIFY_AND_REPORT.md`
9. required supervisor prompt

Dated primary-source evidence for this update is under `research/2026-09-09-verification-blind-spots.md`.
