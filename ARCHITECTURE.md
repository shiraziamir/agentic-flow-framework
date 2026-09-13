# Agentic Flow Architecture

**Status:** CANONICAL SOURCE OF TRUTH  
**Version:** 1.9  
**Updated:** 2026-09-13

Agentic Flow is a repository-first, vendor-neutral operating architecture for coding agents. This file is intentionally a **small canonical map + invariant set**. Detailed contracts live in lower layers and are loaded only when the active task triggers them.

## 1. Source-of-truth hierarchy

When sources disagree, use this order:

1. `ARCHITECTURE.md` — authority, lifecycle and invariants.
2. `schemas/` — durable task/evidence/project/approval contracts.
3. `verification/` — claim-aware verification profiles.
4. `production/` — environment/production-readiness profiles.
5. `skills/` — triggered reusable procedures.
6. approved current project/task/amendment/profile state.
7. receipts, gaps, overrides and reviewer decisions.
8. generated vendor adapters.
9. conversation memory.

Reader docs, research, historical reports and generated exports are explanatory/cold layers, not higher authority.

## 2. Core invariants

> Durable project memory; disposable working context.

> A claim may be no broader than the current receipt that directly establishes it.

> Quality requirements stay fixed; process ceremony adapts to risk.

> An Executor that can edit a behavior but cannot exercise the real changed path is not execution-ready for that claim.

> Remediation autonomy is not scope autonomy.

> Unknown/unowned dirty work is protected state.

> Task authority, mutation authority, environment authority and external-side-effect authority are separate.

> Production readiness is evidenced capability plus explicit gaps—not a badge.

Agent/model/provider sessions are replaceable. Project state must survive reset or handoff without replaying full chat history.

## 3. Progressive disclosure

Humans should not read the whole repository to begin. The normal human route is:

```text
README.md
→ docs/GETTING_STARTED.md
→ docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
→ docs/GUIDE.fa.md when Persian guidance is preferred
```

The normal Executor route is:

```text
docs/agent/START_HERE.md
→ current project profile + current task
→ only triggered schemas/profiles/skills
```

Do not preload research, operator manuals, historical tasks, all production profiles or the full schema shelf.

## 4. Adoption modes

- **NEW / IDLE:** discover project reality, establish/map the project profile, validate build/test/environment entrypoints, then stop before product mutation unless authorized.
- **EXISTING MATURE:** reuse valid CI/CD, observability, security and architecture; do not create shadow systems.
- **MIDSTREAM:** snapshot branch/HEAD/dirty state/current task/tests/environment first; preserve existing work; never fabricate retroactive approval.

The framework can be cloned directly or distributed as a generated portable bundle. Distribution does not change authority semantics.

## 5. Project baseline

A target project should normally maintain:

```text
.agentic/PROJECT_PROFILE.yaml
```

Use `schemas/PROJECT_PROFILE_CONFIG.md` and `templates/PROJECT_PROFILE.example.yaml`.

The profile defines intended testing, execution readiness, mutation modes, environment permissions, review policy, workspace safety, external effects and production expectations. It is not proof that those expectations are satisfied.

Temporary exceptions use `schemas/TEMPORARY_OVERRIDE.md`; they are explicit, owned, expiring and do not silently rewrite the baseline.

## 6. Risk and work kind are separate

New task contracts should represent two dimensions:

```text
risk.level = LOW | MEDIUM | HIGH
work_kind  = IMPLEMENTATION | REMEDIATION | EVIDENCE_ONLY
```

Legacy `governance: HIGH|MEDIUM|EVIDENCE_ONLY` remains readable during migration, but `EVIDENCE_ONLY` is a work kind, not a risk level.

Default workflow:

```text
LOW
execute → focused test → compact self-review → report

MEDIUM
short preflight → execute → cold review → bounded remediation → Manager review

HIGH
frozen contract
→ failure-surface preflight
→ separate initial apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated review
→ controlled remediation window when safe
→ final / independent closure when required
```

