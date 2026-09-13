# Project Profile Config Schema

**Schema version:** 1.7  
**Updated:** 2026-09-13

A target project should keep one small durable profile, usually `.agentic/PROJECT_PROFILE.yaml`. It declares the intended operating bar; current receipts establish reality.

Recommended shape:

```yaml
profile_version: 1
project_id: <stable-id>
updated_at: <RFC3339>

project_mode:
  mode: VIBE_PROTOTYPE|PRODUCT_BUILD|MAINTENANCE
  vibe_prototype:
    sacrificial_by_default: true|false
    production_baseline: false
    sensitive_or_production_data: DENIED|OWNER_APPROVAL|PROJECT_DEFINED
    promotion_requires_rebaseline: true|false
  product_build:
    require_product_brief: true|false
    require_quality_or_eval_contract: true|false
    require_architecture_discovery: true|false
    require_walking_skeleton: true|false
    require_architecture_checkpoint: true|false

swamp_guard:
  enabled: true|false
  check_at_material_checkpoints: true|false
  states: [CLEAR, WATCH, ALERT, STOP_REBASELINE]
  repeated_remediation_alert_after: <integer>
  require_eval_before_ai_rag_tuning: true|false
  require_vertical_slice_before_broad_feature_growth: true|false
  require_decision_for_major_architecture_change: true|false
  require_rebaseline_for_vibe_to_product: true|false
  stop_on_unresolved_sensitive_data_boundary: true|false
  stop_on_source_of_truth_ambiguity: true|false

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
    maximum_without_escalation: <integer>
    extra_iteration_requires_new_material_finding: true|false
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
  independence:
    implementation: REQUIRED_FOR_INDEPENDENT_CLOSURE|PROJECT_DEFINED
    context: REQUIRED_FOR_INDEPENDENT_CLOSURE|PROJECT_DEFINED
    authority: REQUIRED_FOR_MATERIAL_WORK|PROJECT_DEFINED
    evidence: REQUIRED_FOR_INDEPENDENT_CLOSURE|PROJECT_DEFINED
    model_diversity: PREFERRED|OPTIONAL|DISABLED
  multi_model_agreement_upgrades_evidence: false

role_access:
  project_architect:
    source: READ_ONLY|PROJECT_DEFINED
    product_mutation: DENIED
    production_mutation: DENIED
  designer:
    source: READ_ONLY|PROJECT_DEFINED
    production_read: OWNER_APPROVAL|DENIED
    production_mutation: DENIED
  executor:
    source: BOUNDED_WRITE|PROJECT_DEFINED
    production_read: OWNER_APPROVAL|DENIED
    production_mutation: OWNER_APPROVAL|DENIED
  manager:
    source: READ_REVIEW|PROJECT_DEFINED
    production_read: OWNER_APPROVAL|DENIED
    production_mutation: DENIED|OWNER_APPROVAL
  independent_judge:
    source: READ_ONLY|READ_REVIEW
    production_read: OWNER_APPROVAL|DENIED
    production_mutation: DENIED

model_routing:
  vendor_neutral: true
  project_architect: HIGH_REASONING_WHEN_JUSTIFIED|PROJECT_DEFINED
  executor: TASK_ADEQUATE_COST_EFFICIENT|PROJECT_DEFINED
  manager: HIGH_REASONING_WHEN_JUSTIFIED|PROJECT_DEFINED
  independent_judge: HIGH_REASONING_SEPARATE_CONTEXT|PROJECT_DEFINED
  never_reduce_acceptance_or_evidence_for_cost: true

state_handoff:
  repository_transports_engineering_state: true
  human_transports_authority: true
  require_current_task_ref: true
  require_current_repository_ref: true
  session_reset_after_durable_checkpoint: ALLOWED|PROJECT_DEFINED

flow_metrics:
  enabled: true|false
  collect_material_tasks_only: true|false

agent_environment_policy:
  local: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  ephemeral_test: AUTO_ALLOWED|OWNER_APPROVAL|DENIED
  shared_test: OWNER_APPROVAL|AUTO_ALLOWED|DENIED
  staging: OWNER_APPROVAL|AUTO_ALLOWED|DENIED
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
  freeze_hard_to_change_invariants_not_easy_choices: true
  architecture_decisions:
    require_context_decision_consequences_revisit_trigger: true|false

temporary_overrides:
  directory: .agentic/overrides
  require_expiry: true
  require_owner: true
  require_reason: true
  require_compensating_control: true
```

