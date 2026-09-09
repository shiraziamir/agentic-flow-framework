---
name: evidence-integrity
description: Audit every closure claim against exact Definition-of-Done requirements and receipts.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# evidence-integrity

Use before material closure, especially with frozen batteries, benchmarks, acceptance gates, or claims like 'all tests pass'.

1. Enumerate exact DoD items.
2. Map each to current evidence.
3. Preserve counts: if M of N pass, report M/N and failures.
4. Check methodology identity and baseline comparability.
5. Label missing evidence INCOMPLETE, not inferred PASS.

## Mutation authority
READ ONLY.

## Output
`COMPLETE` or `INCOMPLETE` plus requirement-to-receipt matrix and missing evidence.

## Fail closed
No receipt means no verified claim.
