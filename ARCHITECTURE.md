# Agentic Flow Architecture

**Status:** CANONICAL SOURCE OF TRUTH  
**Version:** 1.2  
**Updated:** 2026-09-09

This file defines the portable architecture. Vendor-specific files such as `CLAUDE.md`, `.claude/agents/*`, OpenCode agent definitions, `GEMINI.md`, or generated `AGENTS.md` variants are **adapters**, not policy authority.

## Source-of-truth hierarchy

When sources disagree, use this order:

1. `ARCHITECTURE.md` — lifecycle, authority, invariants.
2. `schemas/` — task/evidence data contracts.
3. `skills/` — reusable procedures, loaded only when their trigger fires.
4. An approved/frozen task contract for the current task.
5. Durable evidence and supervisor decisions for that task.
6. Generated vendor adapters.
7. Conversation memory.

A generated adapter must never silently override layers 1–5.

## Core invariant

> Durable project memory; disposable, high-quality working context.

An agent session is replaceable. Project state must be reconstructible after a clear, crash, model change, provider change, or supervisor change.

## Lifecycle

```text
REQUEST
  ↓
DRAFT TASK CONTRACT
  ↓
SUPERVISOR REVIEW
  ├─ ACCEPT_DRAFT
  ├─ AMEND_DRAFT
  └─ REJECT / NEEDS_EVIDENCE
  ↓
FREEZE CONTRACT
  ↓
APPLY AUTHORIZATION
  ↓
BOUNDED EXECUTION
  ↓
EVIDENCE PACKET
  ↓
SUPERVISOR CLOSURE REVIEW
  ├─ ACCEPT_CLOSURE
  ├─ AMEND_SAME_TASK
  ├─ CREATE_BOUNDED_FOLLOWUP
  └─ NO_SAFE_PATH
  ↓
DURABLE CHECKPOINT
  ↓
SAFE CONTEXT RESET
```

Low-risk projects may combine gates, but must not erase the distinction between **authoring**, **authorization**, **execution**, **evidence**, and **judgment**.

## Roles are not models

- `ORCHESTRATOR` — routes work, curates context, maintains lifecycle state.
- `EXECUTION_TIER` — bounded implementation and evidence gathering.
- `JUDGMENT_TIER` — architecture, ambiguity, safety, policy, closure judgment.
- `INDEPENDENT_REVIEWER` — cold/read-only challenge of claims and evidence.
- `HUMAN_OWNER` — authority that cannot be delegated by a skill or model.

Concrete models are configured separately. A stronger model has greater capability, not automatic truth or authority.

## Model routing

Use the cheapest reliable tier for a bounded task.

```text
T0 DETERMINISTIC
  graph queries, grep/AST, lint, formatting, schema checks, test selection

T1 CHEAP_READONLY
  discovery, inventory, log reduction, repetitive classification

T2 STANDARD_EXECUTION
  localized implementation, tests, module-scoped refactors

T3 JUDGMENT
  architecture, ambiguous root cause, security, public-contract changes,
  repeated failed loops, acceptance of known failures, high-risk closure
```

Escalation transfers a compact evidence packet, not a transcript.

## Context policy

Always-on context should be a map, not a manual. For modular repositories define `EDIT_SET`, `REFERENCE_SET`, `EXCLUDED_SET`, and `CHECK_SET`. Expand only when dependency evidence requires it. Use child/subagent contexts as context firebreaks for high-volume read-only work; return conclusions, file paths, receipts, unresolved facts, and the next action rather than full transcripts.

## Skill policy

Skills are cold procedures, not permanent prompt text. Default task packet: **0–3 load-bearing skills**. A fourth should be exceptional and justified by a distinct trigger.

Skill classes:

- `CORE` — general, high-value, expected to recur.
- `COMMON` — useful for a broad task family.
- `RISK_TRIGGERED` — intentionally rare; load only when its risk exists.
- `EXPERIMENTAL` — not promoted until evidence justifies it.

Low activation count is not evidence a risk-triggered skill is useless. Every skill declares trigger, non-trigger, mutation authority, evidence requirement, fail-closed behavior, and output contract.

## Supervisor architecture

### Supervisor with direct repository/tool access

Preferred for high assurance. The supervisor independently reads the frozen contract, actual diff/source/tests, re-runs or spot-checks falsifying tests where practical, checks the evidence packet against source, remains read-only during review, and returns a structured judgment. Use a separate context/session/model from the executor when independence matters.

### Supervisor without repository/tool access

The executor/orchestrator supplies a bounded evidence packet containing immutable task/contract identity, repository/ref/commit identity, changed paths, diff/patch artifact, commands and results, failing/passing checks, live receipts where required, unresolved facts, residual risk, and exact claims submitted for judgment.

The supervisor labels anything it cannot independently verify as `UNVERIFIED_FROM_PACKET`, may request missing evidence, and never converts missing access into confident approval.

## Draft/freeze/apply discipline

Drafting does not grant execution authority. A frozen contract changes only through explicit amendment. If execution disproves scope, strategy, or prerequisites:

```text
STOP
→ record new evidence
→ request amendment/judgment
→ freeze amended contract
→ re-authorize APPLY if required
```

Execution retry is allowed within frozen strategy. Silent strategy retry or scope expansion is not.

## Closure

Closure is a claim about evidence, not effort. Map every Definition-of-Done item to a receipt. If N required checks exist and M pass, report `M/N` and the failing items. A simpler test cannot silently replace a frozen acceptance gate.

## Generated adapters

`prompts/bootstrap/` contains prompts for creating/updating vendor adapters. Adapters MUST point back to this file, stay concise, preserve vendor-neutral authority, expose skills lazily, encode only vendor-specific mechanics, avoid copying the canonical architecture, and remain regenerable.

## Validation principle

Prefer deterministic enforcement for deterministic rules: scripts, hooks, CI, schemas, permissions, linters. Do not spend model judgment on conditions a program can check exactly.

## Evidence before policy promotion

A method/model/skill becomes default because evidence supports it, not because it sounds elegant. Use frozen fixtures and controlled comparisons when claiming a route or skill improves quality/cost.
