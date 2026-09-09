# Agentic Flow Architecture

**Status:** CANONICAL SOURCE OF TRUTH  
**Version:** 1.4  
**Updated:** 2026-09-09T08:22:00Z

This file defines the portable architecture. Vendor-specific files such as `CLAUDE.md`, `.claude/agents/*`, OpenCode agent definitions, `GEMINI.md`, or generated `AGENTS.md` variants are **adapters**, not policy authority.

## Source-of-truth hierarchy

When sources disagree, use this order:

1. `ARCHITECTURE.md` — lifecycle, authority, invariants.
2. `schemas/` — task/amendment/evidence/usage/history data contracts.
3. `skills/` — reusable procedures, loaded only when their trigger fires.
4. An approved/frozen task contract or approved amendment for the current task.
5. Durable evidence and supervisor decisions for that task.
6. Generated vendor adapters.
7. Conversation memory.

A generated adapter must never silently override layers 1–5.

## Core invariant

> Durable project memory; disposable, high-quality working context.

An agent session is replaceable. Project state must be reconstructible after a clear, crash, model change, provider change, or supervisor change.

## Risk-adaptive governance

The framework preserves safety boundaries without forcing high-assurance ceremony onto every change.

### HIGH — architecture / persistence / production semantics

Use when work materially affects architecture, durable data, security/trust boundaries, production semantics, cross-module public contracts, migrations, or other high-impact behavior.

```text
DRAFT TASK
→ SUPERVISOR REVIEW
→ FREEZE
→ SEPARATE APPLY AUTHORIZATION
→ BOUNDED EXECUTION
→ EVIDENCE PACKET
→ INDEPENDENT CLOSURE REVIEW
→ CHECKPOINT
```

### MEDIUM — bounded same-task correction

Use when new evidence requires a correction inside an existing task but does not justify restarting the whole lifecycle.

```text
OWNER-APPROVED AMENDMENT
→ bounded apply
→ required tests/evidence
→ independent closure
```

The amendment keeps the original task identity, records reason/scope/STOP conditions, and receives a durable version/hash. Escalate to HIGH if it grants materially new runtime authority or changes architecture/security/persistence/public contracts.

### EVIDENCE_ONLY — docs / test-contract / evidence correction

Use when the change corrects wording, freezes an evidence artifact/query set/matrix, or clarifies a test/evidence contract and **does not grant new runtime/mutation authority**.

```text
DURABLE OWNER-APPROVED AMENDMENT
→ hash/ref
→ evidence/doc update
→ closure check if material
```

A separate freeze/apply ceremony is unnecessary unless execution or mutation follows.

### Boundaries that never disappear

Regardless of governance level:

- source of truth stays explicit;
- frozen/approved artifacts have durable identity/hash/ref;
- executor does not self-certify material closure;
- implementation and closure judgment remain distinct when risk warrants independence;
- STOP occurs before scope creep or strategy mutation;
- Task N+1 is never silently absorbed;
- if required evidence does not exist, the agent must not invent a plausible substitute;
- high-risk scope cannot be downgraded merely to save tokens or time.

## Roles are not models

- `ORCHESTRATOR` — routes work, curates context, maintains lifecycle state.
- `CHEAP_READONLY` — bounded discovery/inventory/log reduction with no mutation authority by default.
- `EXECUTION_TIER` — bounded implementation and evidence gathering.
- `JUDGMENT_TIER` — architecture, ambiguity, safety, policy, high-risk closure judgment.
- `INDEPENDENT_REVIEWER` — cold/read-only challenge of claims and evidence.
- `HUMAN_OWNER` — authority that cannot be delegated by a skill or model.

Concrete models are configured separately. A stronger model has greater capability, not automatic truth or authority.

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

Escalation transfers a compact evidence packet, not a transcript. A cheaper model may gather evidence; it may not weaken Definition of Done, tests, security boundaries, or review requirements. Route changes that claim savings at equal quality should be benchmarked with frozen fixtures.

## Context and token-efficiency policy

Context is working memory, not archive storage. Optimize **signal-to-context ratio**, not token count alone.

For modular repositories define `EDIT_SET`, `REFERENCE_SET`, `EXCLUDED_SET`, and `CHECK_SET`. Expand only when dependency evidence requires it. Use child/subagent contexts as firebreaks for high-volume read-only work and return conclusions, file paths, receipts, unresolved facts, and next action rather than transcripts.

### Waste controls

Prefer, in order:

1. deterministic/mechanical discovery before LLM discovery;
2. bounded dependency/affected graphs before whole-repo scans;
3. lazy skill/tool loading instead of preloading large shelves/toolsets;
4. filtered log slices plus raw-artifact refs instead of huge tool results in context;
5. batched/programmatic tool calls when intermediate roundtrips add no reasoning value;
6. cheap read-only workers for bounded discovery that can be verified;
7. semantic context reset after durable checkpoint;
8. provider caching for stable prefixes when available, while remembering caching does not necessarily reduce context occupancy.

When provider/harness usage data is observable, record it using `schemas/USAGE_EVENT.md`. Missing telemetry is `UNKNOWN`, never zero.

### Token/cost budget

Material tasks may declare soft/hard token or cost budgets, expected model tiers, and warning conditions. Budgets are observability/steering controls—not permission to lower quality.

On material waste or budget overrun, emit `TOKEN_WASTE_WARNING` with evidence and a quality-preserving alternative. Hard-budget breach or any proposed quality tradeoff requires operator/judgment approval.

## Skill policy

Skills are cold procedures, not permanent prompt text. Default task packet: **0–3 load-bearing skills**. A fourth should be exceptional and justified by a distinct trigger.

Skill classes:

