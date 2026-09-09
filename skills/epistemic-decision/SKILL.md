---
name: epistemic-decision
description: Make consequential decisions under uncertainty with explicit evidence, assumptions, unknowns, and error costs.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# epistemic-decision

Use when a consequential technical decision remains uncertain after evidence gathering.

State:
- what is KNOWN;
- what is INFERRED;
- what is UNKNOWN;
- assumptions;
- options;
- cost of false-positive vs false-negative decisions;
- cheapest additional evidence that could change the choice;
- validity boundary of the recommendation.

## Mutation authority
None by itself. High-impact disputed choices belong to JUDGMENT_TIER/HUMAN_OWNER.

## Output
Decision packet with evidence, uncertainty, error costs, recommendation, and stop/escalation conditions.
