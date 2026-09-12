# Production Profile — Agent Environments

**Version:** 1.1
**Updated:** 2026-09-13

Goal: give agents enough real execution capability to verify code while preserving environment and production safety.

## Preferred environment ladder

```text
LOCAL / HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST / INTEGRATION
→ STAGING / PRODUCTION-LIKE
→ CONTROLLED PRODUCTION READ/CANARY
→ PRODUCTION MUTATION (explicit authority only)
```

Use the lowest environment that can directly establish the required claim.

## Execution-readiness gate

For behavior-changing work, the Executor must have at least one authorized environment that can exercise the real changed path. Ability to edit, compile or run isolated mocks is not enough when closure claims cross a real boundary.

Normal baseline for non-documentation work:

```text
LOCAL_REAL or EPHEMERAL_TEST
```

`LOCAL_REAL` means the relevant application runtime plus the affected real local dependencies (for example a disposable database/container and actual migrations). `EPHEMERAL_TEST` means an isolated, disposable integration environment with the relevant runtime and boundaries. Neither label grants access by itself.

The requirement is claim-dependent:

| Planned claim | Minimum meaningful environment/receipt |
|---|---|
| pure transformation behaves as specified | focused test may be sufficient |
| service and database transaction interact correctly | real application + disposable real database integration |
| migration preserves/transforms data correctly | actual migration engine against representative disposable data |
| provider contract is honored | contract test plus approved sandbox/faithful controlled boundary as required |
| user workflow works | running application and relevant real boundaries; browser/runtime receipt when applicable |
| deployed behavior exists in target X | identified target environment + exact deployed artifact + live check |

If the minimum environment is unavailable, record `UNVERIFIED` or `BLOCKED` and issue an environment request. Do not replace the claim with a weaker mock receipt while keeping the stronger wording.

## Mock semantics

Mocks/fakes are valuable for narrow, deterministic tests. They establish only the modeled boundary. A mock-only pass cannot close integration, persistence, migration, end-user, deployment or production claims. Pair it with real-boundary receipts when the planned claim crosses that boundary.

## Default policy

- local/hermetic: agent may create/run when project tooling permits;
- ephemeral test: preferred for integration/database/provider emulation and disposable experiments;
- shared test: allowed only when task identity and cleanup/isolation are defined;
- staging/production-like: use for deployment, migration, performance, security and realistic integration claims that lower environments cannot prove;
- production read-only: explicit permission or project profile policy, with bounded queries and no secret/raw-PII expansion;
- production mutation: separate owner authorization, blast-radius/rollback/monitoring plan and task governance appropriate to risk.

## Production-like environment

A production-like environment should mirror the properties that matter to the test rather than blindly duplicate cost:

- relevant runtime/container/OS versions;
- database/schema and representative data shape;
- network/security/identity boundaries;
- caching/autoscaling where behavior depends on them;
- external dependencies or faithful controlled substitutes;
- deployment mechanism and artifact format;
- telemetry sufficient to diagnose failures.

Microsoft Well-Architected guidance recommends purpose-driven environments and production-like environments proportional to workload risk; mission-critical guidance recommends at least one staging environment that meaningfully reflects production. Google SRE canarying acknowledges that lower environments cannot reproduce all real production traffic/conditions, so controlled progressive production exposure is sometimes required.

## Agent environment request

When the required receipt cannot be obtained in currently authorized environments, the agent should return:

```yaml
environment_request:
  required_for_claim: <claim-id>
  requested_environment: EPHEMERAL_TEST|SHARED_TEST|STAGING|PRODUCTION_READ|PRODUCTION_CANARY
  reason: <why lower environment is insufficient>
  resources/dependencies: []
  data_requirements: <synthetic/anonymized/representative>
  access_required: READ|DEPLOY|MUTATE_BOUNDED
  expected_duration: <bounded>
  cleanup_plan: <required for disposable/shared environments>
  risk: <bounded risk>
```

The request is evidence that an environment is needed, not permission to create/use it.

## Test data

Prefer synthetic representative data. If production-derived data is necessary, minimize/anonymize it and apply production-equivalent security controls appropriate to sensitivity.