- `CORE` — general, high-value, expected to recur.
- `COMMON` — useful for a broad task family.
- `RISK_TRIGGERED` — intentionally rare; load only when its risk exists.
- `EXPERIMENTAL` — not promoted until evidence justifies it.

Low activation count is not evidence a risk-triggered skill is useless. Promotion/retirement considers eligible-trigger denominator, activation quality, evidence level, rework/regressions, and controlled comparisons when causal claims matter.

## Supervisor architecture

### Supervisor with direct repository/tool access

Preferred for high assurance. The supervisor independently reads the frozen contract/amendment, actual diff/source/tests, re-runs or spot-checks falsifying tests where practical, checks the evidence packet against source, remains read-only during review, and returns a structured judgment. Use a separate context/session/model from the executor when independence matters.

### Supervisor without repository/tool access

The executor/orchestrator supplies a bounded evidence packet containing immutable task/contract identity, repository/ref/commit identity, changed paths, diff/patch artifact, commands and results, failing/passing checks, live receipts where required, unresolved facts, residual risk, and exact claims submitted for judgment.

The supervisor labels anything it cannot independently verify as `UNVERIFIED_FROM_PACKET`, may request missing evidence, and never converts missing access into confident approval.

### Expensive judgment must be durable but cold

If a stronger/more expensive model is used for review or architecture judgment, persist its **decision artifact**: decision, claim findings, evidence refs, required amendment/follow-up, validity boundary, model/provider if observable, timestamp/version. Do not persist its chain-of-thought or force future tasks to reread every historical judgment.

Normal tasks consult the current checkpoint/index and only open historical judgments when a decision dependency or explicit history request exists.

## Amendment discipline

A frozen HIGH task changes only through explicit amendment. MEDIUM and EVIDENCE_ONLY amendments use `schemas/AMENDMENT.md` and preserve original task identity. If execution disproves scope, strategy, or prerequisites:

```text
STOP
→ record new evidence
→ classify amendment risk
→ owner/supervisor decision
→ amend at the minimum sufficient governance level
→ re-authorize APPLY only when required
```

Execution retry is allowed within frozen strategy. Silent strategy retry or scope expansion is not.

## Closure

Closure is a claim about evidence, not effort. Map every Definition-of-Done item to a receipt. If N required checks exist and M pass, report `M/N` and the failing items. A simpler test cannot silently replace a frozen acceptance gate.

Repeated status/receipt fields should have one authoritative artifact and be referenced rather than copied into every phase.

## Hot state vs cold history

Daily agent context must stay small.

### Hot state

- canonical architecture/map;
- current task/amendment;
- current checkpoint;
- directly relevant module/docs/skills;
- current budget state and unresolved decisions.

### Cold history

- completed task summaries;
- historical evidence packets;
- supervisor judgments;
- architecture decision history;
- usage/token/cost ledger;
- append-only execution retrospective ledger;
- generated retrospectives and project stories/case studies.

Cold history is indexed and versioned but loaded only on explicit trigger: decision provenance, regression investigation, audit, retrospective, project storytelling, or user request.

## Execution retrospective / work reconstruction

For long campaigns, rescues, migrations, or other work whose execution history itself has engineering value, maintain a compact **cold append-only execution ledger** using `schemas/EXECUTION_RETROSPECTIVE_LEDGER.md`.

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

Each entry points to Git/task/judgment/evidence/usage artifacts instead of copying them. This makes later reconstruction cheap without turning history into permanent context.

A formal retrospective is an on-demand deliverable produced by `project-retrospective`. It reconstructs, where evidence permits:

- timeline and reliable logging boundary;
- tasks closed and amendment loops;
- STOP conditions that prevented real mistakes;
- independent judgments/reviews;
- implementation versus evidence/governance commits;
- tests added and suite-count evolution where derivable;
- pre-closure defects and false-complete states caught;
- provider calls, test-environment and production mutations;
- deferred findings and intentionally blocked scope creep;
- approximate duration/iterations only when timestamps/receipts support them;
- governance value versus ceremony;
- evolution of the engineering process;
- what should change next time.

Every material historical fact is classified as one of:

```text
PROVEN FROM GIT / DURABLE ARTIFACTS
RECONSTRUCTED FROM OWNER JOURNAL / RECEIPTS
UNKNOWN / NOT LOGGED RELIABLY
```

Unknown history stays unknown. Never backfill exact counts merely to make the retrospective complete.

## Project history, storytelling and self-branding

Execution reconstruction and storytelling are separate layers. `project-retrospective` produces the audit-grade timeline/metrics/truth classes. `project-storytelling` turns verified/reconstructed evidence into project history, architecture evolution, incidents, engineering advantages, case studies and self-branding material.

When a retrospective already exists, storytelling should consume its bounded outputs and source refs rather than rereading the entire cold history. Generated stories are reader artifacts, not standing agent instructions.

## Documentation versioning and freshness

Canonical project/framework documents must expose a version and update timestamp/date. Material verified changes trigger a documentation-freshness check. Update the authoritative document first, then regenerate projections/adapters.

Use indexes to keep old history discoverable without making it always-on context. Obsolete documents should be superseded/archived rather than ambiguously active.

## Generated adapters

`prompts/bootstrap/` contains prompts for creating/updating vendor adapters. Adapters MUST point back to this file, stay concise, preserve vendor-neutral authority, expose skills lazily, encode only vendor-specific mechanics, avoid copying the canonical architecture, identify the canonical version they were generated from, and remain regenerable.

## Validation principle

Prefer deterministic enforcement for deterministic rules: scripts, hooks, CI, schemas, permissions, linters. Do not spend model judgment on conditions a program can check exactly.

## Evidence before policy promotion

A method/model/skill becomes default because evidence supports it, not because it sounds elegant. Use frozen fixtures and controlled comparisons when claiming a route or skill improves quality/cost.
