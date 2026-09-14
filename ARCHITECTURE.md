# Agentic Flow Architecture

**Status:** CANONICAL SOURCE OF TRUTH  
**Version:** 1.11  
**Updated:** 2026-09-14

Agentic Flow is a repository-first, vendor-neutral operating architecture for coding agents. This file is intentionally a **small canonical map + invariant set**. Detailed contracts live in lower layers and are loaded only when the active project/task triggers them.

## 1. Source-of-truth hierarchy

When sources disagree, use this order:

1. `ARCHITECTURE.md` — authority, lifecycle and invariants.
2. `schemas/` — durable project/task/evidence/approval contracts.
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

> Human transports authority; repository transports engineering state.

> Product intent must become constraints before it becomes architecture.

> VIBE_PROTOTYPE is a learning mode, not a production baseline.

> Freeze hard-to-change invariants; keep easy-to-change implementation choices open until evidence justifies them.

> Unmeasured complexity must not become architecture by accident.

> **Every material change is viewed through Local correctness and System truth, with ceremony proportional to risk.**

> A locally correct function does not prove that data authority, recovery, tenant isolation, privacy, cost, observability or another subsystem still tells the truth.

> Caches, projections, summaries and metrics are not authoritative merely because they are convenient to read.

> **Recency is not priority. Conversational momentum cannot promote a side task.**

> At any moment there is one durable `PRIMARY_TASK`; side work remains explicitly subordinate unless promoted by authorized decision.

> A claim may be no broader than the current receipt that directly establishes it.

> Mock-only evidence cannot silently inherit integration, deployment or production semantics.

> Multi-model agreement is review coverage, not independent behavioral evidence.

> Quality requirements stay fixed; process ceremony adapts to risk.

> An Executor that can edit a behavior but cannot exercise the real changed path is not execution-ready for that claim.

> Remediation autonomy is not scope autonomy.

> Unknown/unowned dirty work is protected state.

> Task authority, mutation authority, environment authority and external-side-effect authority are separate.

> Production readiness is evidenced capability plus explicit gaps—not a badge.

> Every production mutation requires rollback or explicit forward-recovery readiness before execution.

Agent/model/provider sessions are replaceable. Project state must survive reset or handoff without replaying full chat history.

## 3. Project lifecycle before task lifecycle

A new/early-stage project does not begin with the normal coding task loop.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ 2–3 MINIMAL OPTIONS when meaningful
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PROJECT BASELINE
→ NORMAL TASK FLOW
```

The Product Owner owns WHY / WHAT / business trade-offs. The Project Architect owns system-shape discovery. The Executor owns implementation after the baseline is sufficiently coherent.

Canonical guide: `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`.

## 4. Project development modes and operating presets

Project mode describes **what phase the product is in**:

```text
VIBE_PROTOTYPE
PRODUCT_BUILD
MAINTENANCE
```

Operating preset describes **how much default ceremony/assurance to apply**:

```text
VIBE_FAST
PRODUCT_STANDARD
HIGH_ASSURANCE
```

Use the preset as the starting configuration and override only what the project actually needs. Presets never override explicit security, production, external-effect or evidence requirements.

### VIBE_PROTOTYPE / VIBE_FAST

Optimizes for learning speed. Architecture may be provisional and code may be sacrificial. It does not grant production-readiness claims, sensitive-data authority, or production mutation.

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

Promotion to `PRODUCT_BUILD` requires explicit re-baselining and classification of prototype code as `REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD`.

### PRODUCT_BUILD / PRODUCT_STANDARD

Default for a maintainable product. Requires product/quality constraints and load-bearing architecture to be explicit enough to guide implementation. Broad feature expansion should not outrun the walking skeleton and architecture checkpoint.

### HIGH_ASSURANCE

Use when money, identity, privacy, tenant isolation, destructive operations, critical durability, regulated data or high-consequence production behavior makes stronger review/evidence justified. It increases assurance, not bureaucracy for its own sake.

### MAINTENANCE

Uses the established baseline and normal task lifecycle. Return to architecture discovery when a material boundary changes or the Swamp Guard indicates local patches are compounding structural debt.

## 5. Swamp Guard

The Swamp Guard is evaluated at material checkpoints and before architecture/tooling expansion.

```text
CLEAR
WATCH
ALERT
STOP_REBASELINE
```

Typical signals include:

- repeated architecture churn or rewrites in the same subsystem;
- repeated remediation beyond the normal bounded loop;
- new abstractions/frameworks/datastores without a product constraint or failure boundary;
- multiple mechanisms competing for one responsibility;
- AI/RAG tuning without a representative eval baseline;
- feature growth before a real end-to-end vertical slice works;
- architecture decisions existing only in chat;
- duplicate/ambiguous sources of truth or state ownership;
- operational complexity growing faster than demonstrated product value;
- prototype code silently acquiring production expectations;
- a `SIDE_TASK` consuming repeated rounds, architecture attention or implementation scope beyond its bounded purpose;
- the current `PRIMARY_TASK` disappearing from checkpoints while a recent side issue becomes the de-facto optimization target;
- repeated System-Lens `OPEN_RISK` findings being carried forward without a decision;
- caches/projections becoming de-facto business authority without an explicit architecture decision.

Use `STOP_REBASELINE` when continuing would compound structural debt or safety risk—for example unresolved sensitive-data boundaries, prototype-to-production drift, major architecture change without decision/evidence, source-of-truth ambiguity causing repeated defects, or RAG optimization with no measurable eval contract.

Required alert:

```text
SWAMP ALERT: <WATCH|ALERT|STOP_REBASELINE>
Signal: ...
Evidence: ...
Why it matters: ...
Recommended action: ...
Continue allowed: YES|NO
Authority needed: ...
```

The framework itself is subject to this rule: prefer simplification and validation over adding governance concepts when policy surface grows faster than demonstrated value.

## 6. Progressive disclosure

Humans should not read the whole repository to begin. The normal human route is:

```text
README.md
→ docs/GETTING_STARTED.md
→ docs/operator/OPERATOR_GUIDE.*.md
→ docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md when baseline is missing/new
→ docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