HIGH risk means stronger boundaries/evidence, not human approval for every tiny correction.

## 7. Task design before mutation

Material tasks define:

- observable goal and Definition of Done;
- in-scope/out-of-scope surfaces;
- planned closure claims;
- minimum receipt for each claim;
- required environment and real boundaries;
- intentionally omitted checks;
- STOP/escalation conditions.

The frozen contract owns **WHAT + SUCCESS**. The Executor owns the smallest conforming **HOW**.

Engineering guidance may use:

```text
MUST         frozen/owner invariant
SHOULD       evidence-backed recommendation
INVESTIGATE  fact to establish before mutation
AVOID        likely failure/design/test trap
```

Model recommendations do not become `MUST` merely because they are confidently written.

## 8. Failure-surface preflight

For material behavior changes, inspect before coding:

```text
NORMAL PATH
BOUNDARY / INVALID INPUT
DEPENDENCY OR I/O FAILURE
CLEANUP / ROLLBACK FAILURE
OBSERVABILITY / HEALTH PROPAGATION
TEST-ORACLE FALSIFICATION
```

Add only when triggered:

```text
THREAD / PROCESS CONCURRENCY
CRASH / RESTART
DURABILITY / PARTIAL WRITE
PERMISSION / IDENTITY
EXTERNAL PROVIDER
MIGRATION / SCHEMA
CACHE / CONSISTENCY
```

The goal is broader first-pass reasoning, not universal exhaustive testing.

## 9. Designer → Manager → Executor

For material work:

```text
Operator intent
→ Designer: evidence-bound contract + advisory proposal
→ Manager: review/freeze + bounded authority
→ Executor: preflight + implementation + receipts on isolated branch/PR
→ cold/adversarial review
→ Manager: exact diff/commit + evidence review
→ authorized merge/closure
```

The Designer does not self-authorize. The Manager does not accept narrative instead of real diff/source/receipts. The Executor cannot expand scope or self-certify material closure.

Direct Git access with branch/PR isolation is preferred for material code. Context packets are degraded-access alternatives, not equal substitutes for high-risk direct review.

## 10. Mutation authority and controlled remediation

Use `schemas/MUTATION_APPROVAL_POLICY.md`.

Supported modes:

```text
STRICT_PREVIEW
MATERIAL_CHANGES_ONLY
BOUNDED_AUTONOMY
```

`STRICT_PREVIEW` means one bounded preview/approval per coherent mutation batch—not line-by-line permission spam.

After a consolidated Manager review, same-task findings may enter a controlled remediation window with explicit findings, allowed paths/change classes and a configurable iteration limit. A new provider, migration, public contract, security boundary, production action, dependency, architecture strategy or out-of-scope resource invalidates the window and requires STOP + revised authority.

## 11. Workspace and external-effect safety

Uncommitted work is protected unless ownership is known. Potentially destructive operations such as hard reset, clean, force checkout/push or blind restore require dirty-state inspection and appropriate authority when loss is possible.

Unknown ownership means preserve.

Test authority does not imply permission for real provider calls, paid API usage, sending messages/notifications, deployments, destructive data operations or production mutation. External side effects need explicit authority according to project policy.

## 12. Verification and receipts

Use `schemas/CLAIM_RECEIPT.md`, `schemas/STATUS_REPORT.md` and `verification/00_INDEX.md`.

Truth classes:

