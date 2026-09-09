---
name: documentation-freshness
description: Keep canonical architecture, task summaries, decision indexes, and user-facing docs versioned, timestamped, cross-linked, and consistent with verified project state.
---
# Documentation Freshness

**Class:** COMMON  
**Updated:** 2026-09-09

## USE WHEN
- a verified material change alters architecture, capabilities, limitations, task workflow, or operating assumptions;
- closing a medium/high-risk task;
- a doc/index freshness check is explicitly requested;
- a bootstrap adapter may be stale relative to canonical policy.

## RULES
1. Every canonical document carries a visible version and `Updated` date.
2. Update the authoritative home first; regenerate/synchronize projections afterward.
3. Do not duplicate long task histories into hot docs. Link to durable summaries/indexes.
4. Record **what changed and why**, not raw deliberation.
5. If code/evidence and docs conflict, docs are stale until reconciled; never rewrite evidence to fit prose.
6. Completed task details remain cold; update only compact project/architecture indexes needed for discovery.
7. Generated vendor adapters must identify the canonical version they were generated from.

## CLOSURE CHECK
Before closure of material work, verify:
- architecture docs affected by the change are current;
- task/amendment/evidence/judgment artifacts have timestamps and versions/IDs;
- current checkpoint/index points to the latest authoritative artifacts;
- obsolete docs are superseded/archived rather than left ambiguously active;
- user-facing README/quick-start remains accurate if workflow changed.

## OUTPUT
`DOC_FRESHNESS: CURRENT|STALE|NOT_APPLICABLE` plus changed/stale paths and evidence refs.
