# Project Profile Config Schema

**Schema version:** 1.2  
**Updated:** 2026-09-12

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

agent_mutation_policy:
  mode: STRICT_PREVIEW|MATERIAL_CHANGES_ONLY|BOUNDED_AUTONOMY
  group_related_changes_into_batches: true|false
  require_current_vs_proposed_state: true|false
  require_planned_checks_before_apply: true|false
  require_rollback_for_material_changes: true|false

usage_reporting:
  quota_snapshot: ENABLED|OPTIONAL|DISABLED
  report_after_material_task: true|false
  notify_operator: true|false
  stale_after_seconds: <integer>
  never_reduce_acceptance_quality: true

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

## Mutation approval policy

Use `schemas/MUTATION_APPROVAL_POLICY.md`.

Recommended default for first adoption or an operator who wants explicit control:

```yaml
agent_mutation_policy:
  mode: STRICT_PREVIEW
  group_related_changes_into_batches: true
  require_current_vs_proposed_state: true
  require_planned_checks_before_apply: true
  require_rollback_for_material_changes: true
```

Under `STRICT_PREVIEW`, read-only discovery is allowed without a mutation approval. Before each bounded mutation batch, the agent reports current state, proposed state, affected files/resources, impacts, planned checks, rollback/recovery when relevant, and explicit out-of-scope boundaries; then waits for `APPROVE`/`APPLY`.

## Usage/quota reporting

Use `schemas/USAGE_QUOTA_SNAPSHOT.md` and `docs/agent/USAGE_AWARE_TASK_REPORTING.md`.

When enabled and the harness exposes trustworthy quota telemetry, append one compact usage snapshot after each **material task/checkpoint**, not after every trivial tool call. Missing telemetry must be reported as unavailable rather than fabricated.

Quota information is an operator/routing signal only. Low quota may justify checkpointing or proposing deferral, but never silently skips required tests, security checks, evidence, or review.

## Rules

1. This file describes the baseline; current receipts determine reality.
2. A baseline requirement must not be silently switched off during a task. Use `schemas/TEMPORARY_OVERRIDE.md`.
3. `NOT_APPLICABLE` requires a durable rationale when the capability would normally be expected for the selected readiness tier.
4. Agent permissions are an upper bound, not automatic authority. Task/governance/environment authorization can further restrict them.
5. Mutation approval and environment authorization are separate: approval to edit source does not authorize production mutation.
6. Usage/quota values are telemetry, not task-completion evidence.
7. Keep this profile concise. Detailed policy remains in canonical framework/project docs and production profiles.
