# Agentic Flow Architecture

**Status:** CANONICAL SOURCE OF TRUTH  
**Version:** 1.5  
**Updated:** 2026-09-09T10:04:00Z

This file defines the portable architecture. Vendor-specific files such as `CLAUDE.md`, `.claude/agents/*`, OpenCode agent definitions, `GEMINI.md`, or generated `AGENTS.md` variants are **adapters**, not policy authority.

## Source-of-truth hierarchy

When sources disagree, use this order:

1. `ARCHITECTURE.md` — lifecycle, authority and invariants.
2. `schemas/` — task/amendment/classification/evidence/report/usage/history data contracts.
3. `verification/` — surface-specific verification profiles and cross-cutting annexes.
4. `skills/` — reusable procedures, loaded only when their trigger fires.
5. An approved/frozen task contract or approved amendment for the current task.
6. Durable evidence and supervisor decisions for that task.
7. Generated vendor adapters.
8. Conversation memory.

A generated adapter must never silently override canonical layers.

## Core invariant

> Durable project memory; disposable, high-quality working context.

An agent session is replaceable. Project state must be reconstructible after a clear, crash, model change, provider change, or supervisor change.

## Risk-adaptive governance

The framework preserves safety boundaries without forcing high-assurance ceremony onto every change.

### HIGH — architecture / persistence / production semantics

Use when work materially affects architecture, durable data, security/trust boundaries, production semantics, cross-module public contracts, migrations, or other high-impact behavior.

```text
DRAFT TASK
→ DRAFT REVIEW
→ FREEZE
→ SEPARATE APPLY AUTHORIZATION
→ BOUNDED EXECUTION
→ VERIFY + EVIDENCE PACKET
→ BLIND-SPOT / INDEPENDENT CLOSURE REVIEW
→ CHECKPOINT
```

### MEDIUM — bounded same-task correction

```text
OWNER-APPROVED AMENDMENT
→ bounded apply
→ required verification/evidence
→ independent closure when material
```

The amendment keeps original task identity and records reason/scope/STOP conditions plus durable version/hash. Escalate to HIGH if it grants materially new runtime authority or changes architecture/security/persistence/public contracts.

### EVIDENCE_ONLY — docs / test-contract / evidence correction

```text
DURABLE OWNER-APPROVED AMENDMENT
→ hash/ref
→ evidence/doc update
→ closure check if material
```

Separate freeze/apply ceremony is unnecessary unless execution/mutation follows.

### Boundaries that never disappear

Regardless of governance level:

- source of truth stays explicit;
- frozen/approved artifacts have durable identity/hash/ref;
- executor does not self-certify material closure;
- STOP occurs before scope creep or strategy mutation;
- Task N+1 is never silently absorbed;
- missing evidence is never replaced by a plausible-looking substitute;
- report language cannot exceed receipt strength;
- high-risk scope cannot be downgraded merely to save tokens/time.

## Draft → review → apply is a verification-design lifecycle

A material draft is not only an implementation plan. Before APPLY, it defines:

- governance level;
- observed symptom vs hypotheses;
- primary engineering surface and cross-cutting risks;
- affected consumers/systems/environments;
- observable Definition of Done;
- planned closure claims;
- minimum receipt required for each claim;
- selected verification profiles/annexes;
- important checks intentionally out of scope;
- STOP/reclassification/escalation conditions.

Use `prompts/workflow/DRAFT_TASK.md` then `prompts/workflow/REVIEW_DRAFT.md`. The draft reviewer challenges the **verification design** before implementation exists. `ACCEPT_DRAFT` freezes the reviewed contract/version/hash; it does not automatically authorize APPLY unless governance explicitly combines those gates.

If APPLY discovers a materially undeclared surface, consumer, environment, security/persistence/public-contract/production risk or verification requirement:

```text
STOP
→ record evidence
→ classify amendment/reclassification
→ owner/supervisor decision
→ amend/freeze at minimum sufficient governance
→ re-authorize APPLY when required
```

## Change classification and engineering surfaces

Every material code/config task uses `schemas/CHANGE_CLASSIFICATION.md` and `verification/00_INDEX.md`.

### Primary surfaces

- `FRONTEND` — rendered UI, client state, navigation, browser/API-client behavior.
- `BACKEND` — handlers, services/domain logic, jobs/queues and backend integrations.
- `SHARED` — libraries/types/schemas/contracts consumed by multiple surfaces.
- `DATA` — migrations/schema/backfills/durable persistence semantics.
- `INFRA` — cloud/Kubernetes/network/runtime platform configuration.
- `CI_CD` — build/release/deployment orchestration and artifact movement.
- `TOOLING` — repository/developer tooling.
- `DOCS_EVIDENCE` — docs/evidence-only changes without runtime authority.