The normal Executor route is:

```text
docs/agent/START_HERE.md
→ current project mode + operating preset/profile
→ project inception when baseline is missing
→ current PRIMARY_TASK + active task role
→ only triggered schemas/profiles/skills
```

Do not preload research, operator manuals, historical tasks, all production profiles or the full schema/Skill shelf.

## 7. Adoption modes

- **NEW / IDLE:** determine project mode + operating preset. If greenfield or architecture is untrusted, run Project Inception before serious product mutation.
- **EXISTING MATURE:** reuse valid architecture/CI/CD/observability/security; do not create shadow systems.
- **MIDSTREAM:** snapshot branch/HEAD/dirty state/current task/tests/environment first; preserve existing work; never fabricate retroactive approval.

## 8. Project baseline and System Truth Map

A target project should normally maintain:

```text
.agentic/PROJECT_PROFILE.yaml
```

Use `schemas/PROJECT_PROFILE_CONFIG.md` and `templates/PROJECT_PROFILE.example.yaml`.

For `PRODUCT_BUILD`, and for any stateful/cost/privacy/tenant-sensitive system, maintain:

```text
.agentic/SYSTEM_TRUTH_MAP.yaml
```

Use `schemas/SYSTEM_TRUTH_MAP.md` and `templates/SYSTEM_TRUTH_MAP.example.yaml`. The map records entry/trust boundaries, stores/caches/queues/providers/workers, authoritative data and derived copies, restart/failure/recovery behavior, tenant isolation, current scale boundaries and cross-system audit state.

The map is a model of system relationships, not runtime proof. Update it when a material authority, trust boundary, recovery rule or scale boundary changes—not for every local refactor.

The project profile declares intended behavior; current receipts establish reality. Temporary exceptions use `schemas/TEMPORARY_OVERRIDE.md` and remain explicit, owned and expiring.

## 9. Dual-Lens engineering

Every material change is viewed through two lenses:

```text
LOCAL LENS
Is the changed behavior implemented correctly?

SYSTEM LENS
What truth does the whole system claim after this change?
```

The Local Lens covers code-path correctness, focused behavior, failure semantics, resource handling, regression checks, diff review and mutation-sensitive tests when load-bearing.

The System Lens uses these dimensions when relevant:

```text
WRITE · READ · AGGREGATE · CACHE · RESTART · FAILURE · RECOVERY
ADMIN · METRIC · TENANT_ISOLATION · SCALE · PRIVACY · COST
```

States are `UNAFFECTED | VERIFIED | CHANGED_AND_TESTED | OPEN_RISK | NOT_APPLICABLE`.

**Risk-adaptive rule:**

- `LOW` local-only work: short System-Lens impact summary; expand the matrix only when a dimension is plausibly affected.
- `MEDIUM/HIGH` material work: record the relevant matrix explicitly.
- any risk level touching money, privacy, identity, tenant isolation, durability/recovery, destructive state or production semantics: use the explicit affected dimensions regardless of nominal task size.

`OPEN_RISK` remains visible until resolved/accepted/deferred; it is never silently converted to `UNAFFECTED`.

## 10. Periodic cross-system audit

Task-local correctness does not guarantee system relationships stay healthy. Audit trigger priority is:

```text
EVENT TRIGGER
> RISK / AUTHORITY TRIGGER
> TASK-COUNT REMINDER
```

Run or consider a cross-system audit before real-customer release, after material incident, and around material authority/security/data/recovery changes. A configurable `5–8 material tasks` reminder is only a fallback—not a rule that overrides risk.

## 11. Architecture decision discipline

Architecture is not a library list. Freeze decisions that are load-bearing and expensive to change, such as data ownership, tenant/security boundaries, provenance/version/delete semantics, public contracts, recovery expectations, online/offline boundaries and evaluation contracts.

Keep cheap experiment variables open until evidence supports them.

