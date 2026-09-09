# Verification Profile — DATA / PERSISTENCE

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for schema changes, migrations, durable storage semantics, backfills or changes whose correctness depends on persistence.

## Core checks

1. identify exact storage/schema/migration version and representative starting state;
2. validate/plan schema migration before applying where tooling supports it;
3. test forward migration on representative existing data when feasible;
4. verify write/read round trip or equivalent durable state transition;
5. verify constraints, null/default/precision/order/time semantics that matter;
6. verify transaction/rollback/partial-failure behavior where applicable;
7. assess idempotency/re-run behavior for migration/backfill jobs;
8. define rollback/restore strategy; if irreversible, state that explicitly rather than claiming rollback safety;
9. check application compatibility during rolling/mixed-version deployment when relevant;
10. capture target environment/storage identity for live/testenv evidence.

## Receipt rules

- Application response success is not a persistence receipt.
- Migration file presence is not proof the migration was applied.
- A clean new database does not prove migration safety for existing data.
- A down migration is not automatically a safe rollback if data has been transformed/lost.

## Data blind spots

- migration succeeds empty but fails on production-shaped data;
- existing null/duplicate/out-of-range values violate new constraint;
- partial migration leaves mixed state;
- backfill is not idempotent;
- old and new app versions are incompatible during rollout;
- timezone/precision/encoding/collation semantics change;
- read path uses cache and hides persistence failure;
- irreversible data loss hidden behind a syntactically valid rollback;
- restore/backup assumption was never exercised or documented;
- test database engine/version differs materially from target.