### Cross-cutting flags

Examples include `AUTH_SECURITY`, `PUBLIC_CONTRACT`, `PERSISTENCE`, `CONCURRENCY`, `CACHE_STATE`, `EXTERNAL_PROVIDER`, `PERFORMANCE`, `MIGRATION`, `OBSERVABILITY`, `PRODUCTION`.

Verification selection is:

```text
GENERAL
+ primary surface profile
+ only triggered cross-cutting annexes
```

Do not hide a shared/public-contract/data/security change inside a simpler FRONTEND/BACKEND label. Classify from actual paths/dependency/contracts/project graph where possible, not filename intuition alone.

## Receipts, claims and report truth

Closure is a bounded statement about observable reality, not effort or model confidence.

All material claims follow `schemas/CLAIM_RECEIPT.md` and reports follow `schemas/STATUS_REPORT.md`.

### Truth classes

```text
OBSERVED      directly visible at an identified ref/artifact/environment
DERIVED       deterministic calculation from named observed inputs
INFERRED      reasoned but not directly established
UNKNOWN       required information missing/unobservable
CONTRADICTED  current receipts conflict with the claim
```

Subjective confidence is not a truth class.

### Verification ladder

From narrow/lower-level to broader evidence:

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

Use the lowest rung that directly establishes the claim. A lower rung does not inherit a stronger claim.

Never silently equate:

```text
plan/intention          != implementation
source/config presence  != runtime behavior
unit/component test     != frontend user flow
HTTP 200                != persistence/downstream effect
screenshot              != successful interaction
mock success            != real boundary compatibility
CI green                != every relevant job/test executed
repository commit       != deployed artifact
reviewer approval       != behavioral evidence
checks A/B found no bug != no bug exists anywhere
```

### Negative/global claims

Words like `all`, `none`, `only`, `no regression`, `secure`, `fully tested`, `nothing else` require a finite named universe plus exhaustive method. Otherwise narrow the report to the actual verification boundary.

Prefer:

```text
128/128 frozen tests passed at <ref>;
browser flows A/B passed in <environment>;
security was not exhaustively assessed.
```

not:

```text
Everything is good; there are no regressions.
```

### Evidence identity and freshness

Material receipts identify the repository ref, artifact/image/build when relevant, environment/config identity and observation time. A later material mutation makes earlier behavioral evidence stale unless continued validity is explicitly established.

## Surface-specific verification

Verification profiles live under `verification/` and are progressive-disclosure artifacts, not permanent prompt content.

### FRONTEND

For user-visible behavior, browser/live receipt is required when the claim exceeds component/logic scope. Check applicable interaction, rendered result, console/network failures, loading/error/empty/permission states, API-client contract, responsive/visual/accessibility semantics when claimed. Screenshot alone proves a state, not the interaction.

### BACKEND

Use handler/service/repository/integration evidence at the boundary appropriate to the claim. Include relevant validation, authz/tenant/ownership, error paths, timeout/retry/idempotency and persistence semantics. `200 OK` alone does not prove durable effect.

### SHARED / PUBLIC CONTRACT

Mechanically identify affected consumers where possible and test/build consumers as well as producer. Type compatibility does not automatically prove runtime serialization/protocol compatibility; contract tests should exercise actual consumer boundary/client code where practical.

### DATA / PERSISTENCE

Migration-file presence is not application proof. Verify representative existing data, forward migration, write/read semantics, constraints, transaction/partial failure, idempotency and rollback/restore boundary as applicable. A new empty test DB does not establish production-shaped migration safety.

### INFRA / CI_CD

Capture target environment/account/cluster/branch identity, plan/rendered diff, permissions, triggers/conditions, artifact handoff and exact deployed artifact. `CI green` does not prove a skipped/neutral job executed. Real pipeline/deployment receipt is required when operational execution itself is the claim.

### SECURITY / AUTH annex

Functional success is not authorization proof. Exercise relevant negative/unauthorized/tenant/ownership path, input/security boundary, fail-open/fallback and secrets/privilege semantics. Standards claims should identify the standard/version/requirement actually verified.

### RELIABILITY / PERFORMANCE annex

Use comparable baseline/treatment methodology, repeated observations where variance matters, explicit cache/warm-state, timeout/retry/concurrency/provider/fallback semantics and bounded log/metric/trace queries. One lucky timing sample is not a performance result.

## Blind-spot audit

For HIGH or evidence-complex MEDIUM closure, broad claims, or known false-complete risk, use `blind-spot-audit` before closure.

It challenges:

