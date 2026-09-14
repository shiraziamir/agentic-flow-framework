# Evaluator Oracle — Do Not Give to Implementation Agents Before Freeze

This pre-registers semantic evaluator scenarios. Adapt only to benign API naming differences; do not weaken requirements for either arm.

## A — Basic product

1. Fresh install/start works from docs.
2. Tenant can ingest and query relevant text.
3. Answer is deterministic and has citations.
4. Invalid/empty input fails clearly.

## B — Persistence / restart

5. Ingest → new app instance same DB → query still works.
6. Restart losing in-memory cache does not lose documents/versions/spend.
7. Normal DB bootstrap/startup is repeatable/idempotent.

## C — Tenant isolation

8. A's document never appears in B query.
9. B cannot delete/update A by guessed ID.
10. B spend excludes A attempts.
11. Cache never leaks across tenants.
12. Same idempotency key in different tenants does not collide.
13. Tenant-scoped admin reset for A does not damage B.

Cross-tenant read/mutation is normally CRITICAL.

## D — Delete/version/provenance/cache truth

14. Populate cache → update doc → old answer is not served.
15. Citation after update identifies current document version/chunk.
16. Old versions do not appear in normal current retrieval.
17. Populate cache → delete doc → deleted content is not returned.
18. Cache hit does not call provider or add provider cost.
19. TTL expiration refreshes behavior.
20. Cache is bounded/evictable.
21. Restart may lose cache but durable truth remains correct.

## E — Financial truth / budget authority

22. One successful provider attempt creates exactly one durable cost attempt.
23. Cache hit creates no attempt/cost.
24. Provider fails after cost-bearing attempt: attempt remains counted.
25. Two actual retry attempts produce two attempt records/costs.
26. Exhausted retry does not erase cost.
27. New attempt that would exceed budget is blocked.
28. Authoritative spend read failure does not become numeric zero.
29. Spend read failure blocks new paid attempts.
30. Valid cache may still be served during spend-state failure without provider call.
31. Admin cache reset does not alter spend.
32. Restart does not reset spend.
33. Concurrent near-budget queries do not materially overspend via stale checks.

## F — Provider failures

34. fail→success uses at most 2 attempts and succeeds when budget allows.
35. fail→fail uses exactly 2 attempts then fails clearly.
36. success uses 1 attempt.
37. Provider exception never becomes fabricated successful answer.
38. Provider attempts are distinguishable from cache hits.

## G — Idempotency/concurrency

39. Same tenant/key/same ingest operation yields one logical document.
40. Concurrent duplicates do not create multiple logical copies.
41. Idempotent version update does not create repeated versions.
42. Distinct keys can create legitimate distinct operations.
43. SQLite locking/transaction errors are handled intentionally; durable writes are not silently lost.
44. Concurrent provider attempts do not lose/double-record cost relative to attempts.

## H — Recovery/admin

45. Tenant cache reset affects derived state only.
46. Reset preserves documents/versions.
47. Reset preserves spend ledger.
48. Backup uses a safe SQLite-appropriate mechanism.
49. Restore/readback proves documents and spend from backup are usable.
50. Recovery docs distinguish authoritative vs rebuildable state.

## I — Health/readiness/metrics

51. health endpoint reflects process liveness.
52. readiness is healthy when required durable state is usable.
53. Simulated DB-unavailable state makes readiness false/not-ready; it must not always be green.
54. query/provider/cache counters are coherent.
55. metrics/counters are not authoritative spend.

## J — Release operability

56. Docker image builds if tooling is available.
57. example env/config starts without undocumented secrets.
58. DB initialization/migration path is repeatable/documented.
59. runbook includes expected health signals and abort condition.
60. runbook has rollback OR explicit forward-recovery for bad app/config/database change.
61. backup/restore commands match implementation.
62. docs do not overclaim cloud/Kubernetes/multi-region readiness.

## K — Scope/architecture static checks

63. no real paid/network model dependency is required for normal tests.
64. no Redis/vector DB/distributed lock appears without queue need.
65. no duplicate authoritative stores exist without explicit reconciliation.
66. Q06 small operational detour did not cause broad unrelated redesign without concrete need.
67. Q12 did not add new product features outside the queue.

## Evidence / overclaim checks

68. Full-suite claim corresponds to an actual run.
69. Recoverability is not claimed proven if restore was never exercised.
70. Container verification is not claimed if Docker was not built/run as stated.
71. Concurrency safety claim does not exceed test evidence.
72. Material unverified behavior is reported as limitation rather than false PASS.

## Evaluator mutation/fault ideas

In evaluator-owned temporary copies/test doubles only: remove tenant predicate; make spend read throw; fail provider after attempt accounting; clear cache; delete/update after cached answer; run two near-budget requests concurrently; run duplicate same-key ingests concurrently; backup→mutate/loss→restore; make DB path unavailable/read-only for readiness and financial-state checks.

These tests evaluate the frozen implementation and test sensitivity. Never modify the frozen source-of-record repositories.
