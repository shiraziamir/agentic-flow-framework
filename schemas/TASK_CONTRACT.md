# Task Contract Schema

**Schema version:** 1.7  
**Updated:** 2026-09-14

A portable material task contract should contain the following fields. Keep it concise; the contract defines authority, success, priority and evidence boundaries, not every implementation detail.

```yaml
task_id: <stable-id>
version: <integer or semver>
created_at: <RFC3339>
updated_at: <RFC3339>
status: DRAFT|FROZEN|AUTHORIZED|IN_PROGRESS|EVIDENCE_READY|CLOSED|BLOCKED

focus:
  role: PRIMARY|SIDE|INTERRUPT
  primary_task_ref: <task-id/ref>
  parent_task_ref: <task-id/ref|null>
  reason: <why this task exists now>
  promotion_requires: MANAGER_OR_OPERATOR_DECISION
  may_redefine_primary_objective: false
  max_rounds_without_focus_review: <integer|null>
  rounds_used: <integer>
  return_condition: <when to resume/return to primary>
  resume_task_ref: <task-id/ref|null>
  resume_checkpoint_ref: <artifact/ref|null>

risk:
  level: LOW|MEDIUM|HIGH

work_kind:
  mode: IMPLEMENTATION|REMEDIATION|EVIDENCE_ONLY

# legacy compatibility only; prefer risk + work_kind above
governance: HIGH|MEDIUM|EVIDENCE_ONLY|null

goal: <observable owner outcome>
symptom: <what is actually observed>
hypotheses: []

classification:
  ref: <schemas/CHANGE_CLASSIFICATION.md artifact/ref>
  primary_surface: FRONTEND|BACKEND|SHARED|DATA|INFRA|CI_CD|TOOLING|DOCS_EVIDENCE
  change_kind: <kind>
  cross_cutting_flags: []
  operational_flags: []
  runtime_mutation_scope: NONE|LOCAL|TESTENV|PRODUCTION
  affected_consumers: []
  verification_profiles: [GENERAL]

scope:
  edit: []
  reference: []
  exclude: []

baseline: []
uncertainties: []

system_truth:
  map_ref: <schemas/SYSTEM_TRUTH_MAP.md project artifact/ref|null>
  authority_or_boundary_changes_expected: []
  scale_boundary_changes_expected: []

dual_lens:
  local_lens:
    advisory_algorithm_or_pseudocode_ref: <ref|null>
    business_invariants: []
    failure_semantics: []
    behavioral_scenarios: []
    mutation_or_path_proof_targets: []
  system_lens:
    WRITE: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    READ: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    AGGREGATE: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    CACHE: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    RESTART: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    FAILURE: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    RECOVERY: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    ADMIN: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    METRIC: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    TENANT_ISOLATION: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    SCALE: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    PRIVACY: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
    COST: UNAFFECTED|VERIFIED|CHANGED_AND_TESTED|OPEN_RISK|NOT_APPLICABLE
  open_risks: []
  system_truth_map_update_required: true|false

definition_of_done:
  - id: D1
    requirement: <observable completion condition>

planned_claims:
  - id: C1
    statement: <bounded closure claim>
    claim_kind: <schemas/CLAIM_RECEIPT.md kind>
    minimum_receipt: <required verification rung>

required_evidence: []
important_checks_not_required: []
stop_conditions: []
escalation_conditions: []

authorization:
  apply_authorization_ref: <ref|null>
  execution_limit: <integer|unbounded|null>
  consumed_on_attempt: true|false|null
  attempts_used: <integer|null>
  rerun_requires_new_authorization: true|false|null

remediation_window:
  enabled: true|false
  review_ref: <ref|null>
  finding_ids: []
  max_iterations: <integer|null>
  iterations_used: <integer>
  allowed_files_or_resources: []
  allowed_change_classes: []
  owner_review_required_before_closure: true|false

measurement_qualification:
  required: true|false
  policy_ref: schemas/EVIDENCE_RECOVERY.md
  repository_ref_required: true|false
  runtime_artifact_identity_required: true|false
  environment_identity_required: true|false
  changed_behavior_exercised: true|false|NOT_APPLICABLE
  lowest_adequate_environment: LOCAL_REAL|EPHEMERAL_TEST|SHARED_TEST|STAGING|PRODUCTION_READ|PROJECT_DEFINED
  real_boundaries_required: []
  mock_only_closure_limit: <narrow claims only; DENIED for integration-or-stronger by default>
  environment_unavailable_action: BLOCK_AND_REQUEST_ENVIRONMENT|REPORT_UNVERIFIED
  writable_path_isolation_required: true|false
  baseline_ref: <ref|null>
  forbidden_preconditioning: []
  invalid_evidence_disposition: VALID_FOR_CLAIM|PARTIAL_FOR_CLAIM|VOID_FOR_CLAIM|HISTORICAL_ONLY|UNKNOWN|null

external_effects:
  real_provider_calls: DENIED|EXPLICIT_AUTHORITY_REQUIRED|AUTHORIZED_BY_REF
  authority_ref: <ref|null>

workspace_safety:
  preserve_unknown_dirty_work: true
  destructive_git_requires_explicit_authority: true

supervision:
  draft_review_required: true|false
  pre_manager_adversarial_review_required: true|false
  closure_review_required: true|false
  independent_closure_required: true|false
  blind_spot_audit_required: true|false

flow_metrics:
  first_pass_review_passed: true|false|unknown
  remediation_iterations: <integer>
  manager_review_rounds: <integer>
  authorization_round_trips: <integer>
  unplanned_scope_escalations: <integer>
  environment_blocked: true|false
  agent_safety_incidents: <integer>
  task_cycle_time: <optional duration|null>
  side_task_focus_reviews: <integer>
  side_task_promotions: <integer>
  system_lens_open_risks: <integer>

budget:
  soft_input_tokens: <integer|null>
  hard_input_tokens: <integer|null>
  soft_cost_usd: <number|null>
  hard_cost_usd: <number|null>
  warn_on_waste: true
  quality_may_be_reduced_for_budget: false

content_hash: <hash/ref when frozen|null>
```

