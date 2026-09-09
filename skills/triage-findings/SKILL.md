---
name: triage-findings
description: Classify multiple findings before allowing them to expand a task's scope.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# triage-findings

Use when 2+ findings appear or feedback is noisy.

For each finding classify:
- `IN_SCOPE_NECESSITY`
- `OUT_OF_SCOPE_BLOCKER`
- `OPTIONAL_FOLLOWUP`

Also identify shared root vs independent roots, dependency order, and whether judgment is required.

## Mutation authority
NONE during triage.

## Output
Finding cards + proposed order + explicit stop/review point.
