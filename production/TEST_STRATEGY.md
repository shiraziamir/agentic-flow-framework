# Production Profile — Test Strategy

**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

Goal: define tests before implementation strongly enough to prevent narrative-driven closure, without forcing strict TDD on every low-risk edit.

## Default policy

Use `TEST_FIRST_FOR_MATERIAL_CLAIMS` by default:

1. before code mutation, define observable DoD and planned closure claims;
2. identify the minimum test/receipt layer that can establish each claim;
3. add or freeze the relevant test cases/fixtures before or alongside implementation;
4. implement the change;
5. run the planned tests;
6. for load-bearing new tests, prove they can detect the relevant defect using mutation/path proof when practical;
7. restore the code exactly and re-run green;
8. run broader affected/baseline checks required by the task.

Strict red-green-refactor TDD is optional and may be selected by project/team preference. The framework does not require writing every unit test before every line of implementation.

## Why

A test written only after seeing the final implementation can accidentally encode the implementation rather than independently capture intended behavior. Freezing important acceptance examples/claims early reduces this risk.

## Layering

Select the smallest useful layer, then add broader layers according to risk:

- small/unit: fast deterministic logic feedback;
- medium/integration: database/filesystem/local service/process boundaries;
- contract: producer/consumer/public boundary compatibility;
- large/E2E/live: complete user/service path or real external/runtime conditions.

Google has long distinguished Small/Medium/Large tests by resources and external-system usage; current Microsoft Well-Architected guidance recommends layered tests, early continuous testing and production-like environments proportional to risk.

## Mutation/path proof

Use for tests that materially carry closure/security/regression claims, especially newly added tests for a defect.

Preferred sequence:

```text
known good GREEN
→ controlled break of intended behavior
→ expected RED for the intended reason
→ exact restore
→ GREEN again
```

If direct mutation is unsafe or expensive, use an equivalent falsification receipt such as a known-bad fixture, old implementation comparison, dependency fault, invalid policy/config, or coverage/path instrumentation.

Do not mutate production merely to prove a test.

## Do not overdo it

Tiny reversible formatting/docs/mechanical changes do not need mutation testing. The cost of the proof must be proportional to the risk and load-bearing nature of the test.
