# Change Classification Schema

**Schema version:** 1.2  
**Updated:** 2026-09-09T10:40:00Z

Classify a material change before freezing its verification plan. Classification routes verification **and** production-readiness impact; it is not a substitute for reading the actual diff/dependency graph.

```yaml
classification_version: 2
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
  - DEPENDENCY_SUPPLY_CHAIN

operational_flags:
  - INTERNET_EXPOSED
  - USER_FACING
  - MULTI_TENANT
  - STATEFUL
  - SENSITIVE_DATA
  - REGULATED_DATA
  - PRIVILEGED_OPERATION
  - BACKUP_RECOVERY
  - RELEASE_PIPELINE
  - KUBERNETES_RUNTIME
  - ONCALL_IMPACT
  - SLO_IMPACT
  - LOGS_TO_AI
  - CHAOS_OR_FAILURE_INJECTION

runtime_mutation_scope: NONE|LOCAL|TESTENV|PRODUCTION
public_contract_change: true|false
affected_consumers: [<module/service/client/environment>]
verification_profiles: [GENERAL, <primary>, <cross-cutting annexes>]
production_profile_ref: <path/version/hash|NONE>
production_profiles_affected:
  - DELIVERY
  - OBSERVABILITY
  - DATA_DURABILITY
  - TROUBLESHOOTING
  - SECURITY_FIRST
  - AI_LOG_ANALYSIS
  - RESILIENCE_CHAOS
  - CODE_ARCHITECTURE
classification_evidence:
  - <path/diff/project-graph/import/API/schema/manifest/runtime evidence>
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

## Production-routing examples

- `CI_CD` or production deployment change → `DELIVERY` + usually `SECURITY_FIRST`.
- `OBSERVABILITY`/health/telemetry change → `OBSERVABILITY`; add `AI_LOG_ANALYSIS` if logs enter LLM/agent workflows.
- `DATA`, `PERSISTENCE`, `MIGRATION`, `BACKUP_RECOVERY` → `DATA_DURABILITY`.
- `AUTH_SECURITY`, `INTERNET_EXPOSED`, `SENSITIVE_DATA`, `PRIVILEGED_OPERATION` → `SECURITY_FIRST`.
- `CONCURRENCY`, `EXTERNAL_PROVIDER`, critical cache/queue/network failure semantics → consider `RESILIENCE_CHAOS`.
- provider/legacy/shared-boundary/refactor that changes long-term coupling → `CODE_ARCHITECTURE`.
- production service whose operability changes → `TROUBLESHOOTING`.

## Rules

1. Use deterministic path/project/dependency evidence first; agent intuition is only a proposal.
2. Select one primary surface and zero or more flags. A task can affect several systems; use affected consumers and profiles rather than hiding that fact.
3. Security, persistence, public-contract, migration, production, sensitive-data or supply-chain changes may raise governance regardless of primary surface or repository size.
4. `DEPENDENCY` changes should normally add `DEPENDENCY_SUPPLY_CHAIN` when manifest/lock/package/action/container/base-image behavior changes.
5. `TEST_ONLY` changes that create/modify a load-bearing verification gate should trigger `test-mutation-proof` or equivalent falsification when practical.
6. If a production project has no current `PRODUCTION_PROFILE`, report that as a readiness gap; do not silently infer a tier.
7. If APPLY discovers an undeclared surface, operational flag or readiness requirement that materially changes verification, authority or scope: **STOP → record evidence → amend classification/contract**.
8. Never downgrade classification/readiness merely to reduce ceremony, token use or test cost.