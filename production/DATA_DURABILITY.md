# Production Profile — Data Durability

**Version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

Goal: preserve important data and prove it can be recovered within business-defined loss/time bounds.

## First classify the data

For each durable store identify:

- owner and business purpose;
- data sensitivity/classification;
- source of truth vs derived/cache/rebuildable data;
- acceptable data loss (`RPO`);
- acceptable recovery time (`RTO`);
- retention/legal constraints;
- dependencies needed to restore usable service.

A backup policy without RPO/RTO and restore evidence is incomplete.

## Core invariant

> Backup success is not recoverability proof. Restore is the receipt.

## BASIC

For non-rebuildable production data:

- automated recurring backup or managed equivalent;
- backup location is not tied only to the live node/container/filesystem;
- encryption/access controls appropriate to data sensitivity;
- documented restore procedure;
- retention and deletion policy;
- last backup status observable;
- at least one restore test before claiming recoverability.

## STANDARD

Additionally:

- RPO/RTO documented and mapped to backup frequency/architecture;
- point-in-time recovery where business loss tolerance requires it;
- backup/restore monitoring and alerting;
- restore tests on a recurring schedule and after major storage/schema changes;
- restore test verifies application-readable data, not merely archive extraction;
- offsite/account/subscription/failure-domain separation appropriate to threat model;
- privileged backup credentials separated from normal application credentials where practical;
- retention lifecycle and capacity/cost monitored;
- migration/backfill changes include pre-change recovery point and rollback/forward-repair plan.

## HIGH_ASSURANCE

Additionally, where justified:

- recovery drills against realistic outage scenarios;
- immutable/write-protected backup copy or equivalent ransomware/deletion protection;
- multi-region/failure-domain recovery strategy when regional loss is in scope;
- independent verification of recovery artifacts and access path;
- measured restore duration compared with RTO;
- measured recoverable point compared with RPO;
- dependency/config/secrets/IaC restoration included in service recovery, not database data alone;
- regular review of backup exclusions and newly introduced data stores.

## Database-specific examples

### PostgreSQL

PostgreSQL documents SQL dump, filesystem backup, and continuous WAL archiving/PITR as distinct approaches. For PITR, base backups and required WAL segments must both be retained. Choose the method from RPO/RTO and size/operational needs rather than assuming `pg_dump` is sufficient for every database.

### MySQL

MySQL point-in-time recovery depends on a full backup plus binary logs after that backup. If PITR is required, verify binary logging/retention and perform a timed recovery exercise.

### Managed databases

Provider snapshots/backups are still subject to configuration, retention, permissions, region/account and restore behavior. Record the provider-specific recovery receipt rather than claiming recoverability from the existence of a checkbox.

## Migration safety

Before a destructive or compatibility-sensitive migration define:

```text
existing-data fixture/profile
forward migration
application compatibility window
backfill semantics
idempotency/retry behavior
partial-failure behavior
rollback or forward-repair strategy
recovery point before change
```

For zero/low-downtime systems prefer expand/contract or otherwise backward-compatible sequencing over simultaneous breaking schema + app release.

## Restore receipt

A material restore test records:

```text
backup/snapshot identity
target restore environment
restore start/end time
chosen point-in-time if applicable
validation queries/application checks
row/object/domain integrity checks as appropriate
missing/corrupt data discovered
measured RPO/RTO result
cleanup and access controls
```

## Gaps

Examples:

- backups exist but no restore has ever been tested;
- RPO/RTO are undefined;
- critical data store was added but is outside backup policy;
- backup account can be deleted by the same compromised principal as production;
- PITR is assumed but WAL/binlog retention is insufficient;
- restore works technically but application dependencies/config/secrets are missing;
- backups contain sensitive data without equivalent protection;
- retention policy conflicts with legal/privacy deletion requirements.