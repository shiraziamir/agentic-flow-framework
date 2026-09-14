# Project Profile Config Schema

**Schema version:** 2.0  
**Updated:** 2026-09-14

A target project should keep one durable profile at `.agentic/PROJECT_PROFILE.yaml`. The profile declares intended operating policy; current receipts establish reality.

The profile is deliberately split into two layers:

```text
OPERATING PRESET
→ sane defaults

PROJECT OVERRIDES
→ only what this project actually needs to differ
```

Do not copy every possible option into a real project unless it is needed.

## 1. Operating presets

```yaml
operating_preset: VIBE_FAST|PRODUCT_STANDARD|HIGH_ASSURANCE
```

### `VIBE_FAST`

Use for deliberate experiments/prototypes. Defaults favor learning speed, sacrificial code and compact review. It never grants sensitive-data authority, production-readiness claims or production mutation.

### `PRODUCT_STANDARD`

Default for maintainable product work. Uses Product Inception when needed, risk-adaptive Dual-Lens review, real-enough verification, bounded remediation and explicit production recovery.

### `HIGH_ASSURANCE`

Use when money, identity, privacy, tenant isolation, critical durability, destructive operations, regulated data or high-consequence production behavior requires stronger review/evidence by default.

Presets are convenience, not authority. Explicit task/environment/external-effect/production controls still apply.

## 2. Recommended minimal real-project profile

Most projects should start closer to this than to the full reference schema:

```yaml
profile_version: 2
project_id: <stable-id>
updated_at: <RFC3339>
operating_preset: PRODUCT_STANDARD

project_mode:
  mode: PRODUCT_BUILD

codebase_scale: SMALL|MEDIUM|LARGE
readiness_tier: BASIC|STANDARD|HIGH_ASSURANCE

project_traits:
  stateful: true|false
  tenant_scoped: true|false
  privacy_sensitive: true|false
  cost_sensitive: true|false
  production_bound: true|false

# Only declare overrides that differ from the preset.
overrides: {}
```

The effective configuration is:

```text
preset defaults
+ explicit project traits
+ explicit overrides
+ current task authority
```

Task authority never comes from a preset alone.

## 3. Full reference shape

```yaml
profile_version: 2
project_id: <stable-id>
updated_at: <RFC3339>
operating_preset: VIBE_FAST|PRODUCT_STANDARD|HIGH_ASSURANCE

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

project_traits:
  stateful: true|false
  tenant_scoped: true|false
  privacy_sensitive: true|false
  cost_sensitive: true|false
  production_bound: true|false

task_focus_policy:
  require_single_primary_task: true|false
  side_task_max_rounds_without_focus_review: <integer>
  side_task_may_redefine_primary_objective: false
  side_task_promotion: MANAGER_OR_OPERATOR_DECISION|PROJECT_DEFINED
  interrupt_requires_primary_checkpoint: true|false
  resume_primary_after_side_or_interrupt_by_default: true|false

swamp_guard:
  enabled: true|false
  repeated_remediation_alert_after: <integer>
  require_eval_before_ai_rag_tuning: true|false
  require_vertical_slice_before_broad_feature_growth: true|false
  require_rebaseline_for_vibe_to_product: true|false
  stop_on_source_of_truth_ambiguity: true|false
  watch_on_side_task_attention_drift: true|false
  watch_on_repeated_system_lens_open_risk: true|false

dual_lens:
  enabled: true|false
  low_risk_mode: COMPACT_IMPACT_SUMMARY|FULL_MATRIX
  require_system_truth_map_for_product_build: true|false
  require_data_authority_map_when_stateful_or_cost_sensitive: true|false
  require_explicit_matrix_for_medium_high: true|false
  force_explicit_dimensions_for_sensitive_boundaries: true|false
  require_behavior_scenarios_for_material_business_logic: true|false
  require_mutation_or_path_proof_for_load_bearing_tests: true|false
  system_effect_states: [UNAFFECTED, VERIFIED, CHANGED_AND_TESTED, OPEN_RISK, NOT_APPLICABLE]
  cross_system_audit:
    enabled: true|false
    trigger_precedence: EVENT_THEN_RISK_THEN_COUNT
    material_task_interval: <integer|null>
    recommended_interval_range: <string|null>
    before_demo_deployment: true|false
    before_real_customer_release: true|false
    after_material_incident: true|false
    before_or_after_material_authority_change: true|false

scale_boundaries:
  require_current_target: true|false
  require_expected_load_or_unknown: true|false
  require_known_ceiling_or_unknown: true|false
  require_hard_safety_limit_for_unbounded_resources: true|false
  require_failure_behavior: true|false
  require_scale_up_trigger: true|false

quality:
  test_strategy: RISK_BASED|TEST_FIRST_FOR_MATERIAL_CLAIMS|TDD_STRICT
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
    production_mutation: DENIED
  designer:
    source: READ_ONLY|PROJECT_DEFINED
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
  require_primary_task_ref: true
  require_active_task_role: true
  require_resume_checkpoint_for_interrupt: true
  require_current_repository_ref: true
  require_system_truth_map_ref_when_applicable: true|false
  require_system_lens_open_risks: true|false
  session_reset_after_durable_checkpoint: ALLOWED|PROJECT_DEFINED

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

architecture_policy:
  pattern_mode: AGENT_PROPOSES_OWNER_MAY_OVERRIDE|OWNER_SPECIFIES|AGENT_AUTONOMOUS_WITHIN_GUARDRAILS
  require_rationale_for_new_abstraction: true
  avoid_pattern_without_boundary_or_failure_mode: true
  freeze_hard_to_change_invariants_not_easy_choices: true

temporary_overrides:
  directory: .agentic/overrides
  require_expiry: true
  require_owner: true
  require_reason: true
  require_compensating_control: true
```

