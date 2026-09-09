---
name: diagnose-before-fix
description: Prove the failing layer/root cause with the cheapest discriminating test before editing.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# diagnose-before-fix

Use when cause or earliest failing stage is not proven.

Flow: reproduce → hypotheses → cheapest discriminating test → identify layer → bounded fix only if supported → verify.

Distinguish correlation from cause. Prefer a test that makes competing hypotheses produce different outcomes.

## Mutation authority
No fix until evidence supports a layer/cause, except explicitly authorized stopgaps.

## Output
Reproduction receipt, hypotheses, discriminating test, supported diagnosis, bounded next action.

## Fail closed
If competing high-impact roots remain, escalate to judgment.