For material hard-to-reverse choices, prefer a short architecture decision record:

```text
CONTEXT
DECISION
CONSEQUENCES
REVISIT TRIGGER
```

For AI/RAG systems, do not freeze vector vendor, chunk size, embedding model, top-k, reranker, prompt wording or agent framework merely from convention. Establish product/eval constraints first.

## 12. Task hierarchy and attention control

Every active work item is explicitly classified:

```text
PRIMARY_TASK   = current durable objective
SIDE_TASK      = bounded supporting work; cannot redefine the primary objective
INTERRUPT      = urgent preemption with explicit reason and resume target
```

There is one `PRIMARY_TASK` at a time. A side task may be useful or urgent, but it does not become primary because it is recent, difficult, or has consumed several prompts.

Normal rule:

```text
SIDE_TASK done
→ record result
→ return to PRIMARY_TASK
```

Promotion requires an explicit Manager/Operator decision. The agent raises `SIDE_TASK DRIFT` when a side task exceeds its focus budget, creates unrelated architecture or becomes the dominant optimization target.

For a true `INTERRUPT`, checkpoint the primary task first, preserve its exact resume state, execute only the urgent bounded work, then resume or explicitly reprioritize.

## 13. Risk and work kind are separate

```text
risk.level = LOW | MEDIUM | HIGH
work_kind  = IMPLEMENTATION | REMEDIATION | EVIDENCE_ONLY
```

Default workflow:

```text
LOW
execute → focused test → compact review → compact System-Lens summary

MEDIUM
short preflight → execute → Dual-Lens review → cold review
→ one bounded remediation → Manager review

HIGH
frozen contract
→ failure/System-Lens preflight
→ separate initial apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated review
→ one controlled remediation round by default
→ read-only Independent Judge when required
→ Operator production/business decision
```

A second remediation iteration is exceptional: it requires a new material finding, remains inside the configured maximum and cannot silently expand scope. Exceeding the bounded loop is itself a Swamp Guard signal.

## 14. Independent closure

A different model name is not enough to establish independence. Independent review should separate as many of these dimensions as risk requires:

```text
IMPLEMENTATION INDEPENDENCE
CONTEXT INDEPENDENCE
AUTHORITY INDEPENDENCE
EVIDENCE INDEPENDENCE
```

Model/provider diversity is useful defense-in-depth, but it is not an evidence-class upgrade by itself.

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

The Independent Judge is read-only by default. It may inspect source, exact diff, CI/receipts and authorized production telemetry, but it must not mutate product code, rewrite the task to manufacture a pass, or mutate production.

## 15. Artifact-driven handoff and session reset

Humans should not act as permanent message buses between agents. Durable handoff state should include current project mode/baseline, `PRIMARY_TASK`, active task role/ref, suspended/resume state, repository/base/head identity, review findings, remediation state, receipts/gaps, System-Lens open risks, Swamp Guard state, closure state and next authority decision.

A fresh session should be able to continue without replaying the previous conversation and without confusing the most recent side task with project priority.

## 16. Capability/cost routing

The framework does not prescribe model brands. Projects may route roles by capability and cost:

```text
Project Architect → stronger reasoning when architecture ambiguity justifies it
Executor          → task-adequate, cost-efficient model/harness
Manager           → stronger reasoning/review capability when justified
Independent Judge → high-reasoning, separate context
```

Cost routing must never lower the evidence or acceptance bar.

## 17. Production mutation invariant

Production mutation is a separate authority boundary. Before **every production change**, the active change record must identify:

```text
target environment
exact artifact/config/change identity
expected success + health signals
abort condition
rollback OR explicit forward-recovery path
stateful/data rollback constraints
recovery authority/owner
post-change verification
```

If rollback is unsafe or impossible, require forward recovery, backup/checkpoint strategy, blast-radius controls and STOP conditions.

```text
missing rollback/recovery readiness
→ NOT EXECUTION_READY_FOR_PRODUCTION_MUTATION
```

## 18. Canonical practical routes

- Greenfield/vibe/product inception: `docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md`
- System truth/data authority map: `schemas/SYSTEM_TRUTH_MAP.md` + `templates/SYSTEM_TRUTH_MAP.example.yaml`
- Project Architect prompt: `prompts/operator/PROJECT_ARCHITECT.md`
- Task lifecycle: `docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md`
- Mutation/remediation authority: `schemas/MUTATION_APPROVAL_POLICY.md`
- Project operating baseline/presets: `schemas/PROJECT_PROFILE_CONFIG.md`
- Role setup and permissions: `docs/operator/DESIGNER_MANAGER_SETUP.md`
- Independent Judge prompt: `prompts/operator/INDEPENDENT_JUDGE.md`
- Test environments: `production/AGENT_ENVIRONMENTS.md`
- Delivery/rollback: `production/DELIVERY.md`
- Verification semantics: `verification/00_INDEX.md`

Detailed rules belong in those triggered layers rather than being duplicated here.
