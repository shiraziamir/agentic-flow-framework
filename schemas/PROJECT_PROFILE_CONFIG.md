# Project Profile Config Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

A target project should keep one small, durable project-level profile, typically `.agentic/PROJECT_PROFILE.yaml`. It declares baseline operating intent and guardrails. It is not a proof that the project satisfies them.

Recommended shape:

```yaml
profile_version: 1
project_id: <stable-id>
updated_at: <RFC3339>

codebase_scale: SMALL|MEDIUM|LARGE
readiness_tier: BASIC|STANDARD|HIGH_ASSURANCE

surfaces:
  frontend: true|false
  backend: true|false
  shared: true|false
  data: true|false
  infra: true|false

quality:
  test_strategy: RISK_BASED|TEST_FIRST_FOR_MATERIAL_CLAIMS|TDD_STRICT
  mutation_or_path_proof:
    required_for_load_bearing_tests: true|false
  minimum_layers: [UNIT, INTEGRATION, CONTRACT, E2E, LIVE]

operations:
  metrics: REQUIRED|OPTIONAL|NOT_APPLICABLE
  logs: REQUIRED|OPTIONAL|NOT_APPLICABLE
  traces: REQUIRED|OPTIONAL|NOT_APPLICABLE
  slo: REQUIRED|OPTIONAL|NOT_APPLICABLE
  backup: REQUIRED|OPTIONAL|NOT_APPLICABLE
  restore_test: REQUIRED|OPTIONAL|NOT_APPLICABLE
  rollback: REQUIRED|OPTIONAL|NOT_APPLICABLE

security:
  threat_model: REQUIRED|OPTIONAL|NOT_APPLICABLE
  dependency_review: REQUIRED|OPTIONAL|NOT_APPLICABLE
  secret_scanning: REQUIRED|OPTIONAL|NOT_APPLICABLE
  least_privilege: REQUIRED|OPTIONAL|NOT_APPLICABLE

agent_environment_policy:
  local: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  ephemeral_test: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  shared_test: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  staging: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  production_read: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  production_mutation: OWNER_APPROVAL|DENIED

architecture_policy:
  pattern_mode: AGENT_PROPOSES_OWNER_MAY_OVERRIDE|OWNER_SPECIFIES|AGENT_AUTONOMOUS_WITHIN_GUARDRAILS
  require_rationale_for_new_abstraction: true
  avoid_pattern_without_boundary_or_failure_mode: true

temporary_overrides:
  directory: .agentic/overrides
  require_expiry: true
  require_owner: true
  require_reason: true
  require_compensating_control: true
```

## Rules

1. This file describes the baseline; current receipts determine reality.
2. A baseline requirement must not be silently switched off during a task. Use `schemas/TEMPORARY_OVERRIDE.md`.
3. `NOT_APPLICABLE` requires a durable rationale when the capability would normally be expected for the selected readiness tier.
4. Agent permissions are an upper bound, not automatic authority. Task/governance/environment authorization can further restrict them.
5. Keep this profile concise. Detailed policy remains in canonical framework/project docs and production profiles.