- wrong/stale ref/artifact/environment;
- unexpected surface/consumer/scope;
- cache/mock/fallback bypass of changed path;
- weaker proxy replacing frozen acceptance gate;
- frontend hidden runtime/network/error-state gaps;
- backend authz/validation/transaction/retry/provider gaps;
- shared consumer/contract/generated-artifact gaps;
- data migration/existing-data/rollback/idempotency gaps;
- infra/CI skipped stage/wrong target/mutable artifact gaps;
- security negative-path gaps;
- reliability flake/race/cache/timeout/tail/log-query gaps;
- global wording beyond the checked universe;
- reviewer judgment standing in for missing behavioral evidence.

This is falsification, not ritual. Tiny EVIDENCE_ONLY changes do not automatically need it.

## Supervisor architecture

### Independence levels

- `SELF_REVIEW` — useful hygiene; not independent closure.
- `COLD_SAME_MODEL` — separate context/session with no implementation memory.
- `COLD_DIFFERENT_MODEL_OR_HUMAN` — stronger independence where risk/ambiguity warrants it.

Roles are not model brands; use the minimum capable tier consistent with the risk.

### Direct repository/tool access

Preferred order to reduce anchoring:

1. frozen task/DoD/classification;
2. actual diff/source/affected consumers;
3. raw receipts and verification profile;
4. independently selected falsifying checks;
5. executor narrative/status report last.

The reviewer remains read-only during the review pass.

### Evidence-only supervisor

The packet contains immutable task/classification identity, repository/artifact/environment identity, changed paths, exact claims, receipt strengths, commands/results, skipped/not-run checks, DoD matrix, failures, unknowns and residual risks.

The reviewer marks claims `VERIFIED_FROM_PACKET`, `PARTIAL_FROM_PACKET`, `UNVERIFIED_FROM_PACKET` or `CONTRADICTED_BY_PACKET`. Missing access never becomes approval.

### Judgment boundary

A human/model review is a `JUDGMENT` receipt: evidence that a decision was made. It does not replace underlying test/live/persistence/deployment/security evidence for the behavior being judged.

If a stronger/more expensive model performs review or architecture judgment, persist the compact decision artifact, evidence refs, validity boundary, model/provider when observable and timestamp/version—not chain-of-thought or full transcript. Historical judgments remain cold unless a later decision depends on them.

## Roles are not models

- `ORCHESTRATOR` — routes work, curates context, maintains lifecycle state.
- `CHEAP_READONLY` — bounded discovery/inventory/log reduction with no mutation authority by default.
- `EXECUTION_TIER` — bounded implementation and evidence gathering.
- `JUDGMENT_TIER` — architecture, ambiguity, safety, policy, high-risk closure judgment.
- `INDEPENDENT_REVIEWER` — cold/read-only challenge of claims/evidence.
- `HUMAN_OWNER` — authority that cannot be delegated by a skill/model.

A stronger model has greater capability, not automatic truth or authority.

## Model routing and quality invariant

Use the cheapest reliable tier for bounded work while keeping the same acceptance bar.

```text
T0 DETERMINISTIC
  graph queries, grep/AST, lint, formatting, schema checks, test selection

T1 CHEAP_READONLY
  discovery, inventory, log reduction, repetitive classification,
  independent partitions whose outputs can be checked mechanically

T2 STANDARD_EXECUTION
  localized implementation, tests, module-scoped refactors

T3 JUDGMENT
  architecture, ambiguous root cause, security, public-contract changes,
  repeated failed loops, acceptance of known failures, high-risk closure
```

Escalation transfers a compact evidence packet, not a transcript. A cheaper model may gather evidence; it may not weaken Definition of Done, receipt requirements, tests, security boundaries or review requirements. Route changes that claim savings at equal quality should be benchmarked with frozen fixtures.

## Context and token-efficiency policy

Context is working memory, not archive storage. Optimize **signal-to-context ratio**, not token count alone.

For modular repositories define `EDIT_SET`, `REFERENCE_SET`, `EXCLUDED_SET`, and `CHECK_SET`. Expand only when dependency evidence requires it. Use child/subagent contexts as firebreaks for high-volume read-only work and return conclusions, file paths, receipts, unresolved facts and next action rather than transcripts.

### Waste controls

Prefer, in order:

1. deterministic/mechanical discovery before LLM discovery;
2. bounded dependency/affected graphs before whole-repo scans;
3. lazy skill/tool/verification-profile loading;
4. filtered log slices plus raw-artifact refs instead of huge tool results;
5. batched/programmatic tool calls when intermediate roundtrips add no reasoning value;
6. cheap read-only workers for bounded discovery that can be verified;
7. semantic context reset after durable checkpoint;
8. provider caching for stable prefixes when available, remembering caching does not necessarily reduce context occupancy.

When provider/harness usage data is observable, record it using `schemas/USAGE_EVENT.md`. Missing telemetry is `UNKNOWN`, never zero.

### Token/cost budget

