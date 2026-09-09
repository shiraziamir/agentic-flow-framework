# Research note — execution retrospective and cold reconstruction

**Research-note version:** 1.0  
**Updated:** 2026-09-09T08:22:00Z  
**Status:** evidence/research, not policy authority

## Trigger

The Yara task-management review proposed making the end-of-rescue deliverable an **Execution Retrospective / Work Reconstruction Report**, backed by Git, receipts, judgments, tests, commits and owner journal rather than a conventional narrative summary.

The proposal also recommended recording compact boundary entries during the remaining campaign so final reconstruction would not require excavating the entire history from scratch.

## Framework interpretation

This aligns with the framework's hot-state/cold-history design if the ledger is deliberately small and non-authoritative:

- normal tasks do not read it;
- it records only meaningful lifecycle boundaries;
- it points to canonical task/evidence/judgment/Git artifacts rather than duplicating them;
- final audit reconstruction is separate from reader-facing storytelling;
- early incomplete history remains explicitly incomplete.

## Primary-source support

### OpenAI — repository-local plans and progressive disclosure

OpenAI's Harness Engineering report describes an agent-first repository in which:

- a short `AGENTS.md` acts as a map rather than an encyclopedia;
- structured `docs/` are treated as system of record;
- execution plans are first-class versioned artifacts;
- active plans, completed plans and decision logs are co-located;
- progressive disclosure keeps agents from being overwhelmed by irrelevant history;
- documentation freshness is mechanically checked/gardened.

Source:
- https://openai.com/index/harness-engineering/

This supports keeping durable execution history in the repository while keeping ordinary context bounded.

### Anthropic — context pressure and usage visibility

Anthropic's current tool-context guidance explicitly identifies accumulated tool results and large tool definitions as context pressure, and recommends lazy tool search, programmatic/batched tool calls, prompt caching and context editing depending on the source of bloat.

Its Usage and Cost API exposes organization-level usage counters including uncached input, cache creation/read and output tokens when using supported API workflows.

Sources:
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
- https://platform.claude.com/docs/en/manage-claude/usage-cost-api

This supports recording compact usage references/counters separately from narrative history instead of preserving full agent transcripts.

## Design decision

Add three separate layers:

1. **Execution ledger** — append-only compact boundary facts, cold by default.
2. **Project retrospective** — audit-grade reconstruction with truth classes and metrics.
3. **Project storytelling** — reader-facing case study/self-branding narrative built from bounded verified/reconstructed evidence.

Do not merge these into a single always-on history file.

## Truth classes

The retrospective must distinguish:

```text
PROVEN FROM GIT / DURABLE ARTIFACTS
RECONSTRUCTED FROM OWNER JOURNAL / RECEIPTS
UNKNOWN / NOT LOGGED RELIABLY
```

A missing historical denominator or timestamp is not an invitation to estimate an exact number.

## Governance-overhead analysis

The retrospective should measure not only output but process value:

- STOPs that prevented implementation against false prerequisites;
- independent reviews that caught pre-closure gaps;
- false-complete states prevented;
- amendment loops;
- implementation versus governance/evidence commits;
- repeated receipt/status duplication;
- where HIGH governance was justified;
- where MEDIUM/EVIDENCE_ONLY would have preserved the same safety with less ceremony.

This turns governance refinement into an evidence-based feedback loop rather than a subjective preference.
