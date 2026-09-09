# Verification Profile — BACKEND

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for server handlers, domain/services, jobs/queues, integrations and backend runtime behavior.

## Core checks

1. compile/type/lint/build as applicable;
2. focused unit/domain tests for changed logic;
3. integration through the real handler/service/repository boundary when the claim crosses layers;
4. request/input validation and relevant malformed/boundary cases;
5. authentication/authorization/tenant/ownership paths when applicable;
6. error mapping/status/result semantics, not only success path;
7. timeout/retry/idempotency behavior for external calls/jobs when relevant;
8. actual persistence receipt when durable data semantics are claimed;
9. consumer/provider contract checks for public/shared APIs;
10. logs/metrics/traces or runtime smoke when operational behavior is part of the claim.

## Receipt rules

- `200 OK` proves only that the observed request received that status; it does not prove correct persistence, downstream effect or consumer compatibility.
- A mocked repository/provider cannot by itself prove the real integration boundary.
- A unit test of a helper cannot prove that the production handler actually routes through that helper.
- For jobs/queues, enqueue success is not completion; name the stage actually observed.

## Backend blind spots

- authorization/tenant boundary omitted while functional path passes;
- invalid/empty/duplicate input omitted;
- transaction rollback/partial write not checked;
- retry creates duplicate side effects;
- timeout/cancellation path not propagated;
- provider fallback silently changes semantics;
- serializer/schema differs from domain object assumptions;
- queue/job ack occurs before durable work;
- cache masks database/provider path;
- timezone/order/precision/nullability boundary differs in real storage/transport;
- integration test calls a test helper instead of the real handler/client path.
