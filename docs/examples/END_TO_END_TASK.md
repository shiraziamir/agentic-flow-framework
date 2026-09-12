# End-to-End Task Example

This example shows the artifacts and decisions for a small backend defect without pretending a mocked unit test proves database behavior.

## Scenario

An order endpoint sometimes returns success even though writing the audit row fails. The operator wants the order and audit record to commit or roll back together.

Assume the project profile permits local and ephemeral tests automatically, requires `STRICT_PREVIEW`, and requires a real database when persistence is affected.

## 1. Operator intent

```text
Fix order creation so the order and its audit record are atomic.
Do not change the public request/response contract.
Do not touch production.
```

This states intent, not implementation, mutation or environment authority.

## 2. Designer: read-only proposal

The Designer inspects an identified ref:

```yaml
repository_ref: 4f2c... on feature/order-audit
observed:
  - src/orders/service.py owns order creation
  - src/audit/repository.py writes the audit row
  - tests currently mock both repositories
unknown:
  - whether both repositories share one connection/transaction
```

Contract proposal:

```yaml
objective: order and audit persistence are atomic
in_scope:
  - order creation transaction boundary
  - regression/integration tests for audit failure
out_of_scope:
  - response schema changes
  - unrelated repository refactor
  - production deploy or data mutation
acceptance:
  - successful request persists both records
  - forced audit failure persists neither record
  - existing response contract remains unchanged
planned_claims:
  - statement: rollback is atomic against PostgreSQL
    minimum_receipt: real application path + disposable PostgreSQL query confirming neither row persists
stop_conditions:
  - repositories cannot participate in one transaction without a public/architecture change
  - migration or production access becomes necessary
```

Advisory:

```text
[INVESTIGATE] Trace connection ownership through the service and both repositories.
[MUST] Preserve the frozen public response contract.
[MUST] Demonstrate atomic rollback through real PostgreSQL.
[SHOULD] Reuse the existing transaction helper if it already owns both repository calls; evidence: src/db/transaction.py is used by sibling write flows.
[AVOID] A test-only production branch or two independent commit calls.
[AVOID] Treating mocked rollback calls as proof that neither row persisted.
```

The Designer returns a proposal. It does not freeze or implement it.

## 3. Manager: task review and freeze

The Manager reads the contract first, then repository evidence. It resolves the unknown: both repositories can accept the same transaction-scoped connection without changing the public API.

```yaml
decision: PASS_TO_FREEZE
reviewed_repository_ref: 4f2c...
required_change:
  - name the disposable PostgreSQL setup and cleanup plan
frozen_task_id: ORDER-AUDIT-ATOMIC-01
task_authority: bounded to listed files/behavior
mutation_authority: not yet granted
environment_authority:
  local_real: allowed
  ephemeral_test: allowed
  production: denied
```

## 4. Executor: implementation design and STRICT_PREVIEW

Before editing:

```text
IMPLEMENTATION DESIGN PROPOSED

Observed current design
- service creates order, then calls audit repository with a separate connection

Chosen implementation shape
- enter the existing transaction helper in the service
- pass its connection to both existing repository methods
- add one real-PostgreSQL integration test that injects audit failure

Affected files
- src/orders/service.py
- tests/integration/test_order_audit_atomicity.py

Why smallest coherent
- reuses the existing transaction owner; no new abstraction or public API

Verification
- focused unit suite
- disposable PostgreSQL: success persists both rows
- disposable PostgreSQL: audit failure persists neither row
- query database after each request
- record commit SHA, container/image version and test output

Advisory departures
- none

Out of scope
- deployment, production data, unrelated transaction cleanup
```

Under `STRICT_PREVIEW`, the Manager checks this bounded batch and explicitly approves it. The frozen task alone did not authorize mutation.

## 5. Executor: isolated implementation and receipts

The Executor creates/uses an isolated task branch, edits only the approved files, and runs the planned tests in an authorized disposable environment.

Illustrative receipt:

```yaml
repository:
  base: 4f2c...
  head: 91ab...
  branch: task/order-audit-atomic
environment:
  kind: EPHEMERAL_TEST
  application_ref: 91ab...
  database: postgres:17.6
  isolation: disposable container
claims:
  - statement: successful flow persists order and audit
    status: VERIFIED
    receipt: integration test + direct row query
  - statement: audit failure rolls back both rows
    status: VERIFIED
    receipt: forced real-path failure + direct query showing zero new rows
  - statement: no regressions
    status: NOT_CLAIMED
checks:
  focused_unit: PASS
  postgres_integration: PASS
not_executed:
  - staging
  - production
```

A mocked test may still exist for fast feedback, but it is not the receipt used to close the persistence claim.

## 6. Manager: real commit/PR review

The Manager reviews in this order:

1. frozen contract;
2. advisory;
3. base/head diff and relevant surrounding source;
4. raw test/environment receipts;
5. Executor summary last.

```yaml
reviewed_base: 4f2c...
reviewed_head: 91ab...
decision: APPROVE
contract_findings: []
advisory_departures_reviewed: []
checks_observed:
  - focused unit PASS
  - disposable PostgreSQL integration PASS
checks_not_observed:
  - staging
  - production
residual_risk:
  - no evidence from production traffic
merge_authority: operator/project policy
```

If the PR head changes, the review is stale until the Manager reviews the new head.

## 7. Closure language

Good:

```text
At commit 91ab..., the focused suite passed and the identified disposable
PostgreSQL integration run observed both success persistence and rollback on
forced audit failure. Staging and production were not tested.
```

Not supported:

```text
The ordering system is fully correct and production-ready with no regressions.
```

This example preserves the essential separation: task authority, mutation authority, environment authority and evidence-based closure.
