# Agentic Flow Framework — English Reader Guide

**Reader-guide version:** 1.3  
**Updated:** 2026-09-09  
**Canonical source of truth:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

This document is a synchronized reader-facing guide. If it conflicts with `ARCHITECTURE.md`, the architecture file wins.

## Core idea

> Durable project memory; disposable, high-quality working context.

The framework separates project memory from agent working memory. Tasks, evidence, decisions, architecture changes, usage telemetry and project history remain durable; ordinary agent runs load only the current working set and pointers they actually need.

## Risk-adaptive task governance

### HIGH
Architecture, persistence, production/security/trust, durable data, or material public-contract work:

```text
DRAFT → SUPERVISOR → FREEZE → SEPARATE APPLY → EXECUTE → EVIDENCE → INDEPENDENT CLOSURE
```

### MEDIUM
Bounded correction inside an existing task:

```text
OWNER-APPROVED AMENDMENT → BOUNDED APPLY → TESTS/EVIDENCE → INDEPENDENT CLOSURE
```

### EVIDENCE_ONLY
Docs, evidence or test-contract correction that grants no new runtime authority:

```text
DURABLE APPROVED AMENDMENT + HASH/REF → UPDATE → CLOSURE CHECK IF MATERIAL
```

Source-of-truth, durable identity, STOP-before-scope-creep, no self-certification, no Task N+1 absorption, and “do not invent missing evidence” remain invariant at every level.

## Model and token efficiency

Semantic routing:

```text
T0 deterministic/mechanical
T1 cheap read-only discovery/partition
T2 standard bounded execution
T3 judgment/high-risk review
```

Use the cheapest reliable tier whose output can meet the same acceptance bar. Cheap workers may gather evidence; they do not reduce DoD, tests, security or review requirements.

For long/cost-sensitive work use `skills/token-efficiency/SKILL.md`. The agent should warn on unjustified whole-repo scans, repeated rereads, full-history loading, huge raw logs, strong models doing mechanical work, overlapping subagents, repeated failed loops, or budget overruns.

When the provider/harness exposes usage, record privacy-safe counters in `.agentic/usage/events.jsonl` using `schemas/USAGE_EVENT.md` and `scripts/usage_ledger.py`. Missing telemetry is unknown, not zero.

Prompt caching is a cost/latency optimization, not automatic context compression. Prefer small working sets, lazy tool/skill discovery, batched tool operations, filtered log artifacts, compact subagent handoffs and semantic resets.

## Hot state and cold history

Hot state for ordinary work:

- current task/amendment;
- current checkpoint/index;
- current budget/unresolved decisions;
- relevant modules/docs/skills only.

Cold history:

- completed tasks;
- supervisor judgments;
- evidence packets;
- architecture decisions;
- token/cost ledger;
- project timeline and generated stories.

Cold history is opened only for provenance, audit, regression analysis, retrospective or explicit user request.

## Supervisors

A supervisor may be a human, a separate model, or a cold independent session.

- **Direct-access supervisor:** inspects real source/diff/tests/evidence and remains read-only during review.
- **Evidence-only supervisor:** reviews a bounded evidence packet and marks inaccessible claims `UNVERIFIED_FROM_PACKET`.

If an expensive model performs judgment, preserve the compact decision artifact with timestamp/version/evidence refs—not its chain-of-thought or full transcript.

## Skills

Skills are on-demand procedures. The router default is 0–3 load-bearing skills, not the whole shelf. Broad skills may activate frequently; risk-triggered skills are expected to be rare.

See `skills/00_INDEX.md`. New v1.3 skills include:

- `token-efficiency`
- `documentation-freshness`
- `project-storytelling`

## Project storytelling and self-branding

`project-storytelling` is explicitly cold/on-demand. When requested, it reconstructs project history, architecture evolution, engineering decisions, incidents, measurable advantages and portfolio/self-branding material from compact indexes first, opening raw artifacts only when a claim needs deeper verification.

Generated stories remain reader artifacts, not coding-agent standing context.

## Documentation freshness

Canonical and index documents carry versions and update dates. Material verified changes trigger `documentation-freshness`: update the authoritative source first, then synchronize reader guides and generated vendor adapters.

## Start here

1. `README.md`
2. `ARCHITECTURE.md`
3. matching bootstrap prompt under `prompts/bootstrap/`
4. current task/amendment and only the skills it triggers

Research evidence lives under `research/` and is dated; it informs policy but does not override the canonical architecture.