## Recommended balanced default

```yaml
project_mode:
  mode: PRODUCT_BUILD
  vibe_prototype:
    sacrificial_by_default: true
    production_baseline: false
    sensitive_or_production_data: DENIED
    promotion_requires_rebaseline: true
  product_build:
    require_product_brief: true
    require_quality_or_eval_contract: true
    require_architecture_discovery: true
    require_walking_skeleton: true
    require_architecture_checkpoint: true

swamp_guard:
  enabled: true
  check_at_material_checkpoints: true
  states: [CLEAR, WATCH, ALERT, STOP_REBASELINE]
  repeated_remediation_alert_after: 2
  require_eval_before_ai_rag_tuning: true
  require_vertical_slice_before_broad_feature_growth: true
  require_decision_for_major_architecture_change: true
  require_rebaseline_for_vibe_to_product: true
  stop_on_unresolved_sensitive_data_boundary: true
  stop_on_source_of_truth_ambiguity: true

agent_mutation_policy:
  mode: STRICT_PREVIEW
  group_related_changes_into_batches: true
  require_current_vs_proposed_state: true
  require_planned_checks_before_apply: true
  require_rollback_for_material_changes: true
  remediation_windows:
    enabled: true
    default_max_iterations: 1
    maximum_without_escalation: 2
    extra_iteration_requires_new_material_finding: true
    manager_review_required_before_closure: true

review_policy:
  pre_manager_adversarial_review: REQUIRED_FOR_MEDIUM_HIGH
  consolidated_manager_findings: true
  independent_closure: REQUIRED_FOR_HIGH
  independence:
    implementation: REQUIRED_FOR_INDEPENDENT_CLOSURE
    context: REQUIRED_FOR_INDEPENDENT_CLOSURE
    authority: REQUIRED_FOR_MATERIAL_WORK
    evidence: REQUIRED_FOR_INDEPENDENT_CLOSURE
    model_diversity: PREFERRED
  multi_model_agreement_upgrades_evidence: false

role_access:
  project_architect:
    source: READ_ONLY
    product_mutation: DENIED
    production_mutation: DENIED
  executor:
    source: BOUNDED_WRITE
    production_read: OWNER_APPROVAL
    production_mutation: OWNER_APPROVAL
  manager:
    source: READ_REVIEW
    production_read: OWNER_APPROVAL
    production_mutation: DENIED
  independent_judge:
    source: READ_ONLY
    production_read: OWNER_APPROVAL
    production_mutation: DENIED

model_routing:
  vendor_neutral: true
  project_architect: HIGH_REASONING_WHEN_JUSTIFIED
  executor: TASK_ADEQUATE_COST_EFFICIENT
  manager: HIGH_REASONING_WHEN_JUSTIFIED
  independent_judge: HIGH_REASONING_SEPARATE_CONTEXT
  never_reduce_acceptance_or_evidence_for_cost: true

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

## Vibe-mode rule

`VIBE_PROTOTYPE` is a learning mode, not a production-readiness level. It may intentionally trade architecture completeness for speed, but it may not silently become the production baseline. Promotion to `PRODUCT_BUILD` requires product/architecture re-baselining and explicit classification of prototype code as reusable, review-required, rewrite, or discard.

## Swamp-Guard rule

The Swamp Guard is evaluated at material checkpoints. `WATCH` and `ALERT` surface early compounding complexity. `STOP_REBASELINE` stops broad continuation when architecture drift, unresolved data/security boundaries, source-of-truth ambiguity, eval-free AI/RAG tuning, or prototype-to-production drift would make local patches more expensive than restoring a coherent baseline.

## Independent-review rule

A second model is not automatically an independent reviewer. For independent closure, prefer separation of implementation, context, authority and evidence. Model diversity is useful defense-in-depth but does not upgrade the evidence class of the underlying receipts.

## Handoff rule

The human/operator should carry authority decisions, not routine engineering messages. Task state, reviewed refs, findings, receipts, gaps and next actions should be recoverable from durable repository artifacts so a fresh session can continue safely.

## Production-mode rule

When `production_mode.enabled: true`, a production mutation is not execution-ready until the specific change has an executable rollback path or an explicit forward-recovery plan. Production mutation remains separately owner-authorized, and the Independent Judge remains read-only by default.
