# Production Profile — Agent Environments

**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

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