Material tasks may declare soft/hard token/cost budgets, expected model tiers and warning conditions. Budgets are observability/steering controls—not permission to lower quality.

On material waste/budget overrun, emit `TOKEN_WASTE_WARNING` with evidence and a quality-preserving alternative. Hard-budget breach or any proposed quality tradeoff requires operator/judgment approval.

## Skill policy

Skills are cold procedures, not permanent prompt text. Default task packet: **0–3 load-bearing skills**. A fourth should be exceptional and justified by a distinct trigger. Verification profiles are separately selected by classification and loaded lazily.

Skill classes:

- `CORE` — general/high-value, expected to recur.
- `COMMON` — useful for a broad task family.
- `RISK_TRIGGERED` — intentionally rare; load only when risk exists.
- `EXPERIMENTAL` — not promoted until evidence justifies it.

Low activation count is not evidence a risk-triggered skill is useless. Promotion/retirement considers eligible-trigger denominator, activation quality, evidence level, false-complete prevention, rework/regressions, token/cost impact and controlled comparisons when causal claims matter.

## Closure

Closure is a claim about evidence, not effort.

Before closure:

1. inspect actual diff/classification;
2. map each frozen DoD/planned claim to adequate current receipts;
3. preserve exact PASS/FAIL/PARTIAL/SKIPPED/UNVERIFIED counts;
4. report important checks not executed;
5. run surface verification and triggered blind-spot audit;
6. narrow unsupported global claims;
7. produce a reality-reflecting status report/evidence packet;
8. obtain required independent judgment.

A simpler test cannot silently replace a frozen acceptance gate. Repeated status/receipt fields should have one authoritative artifact and be referenced rather than copied into every phase.

## Hot state vs cold history

Daily agent context must stay small.

### Hot state

- canonical architecture/map;
- current task/amendment/classification;
- current checkpoint;
- directly relevant module/docs/skills/verification profiles;
- current budget state and unresolved decisions.

### Cold history

- completed task summaries;
- historical evidence packets/status reports;
- supervisor judgments;
- architecture decision history;
- usage/token/cost ledger;
- append-only execution retrospective ledger;
- generated retrospectives and project stories/case studies.

Cold history is indexed/versioned but loaded only on explicit trigger: decision provenance, regression investigation, audit, retrospective, project storytelling or user request.

## Execution retrospective / work reconstruction

For long campaigns, rescues, migrations or work whose execution history itself has engineering value, maintain a compact cold append-only ledger using `schemas/EXECUTION_RETROSPECTIVE_LEDGER.md`.

Record only meaningful boundaries such as:

```text
DRAFT_REVIEW
AMENDMENT
FREEZE
APPLY_START
STOP
EVIDENCE_READY
CLOSURE_REVIEW
CLOSED
FOLLOWUP_CREATED
```

Each entry points to Git/task/judgment/evidence/usage artifacts instead of copying them. A formal retrospective is an on-demand deliverable produced by `project-retrospective`.

Every material historical fact is classified as:

```text
PROVEN FROM GIT / DURABLE ARTIFACTS
RECONSTRUCTED FROM OWNER JOURNAL / RECEIPTS
UNKNOWN / NOT LOGGED RELIABLY
```

Unknown history stays unknown. Never backfill exact counts merely to make the retrospective complete.

## Project history, storytelling and self-branding

`project-retrospective` produces audit-grade timeline/metrics/truth classes. `project-storytelling` turns verified/reconstructed evidence into project history, architecture evolution, incidents, engineering advantages, case studies and self-branding material.

When a retrospective exists, storytelling should consume its bounded outputs/source refs rather than rereading the entire cold history. Generated stories are reader artifacts, not standing agent instructions.

## Documentation versioning and freshness

Canonical project/framework documents expose version and update timestamp/date. Material verified changes trigger documentation-freshness check. Update authoritative source first, then regenerate projections/adapters.

Use indexes to keep old history discoverable without making it always-on context. Obsolete documents should be superseded/archived rather than ambiguously active.

## Generated adapters

`prompts/bootstrap/` contains prompts for creating/updating vendor adapters. Adapters MUST point back to this file, stay concise, preserve vendor-neutral authority, expose skills/verification profiles lazily, encode only vendor-specific mechanics, avoid copying canonical architecture, identify canonical version generated from, and remain regenerable.

## Validation principle

Prefer deterministic enforcement for deterministic rules: scripts, hooks, CI, schemas, permissions, linters, project/dependency graphs and structural tests. Do not spend model judgment on conditions a program can check exactly.

## Evidence before policy promotion

A method/model/skill becomes default because evidence supports it, not because it sounds elegant. Use frozen fixtures and controlled comparisons when claiming a route/skill/reviewer improves quality/cost. Skill evaluation should include trigger accuracy, non-trigger behavior, coexistence and output quality where the harness supports it.
