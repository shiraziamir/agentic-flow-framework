# Change Classification Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Classify a material change before freezing its verification plan. Classification is a routing input, not a substitute for reading the actual diff/dependency graph.

```yaml
classification_version: 1
primary_surface: FRONTEND|BACKEND|SHARED|DATA|INFRA|CI_CD|TOOLING|DOCS_EVIDENCE
change_kind: BUG_FIX|FEATURE|REFACTOR|TEST_ONLY|DOCS_ONLY|CONFIG|DEPENDENCY|MIGRATION|PERFORMANCE|RELIABILITY
cross_cutting_flags:
  - AUTH_SECURITY
  - PUBLIC_CONTRACT
  - PERSISTENCE
  - CONCURRENCY
  - CACHE_STATE
  - EXTERNAL_PROVIDER
  - PERFORMANCE
  - MIGRATION
  - OBSERVABILITY
  - PRODUCTION
runtime_mutation_scope: NONE|LOCAL|TESTENV|PRODUCTION
public_contract_change: true|false
affected_consumers: [<module/service/client/environment>]
verification_profiles: [GENERAL, <primary>, <cross-cutting annexes>]
classification_evidence:
  - <path/diff/project-graph/import/API/schema evidence>
```

## Primary surfaces

- `FRONTEND` — rendered UI, browser/client state, navigation, frontend API clients.
- `BACKEND` — server handlers, services, domain logic, queues/jobs, service integrations.
- `SHARED` — public/shared libraries, schemas, types, utilities or contracts consumed by multiple surfaces.
- `DATA` — schema, migrations, durable persistence semantics, backfills.
- `INFRA` — cloud/Kubernetes/network/runtime platform configuration.
- `CI_CD` — pipelines, release/deploy orchestration, build artifact movement.
- `TOOLING` — repository/dev tooling that does not itself define product runtime behavior.
- `DOCS_EVIDENCE` — documentation/evidence-only changes with no runtime authority.

## Rules

1. Use deterministic path/project/dependency evidence first; agent intuition is only a proposal.
2. Select one primary surface and zero or more cross-cutting flags. A task can touch several surfaces; use `affected_consumers` and annexes rather than hiding that fact.
3. `AUTH_SECURITY`, `PERSISTENCE`, `PUBLIC_CONTRACT`, `MIGRATION`, or `PRODUCTION` may raise governance regardless of primary surface.
4. If APPLY discovers an undeclared surface or cross-cutting risk that materially changes verification, authority, or scope: **STOP → record evidence → amend classification/contract**.
5. Never downgrade classification merely to reduce ceremony, token use, or test cost.
