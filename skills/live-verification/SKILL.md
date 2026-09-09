---
name: live-verification
description: Verify runtime/deployed behavior on the real relevant stack rather than stopping at unit tests.
metadata:
  class: RISK_TRIGGERED
  authority: portable-agentic-flow
---

# live-verification

Use when changed behavior depends on container/runtime/wiring/integration/deploy paths that static/unit tests cannot establish.

Rebuild/restart only within the authorized environment, exercise the real path, and capture a bounded receipt.

## Mutation authority
Only the environment explicitly authorized by the task. Production requires separate owner authority.

## Output
Environment identity, build/deploy identity, request/action, observed result.

## Fail closed
`Unit tests pass` is not a live receipt.