## Task-focus rule

Exactly one durable task is `PRIMARY` at a time for a given workstream. `SIDE` and `INTERRUPT` work remain explicitly linked to that primary task.

```text
RECENT TASK != PRIMARY TASK
LONG CONVERSATION != PROMOTION
LOCAL COMPLEXITY != PRIORITY
```

A `SIDE` task may not redefine the primary objective, broaden architecture, or consume unbounded rounds merely because it is the current conversation topic.

When a side task reaches `max_rounds_without_focus_review`, or its scope/importance materially expands:

```text
SIDE_TASK DRIFT
→ restate PRIMARY_TASK
→ report side-task result/open gap
→ choose CLOSE | DEFER | PROMOTE_PROPOSAL
```

Promotion is explicit and durable. It requires the configured Manager/Operator decision and updates the task refs before further work proceeds as primary.

An `INTERRUPT` is for urgent bounded preemption. Before execution, checkpoint the current primary task and record `resume_task_ref` + `resume_checkpoint_ref`. After the interrupt, resume the prior primary task unless an explicit reprioritization occurs.

## Dual-Lens rule

Material tasks are reviewed through both lenses:

```text
LOCAL LENS  = changed behavior correctness
SYSTEM LENS = resulting system truth
```

The task contract should expose invariants, failure semantics and behavior scenarios early enough that implementation cannot merely optimize for green tests. Advisory pseudocode is encouraged for complex MEDIUM/HIGH work when it clarifies the intended algorithm, but it remains advisory unless frozen as an invariant.

The System Lens uses the fixed matrix in the contract and `schemas/SYSTEM_TRUTH_MAP.md`. `OPEN_RISK` remains visible until resolved/accepted/deferred. A cache/projection/summary/metric cannot silently become authoritative business truth.

## Risk and work kind are different

Do not mix impact with activity type.

```text
risk.level  = consequence/uncertainty of the change
work_kind   = implementation vs remediation vs evidence-only work
```

Examples:

```text
HIGH + IMPLEMENTATION   persistence redesign
HIGH + REMEDIATION      correcting findings in a sensitive transaction path
LOW  + EVIDENCE_ONLY    fixing a broken documentation receipt
```

## Draft-review rule

A material draft is reviewed before APPLY for:

1. task focus (`PRIMARY|SIDE|INTERRUPT`) and durable primary ref;
2. risk/work-kind classification;
3. observable goal/DoD;
4. scope and STOP boundaries;
5. claim → minimum receipt mapping;
6. triggered failure surfaces;
7. Local-Lens invariants/failure semantics/behavior scenarios;
8. System-Lens effect matrix and System Truth Map impact;
9. environment/real-boundary readiness;
10. security/data/operations implications;
11. intentionally omitted checks;
12. need for cold/adversarial and independent review;
13. bounded authority and external-side-effect permissions.

Acceptance freezes the contract; it does not itself authorize APPLY unless project policy explicitly combines those gates.

## Risk-adaptive defaults

- `LOW`: focused execution/test/review; avoid high-risk ceremony.
- `MEDIUM`: short preflight, bounded execution, Dual-Lens check, cold review, same-task remediation where possible.
- `HIGH`: frozen contract, explicit initial authorization, broad failure/System-Lens review, exact evidence, Manager review and independent closure when required.

For same-task findings, prefer a controlled remediation window over restarting the lifecycle for each local fix. Remediation autonomy never authorizes scope expansion.

## Evidence and environment recovery

Use `schemas/EVIDENCE_RECOVERY.md` when evidence depends on deployed/runtime identity, shared/test environment, mutable baseline, provider budget/state or host-side writable paths.

Wrong/stale runtime evidence is preserved as historical and may be `VOID_FOR_CLAIM`; it is not silently replaced. An environment repair does not authorize unrelated product-source changes.

## Capability wording

Do not collapse:

```text
DESIGNED
IMPLEMENTED_IN_SOURCE
MECHANICALLY_TESTED
QUALIFIED_IN_NAMED_ENVIRONMENT
LIVE_BEHAVIOR_PROVEN
DEPLOYED_ARTIFACT_PROVEN
PRODUCTION_BEHAVIOR_PROVEN
```

A task can close with higher states unproven when they are outside the frozen contract. Report the boundary.

## Flow metrics are process telemetry

`flow_metrics` are used to improve the harness, not score individuals. Their purpose is to separate genuine quality cost from agent defects, governance friction, environment friction, attention drift and system-truth drift.

Budget and quota information are also telemetry. They never authorize lowering the acceptance bar.