## 4. Preset defaults

### `VIBE_FAST`

```yaml
project_mode:
  mode: VIBE_PROTOTYPE

dual_lens:
  enabled: true
  low_risk_mode: COMPACT_IMPACT_SUMMARY
  require_explicit_matrix_for_medium_high: false

review_policy:
  pre_manager_adversarial_review: OPTIONAL
  independent_closure: DISABLED

agent_mutation_policy:
  mode: MATERIAL_CHANGES_ONLY
```

Production/sensitive-data/external-effect authority remains separately controlled.

### `PRODUCT_STANDARD`

```yaml
project_mode:
  mode: PRODUCT_BUILD

task_focus_policy:
  require_single_primary_task: true
  side_task_max_rounds_without_focus_review: 3
  side_task_may_redefine_primary_objective: false
  side_task_promotion: MANAGER_OR_OPERATOR_DECISION
  interrupt_requires_primary_checkpoint: true
  resume_primary_after_side_or_interrupt_by_default: true

swamp_guard:
  enabled: true
  repeated_remediation_alert_after: 2
  require_eval_before_ai_rag_tuning: true
  require_vertical_slice_before_broad_feature_growth: true
  require_rebaseline_for_vibe_to_product: true
  stop_on_source_of_truth_ambiguity: true
  watch_on_side_task_attention_drift: true
  watch_on_repeated_system_lens_open_risk: true

dual_lens:
  enabled: true
  low_risk_mode: COMPACT_IMPACT_SUMMARY
  require_system_truth_map_for_product_build: true
  require_data_authority_map_when_stateful_or_cost_sensitive: true
  require_explicit_matrix_for_medium_high: true
  force_explicit_dimensions_for_sensitive_boundaries: true
  require_behavior_scenarios_for_material_business_logic: true
  require_mutation_or_path_proof_for_load_bearing_tests: true
  system_effect_states: [UNAFFECTED, VERIFIED, CHANGED_AND_TESTED, OPEN_RISK, NOT_APPLICABLE]
  cross_system_audit:
    enabled: true
    trigger_precedence: EVENT_THEN_RISK_THEN_COUNT
    material_task_interval: 6
    recommended_interval_range: "5-8"
    before_demo_deployment: true
    before_real_customer_release: true
    after_material_incident: true
    before_or_after_material_authority_change: true

agent_mutation_policy:
  mode: STRICT_PREVIEW
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
  multi_model_agreement_upgrades_evidence: false

production_mode:
  enabled: false
  rollback_or_forward_recovery_required_for_every_mutation: true
  require_abort_condition: true
  require_post_change_verification: true
```

### `HIGH_ASSURANCE`

Start from `PRODUCT_STANDARD`, then prefer `readiness_tier: HIGH_ASSURANCE`, explicit threat/failure modeling, stronger environment receipts, explicit affected System-Lens dimensions, independent closure for material high-consequence work, and tighter production/change authority. Do not expand ceremony for unrelated low-risk docs/local changes.

## 5. Dual-Lens rule

`LOW` local-only work uses a compact System-Lens impact summary unless sensitive dimensions are plausibly affected. `MEDIUM/HIGH` material work records relevant matrix dimensions explicitly. Any risk level touching money, privacy, identity, tenant isolation, durability/recovery, destructive state or production semantics uses explicit affected dimensions.

A cache/projection/summary/metric cannot silently become authoritative business truth. `OPEN_RISK` remains visible until resolved, accepted or deliberately deferred.

## 6. Cross-system audit rule

Trigger precedence is:

```text
EVENT TRIGGER
> RISK / AUTHORITY TRIGGER
> TASK-COUNT REMINDER
```

The default `material_task_interval: 6` is only a reminder within the heuristic 5–8 range. A material incident or authority/security/data/recovery change can trigger an audit immediately; a run of harmless docs tasks does not force a meaningless audit.

## 7. Task focus, handoff and production

One durable primary task exists per workstream. Side tasks do not become primary through recency or conversation length. Promotion requires explicit Manager/Operator decision. Interrupts checkpoint and later resume the previous primary task unless reprioritization is explicit.

Repository artifacts carry engineering state; humans carry authority decisions. Production mutation is never implied by a preset, reviewer PASS or task closure and always requires rollback or explicit forward-recovery readiness.
