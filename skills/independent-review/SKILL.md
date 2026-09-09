---
name: independent-review
description: Perform a cold, read-only challenge of a task, diff, evidence packet, or closure claim.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# independent-review

Use when independence materially improves confidence.

With direct access:
- read frozen contract;
- inspect actual diff/source/tests;
- reproduce falsifying checks where practical;
- avoid editing reviewed artifacts.

Without direct access:
- consume `schemas/EVIDENCE_PACKET.md`;
- mark non-verifiable items `UNVERIFIED_FROM_PACKET`;
- request missing artifacts instead of guessing.

## Mutation authority
NONE. Reviewer must not repair the work it is judging in the same review pass.

## Output
`PASS|FAIL|INCONCLUSIVE`, findings, falsifying checks, missing evidence, recommended disposition.