```text
OBSERVED | DERIVED | INFERRED | UNKNOWN | CONTRADICTED
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

Do not equate source presence with runtime, unit green with user flow, HTTP 200 with persistence, CI green with deployment, backup configuration with restore proof, or reviewer confidence with behavioral evidence.

Capability wording remains separate:

```text
DESIGNED
IMPLEMENTED_IN_SOURCE
MECHANICALLY_TESTED
QUALIFIED_IN_NAMED_ENVIRONMENT
LIVE_BEHAVIOR_PROVEN
DEPLOYED_ARTIFACT_PROVEN
PRODUCTION_BEHAVIOR_PROVEN
```

## 13. Evidence environment

Use `production/AGENT_ENVIRONMENTS.md` and `schemas/EVIDENCE_RECOVERY.md`.

Environment ladder:

```text
LOCAL / HERMETIC
→ LOCAL_REAL / EPHEMERAL TEST
→ SHARED TEST
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ
→ PRODUCTION MUTATION
```

Use the lowest authorized environment that proves the planned claim. Mocks prove the modeled interaction only. Mock-only evidence cannot silently close persistence, migration, integration, user-flow, deployment or production claims.

If the required environment is unavailable, report `UNVERIFIED` or `BLOCKED`; do not weaken the receipt while retaining the stronger claim.

Wrong/stale-runtime evidence is preserved and classified, including `VOID_FOR_CLAIM` where appropriate. Evidence recovery does not silently authorize new product scope.

## 14. Tests and adversarial review

Define test/receipt strategy before APPLY for material claims. Prefer the smallest test layer that directly proves the claim. For load-bearing safety/regression tests, use mutation/path/falsification proof when risk warrants it.

Before Manager attention on MEDIUM/HIGH work, prefer a cold/read-only adversarial review of the actual diff and nearby source to catch obvious local defects, weak test oracles, cleanup leaks, concurrency gaps, missing observability propagation and scope drift.

Manager review should return consolidated findings where practical.

## 15. Compact reports, rich evidence

Evidence richness does not require verbose status reports. Keep raw logs/artifacts separately and use compact claim-index receipts.

Reports state actual `PASS | FAIL | PARTIAL | SKIPPED | UNVERIFIED` outcomes and explicit gaps.

## 16. Production engineering

Use `schemas/PRODUCTION_PROFILE.md`, `schemas/OPERATIONAL_GAP.md` and `production/00_INDEX.md`.

Production readiness covers delivery, security, observability, data durability, troubleshooting, resilience, architecture and test/environment strategy. Missing capabilities remain explicit:

```text
NOT_IMPLEMENTED | PARTIAL | UNVERIFIED | BLOCKED | ACCEPTED_RISK | CLOSED
```

> Backup success is not recoverability proof. Restore is the receipt.

Patterns are selected for real volatility/failure/security/testability boundaries, not to satisfy a pattern checklist.

## 17. Model/context/cost efficiency

Semantic model tiers:

```text
T0 DETERMINISTIC       graph/query/lint/schema/test selection
T1 CHEAP_READONLY      discovery/inventory/log reduction
T2 STANDARD_EXECUTION  bounded implementation/tests
T3 JUDGMENT            architecture/security/ambiguity/high-risk closure
```

Use the cheapest reliable tier without weakening acceptance quality. Escalation sends compact evidence, not transcript.

Quota/usage telemetry is an operator/routing signal, never engineering evidence and never permission to skip required verification.

## 18. Measure Flow friction

For material tasks, cheap counters may track:

```text
first_pass_review_passed
remediation_iterations
manager_review_rounds
authorization_round_trips
unplanned_scope_escalations
environment_blocked
agent_safety_incidents
task_cycle_time (optional)
```

These are process-improvement telemetry, not developer-performance scores. Use them to distinguish genuine quality cost from agent defects, governance friction and environment friction.

## 19. Hot state vs cold history

Hot state: current task/amendment/profile pointers, relevant source, selected verification/production profiles, triggered skills and unresolved decisions.

Cold state: completed tasks/evidence, incidents, closed gaps, historical judgments, research, retrospectives, stories and large logs.

Do not store chain-of-thought or full transcripts as project state.

## 20. Validation principle

Prefer deterministic enforcement for deterministic facts: schemas, graph checks, linters, tests, artifact hashes, permissions and CI. Spend model judgment where ambiguity exists.

A method/model/skill/pattern/control becomes default because risk and evidence justify it—not because it sounds sophisticated.
