# Project Inception & Architecture Discovery

**Agent-facing canonical lifecycle for greenfield / early-stage projects.**

Use this before ordinary task execution when the project does not yet have a trustworthy architecture baseline, or when the operator only knows the product outcome and wants agents to discover the system shape.

## Goal

Do not jump directly from product idea to implementation.

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ 2–3 MINIMAL OPTIONS
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ REAL EVALUATION
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
→ NORMAL TASK FLOW
```

The Product Owner owns **WHY / WHAT / business trade-offs**. The Project Architect owns **system-shape discovery**. The Executor owns **implementation** inside the approved architecture boundaries.

## 1. Project development mode

Projects should declare one of:

```text
VIBE_PROTOTYPE
PRODUCT_BUILD
MAINTENANCE
```

### VIBE_PROTOTYPE

Use when the primary question is whether an idea, interaction, provider or technical capability is worth pursuing.

Default properties:

- optimize for learning speed;
- architecture may be provisional;
- limited, non-sensitive test data by default;
- no claim of production readiness;
- no silent promotion to production baseline;
- code may be intentionally sacrificial;
- decisions still worth preserving are recorded compactly.

```text
VIBE_PROTOTYPE
!=
PRODUCTION BASELINE
```

A prototype may later contribute code to the product, but reuse is a decision—not an assumption.

### PRODUCT_BUILD

Use when the objective is a maintainable product rather than a disposable experiment.

Before entering PRODUCT_BUILD, establish:

- product brief;
- evaluation / quality contract;
- security/data boundaries;
- System Truth / Data Authority Map;
- current scale boundary and safety limits;
- hard-to-change invariants;
- selected architecture option and decision rationale;
- a walking skeleton that exercises the critical path;
- architecture fitness functions where practical;
- execution/test environment;
- operational/recovery expectations appropriate to the product.

### MAINTENANCE

Use when a trustworthy baseline already exists. Route work through the normal task workflow and reopen architecture discovery only when a material architectural boundary is changing or the Swamp Guard requires re-baselining.

## 2. Product brief before technology

Do not ask the Product Owner to choose libraries or infrastructure they do not need to own.

Translate intent into product constraints such as:

```text
Who are the users?
What job are they trying to complete?
What does a good result look like?
What result is unacceptable?
What data is private or tenant-scoped?
What freshness is required?
What latency/cost range is acceptable?
What happens when the system does not know?
What must be auditable/explainable?
What scale is plausible now vs later?
```

Technology comes after these constraints.

## 3. Quality / evaluation contract

For AI/RAG/search/recommendation systems, define what “good” means before tuning implementation details.

Examples:

```text
retrieval relevance / recall target
citation correctness
groundedness / unsupported-claim rate
cross-tenant leakage = 0
freshness/update/delete behavior
latency budget
cost budget
safe no-answer behavior
```

Create a small representative evaluation set early. Do not optimize chunk size, retrieval strategy, prompts, rerankers or model choice solely on demo impressions.

For conventional software, the equivalent is observable acceptance tests and architecture fitness functions for load-bearing properties.

## 4. Build the System Truth Map before broad coding

Create a compact system/data map using `schemas/SYSTEM_TRUTH_MAP.md`.

### Component map

Identify when applicable:

```text
ENTRY POINTS
TRUST BOUNDARIES
DATABASES
CACHES
QUEUES
EXTERNAL PROVIDERS
BACKGROUND WORKERS
ADMIN OPERATIONS
METRICS / ALERTS
DEPLOYMENT / ROLLBACK / RECOVERY
```

### Data authority map

For each load-bearing datum, record:

```text
name
authoritative source
derived/cached copies
writer(s)
reader(s)
TTL/freshness
maximum size/bound
privacy class
restart behavior
failure behavior
recovery procedure
tenant-isolation mechanism
```

Examples of load-bearing data include spend/accounting, entitlement, identity, tenant ownership, durable attempts, customer state and recovery checkpoints.

A cache/projection/summary/metric is not automatically authoritative. If authority is unavailable, define whether the system blocks, degrades, becomes unavailable, or uses an explicitly approved stale fallback. Do not invent a safe-looking substitute such as zero or empty success.

## 5. Small threat/failure review

Do not create a hundred-page document. Perform a compact adversarial review of the proposed system:

```text
What can leak?
What can be counted twice?
What can be silently lost?
What survives restart?
What becomes stale?
What can grow without a bound?
What happens under concurrency?
What happens when a dependency lies or partially fails?
What can one tenant do to another?
What can cause unexpected provider spend?
What can an administrator safely do later?
```

Record material risks/decisions and translate them into requirements, STOP conditions, tests or architecture boundaries.

## 6. Define the current scale boundary

Do not over-engineer for hypothetical scale, but do not hide the current ceiling.

For important resources record:

```text
expected load
known ceiling or UNKNOWN
soft warning
hard safety limit when unbounded growth could be dangerous
failure behavior
scale-up trigger
```

Example:

```text
Current target: controlled demo / early tenants
Not claimed: 10,000 concurrent users
Required now: bounded memory, bounded queues, bounded retries
Deferred: distributed coordination / multi-region failover
```

## 7. Architecture discovery

The Project Architect works read-only / design-only first and presents 2–3 **minimal viable architecture options** when meaningful alternatives exist.

For each option report:

```text
system boundaries
main data/control flow
hard-to-change decisions
operational burden
security/data implications
cost shape
vendor lock-in
reversibility
scaling limit
main failure modes
what evidence could invalidate this option
```

Prefer the simplest architecture that satisfies current product constraints.

Do not choose a framework, datastore, vector database, queue, agent framework or abstraction merely because it is popular or familiar.

## 8. Freeze invariants, not easy implementation choices

Freeze early when a decision is load-bearing and expensive to change, for example:

```text
data ownership / tenant boundary
authorization position
identity/version/delete semantics
source provenance
public contract
recovery expectations
online vs offline/ingestion boundary
evaluation contract
observability contract
security/privacy invariants
```

Keep easy-to-change experiment variables open until evidence supports them, for example:

```text
specific library/framework
chunk size / overlap
embedding/model choice
top-k
reranker
prompt wording
managed vs custom implementation detail
internal class structure
```

Canonical rule:

```text
FREEZE HARD-TO-CHANGE INVARIANTS
NOT EASY-TO-CHANGE IMPLEMENTATION CHOICES
```

## 9. Walking skeleton

Before broad feature development, build the smallest end-to-end path that crosses the real architecture boundaries.

For a RAG product this might be:

```text
one real document
→ ingest / normalize
→ identity + metadata
→ index
→ authorized query
→ retrieval
→ generation
→ citation
→ evaluation
```

The walking skeleton is not a polished MVP. Its job is to falsify architecture assumptions early.

After it runs, perform an **ARCHITECTURE CHECKPOINT**:

```text
Did data lifecycle assumptions hold?
Can authorization be enforced where planned?
Can updates/deletes/versioning work?
Can the critical path be observed and tested?
Can the selected storage/provider be replaced if needed?
Can evaluation locate failure instead of just report “bad answer”?
Are latency/cost remotely compatible with the product constraint?
Does the System Truth Map still match the implemented walking skeleton?
```

If not, change architecture now while the system is still small.

## 10. Architecture decision records

Record only important, hard-to-reverse decisions. Keep ADRs short:

```text
CONTEXT
DECISION
CONSEQUENCES
REVISIT TRIGGER
```

Avoid documenting every local implementation choice as architecture.

## 11. Swamp Guard — continuous anti-bog check

The agent/Manager MUST evaluate the Swamp Guard at material checkpoints:

```text
before first product mutation
before a new major dependency/provider/datastore/framework
before changing an architecture boundary
after a material review/remediation round
before broad feature expansion
before VIBE_PROTOTYPE → PRODUCT_BUILD
before staging/production promotion
```

Possible states:

```text
CLEAR
WATCH
ALERT
STOP_REBASELINE
```

### Early warning signals

Raise `WATCH` or `ALERT` when one or more are observed:

- repeated architecture churn in the same subsystem;
- repeated remediation/rewrite of the same behavior;
- new abstractions without a concrete boundary/failure mode;
- multiple tools/frameworks/datastores competing for the same responsibility;
- tuning before an evaluation baseline exists;
- feature growth before a working vertical slice exists;
- architecture decisions living only in chat;
- duplicate sources of truth/state ownership;
- expanding scope without updating product/architecture assumptions;
- tests increasingly proving proxies rather than user-visible behavior;
- growing operational complexity without a product constraint that justifies it;
- repeated “temporary” exceptions becoming permanent structure;
- a prototype accumulating production expectations without re-baselining;
- the System Truth Map cannot identify authority/recovery for a new load-bearing state.

### Hard-stop / re-baseline signals

Use `STOP_REBASELINE` when continuing would compound structural debt, including:

- promoting `VIBE_PROTOTYPE` to staging/production without product/architecture re-baseline;
- sensitive/tenant data with unresolved authorization or ownership boundary;
- a material architecture boundary changed without updated decision/evidence;
- remediation exceeds configured limits without a new bounded explanation;
- a third major technology is introduced for a responsibility already served by two competing mechanisms without explicit architecture decision;
- AI/RAG quality is being optimized with no representative eval set or measurable quality contract;
- the current walking skeleton cannot exercise the critical product path and feature work continues anyway;
- source-of-truth ambiguity is causing repeated defects.

### Alert format

Keep alerts short and actionable:

```text
SWAMP ALERT: <WATCH|ALERT|STOP_REBASELINE>
Signal: <what is happening>
Evidence: <repo/task refs>
Why it matters: <likely compounding cost>
Recommended action: <simplify / measure / ADR / vertical slice / re-baseline>
Continue allowed: YES|NO
Authority needed: <none|Manager|Operator>
```

The objective is not to stop experimentation. It is to stop **unmeasured complexity or system-truth ambiguity from becoming architecture by accident**.

## 12. Vibe-to-product transition gate

Never transition by merely renaming the prototype “production”.

```text
VIBE_PROTOTYPE
→ preserve useful learnings/evals
→ product brief
→ architecture discovery
→ system truth / data authority map
→ security/data boundaries
→ choose what prototype code is reusable vs disposable
→ walking skeleton on intended product baseline
→ architecture checkpoint
→ PRODUCT_BUILD
```

At this gate, explicitly classify prototype code:

```text
REUSE_AS_IS
REUSE_AFTER_REVIEW
REWRITE
DISCARD
```

Unknown code does not default to `REUSE_AS_IS`.

## 13. Relationship to the normal task flow

Project inception chooses and validates the project baseline. It does not replace task governance.

Once `PRODUCT_BUILD` baseline is accepted:

```text
Project Inception / Architecture Discovery
→ PROJECT BASELINE + SYSTEM TRUTH MAP
→ docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

If the Swamp Guard later detects structural drift, temporarily return to architecture discovery rather than solving every architecture problem as a sequence of local task patches.

## 14. RAG-specific minimum checklist

Before serious RAG implementation, establish at least:

```text
user / tenant model
document identity and source provenance
version/update/delete semantics
authorization filtering point
ingestion vs online-query boundary
no-answer behavior
citation contract
representative eval set
retrieval and groundedness measures
latency/cost target
observability of retrieval vs generation failure
System Truth Map for documents, indexes/caches, spend and tenant boundaries
current scale target / safety bounds
```

Do **not** freeze vendor, vector database, chunk size, embedding model, top-k, reranker or agent framework until product constraints/evals justify them.

## 15. Research basis

This lifecycle follows the same broad direction found in agent-first, threat-modeling and evolutionary-architecture practice: establish enforceable architectural boundaries early, map trust/data authority, keep implementation simple, use executable evaluation/fitness functions, make hard-to-reverse decisions explicit, and validate architecture through short feedback loops rather than large speculative design documents. See `docs/references/PRIMARY_SOURCES.md` for provenance.