# Task Contract Schema

**Schema version:** 1.5  
**Updated:** 2026-09-13

A portable material task contract should contain the following fields. Keep it concise; the contract defines authority, success and evidence boundaries, not every implementation detail.

```yaml
task_id: <stable-id>
version: <integer or semver>
created_at: <RFC3339>
updated_at: <RFC3339>
status: DRAFT|FROZEN|AUTHORIZED|IN_PROGRESS|EVIDENCE_READY|CLOSED|BLOCKED

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

budget:
  soft_input_tokens: <integer|null>
  hard_input_tokens: <integer|null>
  soft_cost_usd: <number|null>
  hard_cost_usd: <number|null>
  warn_on_waste: true
  quality_may_be_reduced_for_budget: false

content_hash: <hash/ref when frozen|null>
```

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

Legacy `governance` remains readable for migration but new profiles/tasks should prefer the two-dimensional form.

## Draft-review rule

A material draft is reviewed before APPLY for:

1. risk/work-kind classification;
2. observable goal/DoD;
3. scope and STOP boundaries;
4. claim → minimum receipt mapping;
5. triggered failure surfaces;
6. environment/real-boundary readiness;
7. security/data/operations implications;
8. intentionally omitted checks;
9. need for cold/adversarial and independent review;
10. bounded authority and external-side-effect permissions.

Acceptance freezes the contract; it does not itself authorize APPLY unless project policy explicitly combines those gates.

## Risk-adaptive defaults

- `LOW`: focused execution/test/review; avoid high-risk ceremony.
- `MEDIUM`: short preflight, bounded execution, cold review, same-task remediation where possible.
- `HIGH`: frozen contract, explicit initial authorization, broad failure-surface review, exact evidence, Manager review and independent closure when required.

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

`flow_metrics` are used to improve the harness, not score individuals. Their purpose is to separate genuine quality cost from agent defects, governance friction and environment friction.

Budget and quota information are also telemetry. They never authorize lowering the acceptance bar.
