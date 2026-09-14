# System Truth Map — Dual-Lens Baseline

**Status:** project-level durable map  
**Updated:** 2026-09-14

The System Truth Map is the compact project-level input for the **System Lens**. It prevents a locally correct change from silently breaking data authority, recovery, tenant isolation, cost accounting, observability, or another subsystem.

It is deliberately smaller than a full architecture document. Keep it current enough to answer: **what exists, what is authoritative, where trust changes, what survives failure/restart, and what the current scale boundary is.**

## 1. Recommended shape

```yaml
system_truth_map_version: 1
updated_at: <RFC3339>
repository_ref: <commit/ref>

components:
  entry_points: []
  trust_boundaries: []
  databases: []
  caches: []
  queues: []
  external_providers: []
  background_workers: []
  admin_operations: []
  metrics_and_alerts: []
  deployment_and_recovery: []

data_authority:
  - name: <business/system datum>
    authoritative_source: <store/service/log>
    derived_or_cached_copies: []
    writers: []
    readers: []
    ttl_or_freshness: <value|null>
    maximum_size_or_bound: <value|null>
    privacy_class: PUBLIC|INTERNAL|CONFIDENTIAL|SENSITIVE|PROJECT_DEFINED
    restart_behavior: <what survives/reconstructs>
    failure_behavior: <fail-open|fail-closed|unavailable|degraded|project-defined>
    recovery_procedure: <ref|summary>
    tenant_isolation: <mechanism|NOT_APPLICABLE|UNKNOWN>

scale_boundaries:
  current_target: <demo|early-tenants|production|project-defined>
  resources:
    - name: <queue/cache/db/provider/etc>
      expected_load: <value|UNKNOWN>
      known_ceiling: <value|UNKNOWN>
      soft_warning: <value|UNKNOWN>
      hard_safety_limit: <value|UNKNOWN|NOT_APPLICABLE>
      failure_behavior: <bounded behavior>
      scale_up_trigger: <signal/threshold>

cross_system_audit:
  last_audit_ref: <ref|null>
  material_tasks_since_last_audit: <integer>
  next_trigger: <task-count|demo|release|incident|manual>
```

## 2. Data-authority rules

- A cache, projection, summary, metric or replica is **not** authoritative merely because it is convenient to read.
- If a business-critical value such as spend, entitlement, authorization, tenant ownership or durable attempt state has no clear authority, raise a System-Lens finding before broad implementation continues.
- When authority is unavailable, failure semantics must be explicit. Do not fabricate a safe-looking substitute such as `0`, empty data, success, or stale truth unless the contract explicitly permits it.
- Derived state must declare how it is rebuilt or reconciled after restart/failure.
- Tenant isolation belongs in the authority map whenever data is tenant-scoped.

## 3. System map rules

The map should identify, at minimum when applicable:

```text
ENTRY POINTS
TRUST BOUNDARIES
DATABASES
CACHES
QUEUES
EXTERNAL PROVIDERS
BACKGROUND WORKERS
ADMIN OPERATIONS
METRICS / ALERTS
DEPLOYMENT / ROLLBACK / RECOVERY
```

This is not a request for a large design document. One compact diagram/table is enough when it accurately exposes the important boundaries.

## 4. Threat/failure mini-review

At project inception and when a load-bearing boundary changes, ask briefly:

```text
What can leak?
What can be counted twice?
What can be silently lost?
What survives restart?
What becomes stale?
What can grow without a bound?
What happens under concurrency?
What happens when a dependency lies or partially fails?
What can one tenant do to another?
What can cause unexpected external-provider spend?
What can an administrator safely do later?
```

Record only material risks/decisions. Do not turn this into an unbounded threat-modeling exercise.

## 5. Cross-System Effect Matrix

Material tasks use this fixed System-Lens checklist:

```text
WRITE
READ
AGGREGATE
CACHE
RESTART
FAILURE
RECOVERY
ADMIN
METRIC
TENANT_ISOLATION
SCALE
PRIVACY
COST
```

Each row gets exactly one state:

```text
UNAFFECTED
VERIFIED
CHANGED_AND_TESTED
OPEN_RISK
NOT_APPLICABLE
```

`UNAFFECTED` is a reviewed conclusion, not a default copied into every row.

## 6. Periodic cross-system audit

Task-local correctness does not guarantee that relationships between components remain correct. Run a broader audit on a configured cadence and at major boundaries.

Recommended heuristic triggers:

```text
every ~5–8 material tasks (project-configurable)
before demo deployment when system behavior matters
before every real-customer release
after every material incident
before/after a major architecture or data-authority change
```

Audit themes:

```text
FINANCIAL TRUTH
PRIVACY TRUTH
IDENTITY / AUTHORIZATION
TENANT ISOLATION
RESTART SURVIVAL
BACKUP / RESTORE
OBSERVABILITY TRUTH
CAPACITY BOUNDS
EXTERNAL-PROVIDER FAILURE / SPEND
ADMIN RECOVERY
```

## 7. Evidence boundary

The System Truth Map is a model of intended/current system relationships. It is **not proof** that those relationships work. Runtime claims still require receipts from an adequate environment.

Update this map only when a material component, authority, trust boundary, recovery rule or scale boundary changes. Avoid documentation churn for local implementation details.