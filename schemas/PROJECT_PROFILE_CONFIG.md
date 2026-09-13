# Project Profile Config Schema

**Schema version:** 1.5  
**Updated:** 2026-09-13

A target project should keep one small durable profile, usually `.agentic/PROJECT_PROFILE.yaml`. It declares the intended operating bar; current receipts establish reality.

Recommended shape:

```yaml
profile_version: 1
project_id: <stable-id>
updated_at: <RFC3339>

codebase_scale: SMALL|MEDIUM|LARGE
readiness_tier: BASIC|STANDARD|HIGH_ASSURANCE

quality:
  test_strategy: RISK_BASED|TEST_FIRST_FOR_MATERIAL_CLAIMS|TDD_STRICT
  minimum_layers: [UNIT, INTEGRATION, CONTRACT, E2E, LIVE]
  mutation_or_path_proof:
    required_for_load_bearing_tests: true|false

execution_readiness:
  required_for_behavior_changes: true|false
  minimum_capability: LOCAL_REAL|EPHEMERAL_INTEGRATION|PROJECT_DEFINED
  real_application_runtime: REQUIRED_WHEN_AFFECTED|OPTIONAL
  real_database: REQUIRED_WHEN_AFFECTED|OPTIONAL|NOT_APPLICABLE
  real_migrations: REQUIRED_WHEN_AFFECTED|OPTIONAL|NOT_APPLICABLE
  real_external_boundary: REQUIRED_WHEN_CLAIMED|CONTROLLED_SUBSTITUTE_ALLOWED|NOT_APPLICABLE
  mock_only_closure: DENIED_FOR_INTEGRATION_OR_STRONGER|PROJECT_DEFINED
  when_unavailable: BLOCK_AND_REQUEST_ENVIRONMENT|REPORT_UNVERIFIED

agent_mutation_policy:
  mode: STRICT_PREVIEW|MATERIAL_CHANGES_ONLY|BOUNDED_AUTONOMY
  group_related_changes_into_batches: true|false
  require_current_vs_proposed_state: true|false
  require_planned_checks_before_apply: true|false
  require_rollback_for_material_changes: true|false
  remediation_windows:
    enabled: true|false
    default_max_iterations: <integer>
    manager_review_required_before_closure: true|false

workspace_safety:
  preserve_unknown_dirty_work: true
  destructive_git_requires_explicit_authority: true

external_effects:
  real_provider_calls: DENIED|EXPLICIT_AUTHORITY_REQUIRED|PROJECT_DEFINED
  paid_api_calls: DENIED|EXPLICIT_AUTHORITY_REQUIRED|PROJECT_DEFINED
  message_or_notification_sends: DENIED|EXPLICIT_AUTHORITY_REQUIRED|PROJECT_DEFINED

review_policy:
  pre_manager_adversarial_review: REQUIRED_FOR_MEDIUM_HIGH|OPTIONAL|DISABLED
  consolidated_manager_findings: true|false
  independent_closure: REQUIRED_FOR_HIGH|PROJECT_DEFINED|DISABLED

flow_metrics:
  enabled: true|false
  collect_material_tasks_only: true|false

agent_environment_policy:
  local: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  ephemeral_test: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  shared_test: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  staging: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  production_read: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  production_mutation: OWNER_APPROVAL|DENIED

production_mode:
  enabled: true|false
  rollback_or_forward_recovery_required_for_every_mutation: true
  require_abort_condition: true
  require_post_change_verification: true
  irreversible_change:
    require_forward_recovery_plan: true
    require_backup_or_checkpoint: true
    require_blast_radius_control: true

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

usage_reporting:
  quota_snapshot: ENABLED|OPTIONAL|DISABLED
  report_after_material_task: true|false
  notify_operator: true|false
  stale_after_seconds: <integer>
  never_reduce_acceptance_quality: true

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

## Recommended balanced default

```yaml
agent_mutation_policy:
  mode: STRICT_PREVIEW
  group_related_changes_into_batches: true
  require_current_vs_proposed_state: true
  require_planned_checks_before_apply: true
  require_rollback_for_material_changes: true
  remediation_windows:
    enabled: true
    default_max_iterations: 2
    manager_review_required_before_closure: true

workspace_safety:
  preserve_unknown_dirty_work: true
  destructive_git_requires_explicit_authority: true

external_effects:
  real_provider_calls: EXPLICIT_AUTHORITY_REQUIRED
  paid_api_calls: EXPLICIT_AUTHORITY_REQUIRED
  message_or_notification_sends: EXPLICIT_AUTHORITY_REQUIRED

review_policy:
  pre_manager_adversarial_review: REQUIRED_FOR_MEDIUM_HIGH
  consolidated_manager_findings: true
  independent_closure: REQUIRED_FOR_HIGH

flow_metrics:
  enabled: true
  collect_material_tasks_only: true

production_mode:
  enabled: false
  rollback_or_forward_recovery_required_for_every_mutation: true
  require_abort_condition: true
  require_post_change_verification: true
  irreversible_change:
    require_forward_recovery_plan: true
    require_backup_or_checkpoint: true
    require_blast_radius_control: true
```

This keeps first mutation approval explicit while allowing bounded same-task remediation after a consolidated review.

## Production-mode rule

When `production_mode.enabled: true`, a production mutation is not execution-ready until the specific change has an executable rollback path or an explicit forward-recovery plan. The change must also define the target, success/health signals, abort condition, stateful/data constraints, recovery authority and post-change verification.

For irreversible changes, `rollback: impossible` is not enough. Record why rollback is unsafe/impossible and require forward recovery, backup/checkpoint evidence when applicable, controlled blast radius and STOP conditions.

Production mode never converts `production_mutation: OWNER_APPROVAL` into automatic authority.
