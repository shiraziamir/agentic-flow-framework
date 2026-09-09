---
name: resilience-chaos
description: Design or review bounded resilience/failure experiments using steady-state evidence, blast-radius controls, abort conditions and recovery proof.
metadata:
  class: RISK_TRIGGERED
  authority: portable-agentic-flow
---

# Resilience and Chaos

## USE WHEN

- distributed/failure-sensitive behavior matters;
- recovery/failover assumptions need proof;
- retries/timeouts/idempotency/fallback behavior is material;
- a chaos/fault-injection experiment is proposed.

## PROCEDURE

1. Identify user/service steady-state metric or SLI.
2. State the failure hypothesis and expected behavior.
3. Choose the smallest realistic fault that can discriminate the hypothesis.
4. Freeze environment, blast radius, maximum duration and abort conditions.
5. Verify recovery path and operator access before injecting failure.
6. Run in non-production first unless an explicitly approved higher-assurance workflow justifies controlled production testing.
7. Observe user-impact plus metrics/logs/traces.
8. Restore and verify steady state.
9. Record defects/follow-ups; do not call an experiment successful just because infrastructure survived.

## FAIL CLOSED

Do not run a production chaos experiment when observability, recovery, blast-radius control or authorization is missing.

## OUTPUT

Experiment contract, receipts, result `PASS|FAIL|ABORTED|INCONCLUSIVE`, discovered weakness and bounded follow-up.