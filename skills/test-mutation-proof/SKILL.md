---
name: test-mutation-proof
description: Prove a load-bearing test/check can detect the behavior it claims by intentional falsification, changed-path proof, or an equivalent controlled red/green experiment.
metadata:
  class: RISK_TRIGGERED
  authority: portable-agentic-flow
---

# Test Mutation Proof / Check-the-Checker

**Updated:** 2026-09-09T10:04:00Z

Use for new/changed tests or automated checks that carry important correctness/safety claims, especially when a green result could arise because the changed path is mocked, cached, unreachable or not asserted.

## Preferred procedure

1. Run the target check green at the identified ref.
2. Make the smallest safe temporary mutation/fault expected to violate the asserted behavior.
3. Run the target check and observe **red for the intended reason**.
4. Restore exactly.
5. Re-run green.
6. Confirm working tree is restored except intended task changes.
7. Record this as `PATH_PROOF` / mutation receipt tied to the ref/check.

## Alternatives when mutation is unsafe/impractical

Use another explicit changed-path/falsification method such as:

- coverage/instrumentation showing the changed branch executed;
- controlled fixture/input that distinguishes old vs new behavior;
- disable/bypass the changed mechanism and prove the check fails;
- known-bad artifact/config fixture;
- linter/checker self-test with intentionally invalid input.

State why the alternative establishes the same property.

## Do not

- mutate production/shared persistent data merely to test the checker;
- accept a red result caused by unrelated syntax/setup failure;
- leave temporary mutations behind;
- assume snapshot/golden output is meaningful if the assertion cannot detect the intended semantic fault;
- require mutation proof for every trivial test; route by load-bearing risk.

## Mutation authority

Temporary controlled mutation only in safe/local or explicitly authorized isolated test scope.

## Output

Green → falsification → expected red → restore → green, or equivalent PATH_PROOF receipts.

## Fail closed

A load-bearing test/check that cannot be shown to detect the relevant fault has not proved the claim it is being used to support.
