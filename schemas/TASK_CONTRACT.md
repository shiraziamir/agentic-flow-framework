# Task Contract Schema

**Schema version:** 1.4  
**Updated:** 2026-09-09T17:22:00+03:30

A portable material task contract should contain:

```yaml
task_id: <stable-id>
version: <integer or semver>
created_at: <RFC3339>
updated_at: <RFC3339>
status: DRAFT|FROZEN|AUTHORIZED|IN_PROGRESS|EVIDENCE_READY|CLOSED|BLOCKED
governance: HIGH|MEDIUM|EVIDENCE_ONLY

goal: <observable owner outcome>
symptom: <what is actually observed>
hypotheses:
  - <theory, explicitly not fact>

classification:
  ref: <schemas/CHANGE_CLASSIFICATION.md-conformant artifact/ref>
  primary_surface: FRONTEND|BACKEND|SHARED|DATA|INFRA|CI_CD|TOOLING|DOCS_EVIDENCE
  change_kind: <kind>
  cross_cutting_flags: [<flags>]
  operational_flags: [<flags>]
  runtime_mutation_scope: NONE|LOCAL|TESTENV|PRODUCTION
  affected_consumers: [<consumer>]
  verification_profiles: [GENERAL, <selected profiles>]

production:
  profile_ref: <schemas/PRODUCTION_PROFILE.md artifact/ref|NONE>
  readiness_tier: BASIC|STANDARD|HIGH_ASSURANCE|NOT_APPLICABLE|UNKNOWN
  profiles_affected: [DELIVERY, OBSERVABILITY, DATA_DURABILITY, TROUBLESHOOTING, SECURITY_FIRST, AI_LOG_ANALYSIS, RESILIENCE_CHAOS, CODE_ARCHITECTURE]
  known_gap_refs: []
  creates_or_changes_operational_gap: true|false

scope:
  edit: [<paths/modules>]
  reference: [<paths/modules>]
  exclude: [<paths/modules>]

baseline:
  - <check/behavior known before mutation>
uncertainties:
  - <fact to resolve before mutation>

definition_of_done:
  - id: D1
    requirement: <observable completion condition>

planned_claims:
  - id: C1
    statement: <bounded closure claim>
    claim_kind: <schemas/CLAIM_RECEIPT.md kind>
    minimum_receipt: <required verification rung>

required_evidence:
  - <receipt, with ref/artifact/environment identity where relevant>
important_checks_not_required:
  - check: <material check intentionally outside task>
    reason: <why>

stop_conditions:
  - <condition that forbids improvisation>
escalation_conditions:
  - <condition requiring stronger judgment, higher governance, reclassification or readiness review>

authorization:
  apply_authorization_ref: <ref|null>
  execution_limit: <integer|unbounded|null>
  consumed_on_attempt: true|false|null
  attempts_used: <integer|null>
  rerun_requires_new_authorization: true|false|null

measurement_qualification:
  required: true|false
  policy_ref: schemas/EVIDENCE_RECOVERY.md
  repository_ref_required: true|false
  runtime_artifact_identity_required: true|false
  environment_identity_required: true|false
  writable_path_isolation_required: true|false
  baseline_ref: <ref|null>
  forbidden_preconditioning: []
  invalid_evidence_disposition: VALID_FOR_CLAIM|PARTIAL_FOR_CLAIM|VOID_FOR_CLAIM|HISTORICAL_ONLY|UNKNOWN|null

skills:
  selected: [<canonical-skill-id>]
routing:
  expected_roles:
    discovery: T0|T1|T2|T3
    execution: T0|T1|T2|T3
    closure: T0|T1|T2|T3
budget:
  soft_input_tokens: <integer|null>
  hard_input_tokens: <integer|null>
  soft_cost_usd: <number|null>
  hard_cost_usd: <number|null>
  warn_on_waste: true
  quality_may_be_reduced_for_budget: false
supervision:
  draft_review_required: true|false
  closure_review_required: true|false
  independent_closure_required: true|false
  blind_spot_audit_required: true|false
content_hash: <hash/ref when frozen|null>
```

## Draft-review rule

A material DRAFT is reviewed **before APPLY** for:

1. correct governance and engineering surface/risk classification;
2. observable goal/DoD rather than implementation-only wording;
3. affected consumers/scope and STOP boundaries;
4. planned claim → minimum receipt mapping;
5. surface-specific verification/cross-cutting annexes;
6. production-readiness impacts for any production-capable project;
7. build/deploy/observability/security/data/recovery implications triggered by the change;
8. meaningful negative/error/security/persistence/live paths where applicable;
9. important checks intentionally omitted;
10. whether a separate/cold closure reviewer is required;
11. whether the planned evidence run itself needs runtime/environment/baseline qualification;
12. whether bounded execution authority is single-use and what consumes it.

The draft reviewer may return `ACCEPT_DRAFT`, `AMEND_DRAFT`, `NEEDS_EVIDENCE`, or `REJECT_DRAFT`. Acceptance freezes the contract; it does not itself authorize APPLY unless the active governance explicitly combines those gates.

## Evidence-environment recovery rule

Use `schemas/EVIDENCE_RECOVERY.md` when the evidence run may depend on a deployed/runtime artifact, shared/test environment, mutable baseline, provider budget/state, or host-side writable paths.

If a run executes against the wrong/stale runtime or otherwise cannot measure the intended claim:

- preserve the run as historical evidence;
- classify it explicitly, including `VOID_FOR_CLAIM` where appropriate;
- do not overwrite it with a rerun;
- classify whether the defect belongs to implementation, evidence environment, baseline, authorization, or a mixture;
- treat a finite/single-run authorization as consumed on attempt unless the durable authorization says otherwise;
- obtain new authorization for a rerun or new rebuild/restart/mutation scope when required;
- qualify the repaired measuring environment before spending provider calls or running the fresh live evidence sequence.

Fixing the measuring instrument can remain a same-task recovery when product design/source does not need to change. Do not silently widen a verification recovery into implementation scope.

## Capability-maturity wording

Do not collapse these into one completion claim:

```text
DESIGNED
IMPLEMENTED_IN_SOURCE
MECHANICALLY_TESTED
QUALIFIED_IN_NAMED_ENVIRONMENT
LIVE_BEHAVIOR_PROVEN
DEPLOYED_ARTIFACT_PROVEN
PRODUCTION_BEHAVIOR_PROVEN
```

A task may legitimately close with some higher states unproven when they are outside its frozen contract. Report the boundary explicitly.

## Production-readiness rule

For a project intended to run in production:

- use a current `schemas/PRODUCTION_PROFILE.md` or report the missing profile as `UNKNOWN/UNVERIFIED` rather than assuming readiness;
- a change that introduces a new database, queue, external provider, privileged path, public endpoint, deployment mechanism, telemetry path or durable data can create new production requirements;
- material missing/partial/unverified capabilities become `schemas/OPERATIONAL_GAP.md` artifacts with owner/risk/closure requirements;
- production readiness is not a per-task boolean: closure states what this task verified/changed and what gaps remain.

## Governance defaults

- `HIGH`: architecture/persistence/production/security/public-contract or otherwise high-impact work. Full draft → review → freeze → separate apply → independent closure.
- `MEDIUM`: bounded same-task correction. Prefer an approved amendment rather than restarting the whole lifecycle.
- `EVIDENCE_ONLY`: docs/evidence/test-contract correction with no new runtime authority. Durable owner-approved amendment + hash/ref is normally sufficient.

If APPLY discovers a new material primary/consumer surface, operational risk or readiness requirement not represented by the frozen classification/verification/production plan, STOP and amend rather than silently widening scope or weakening evidence.

Budget fields are optional. They make spend/context visible; they never authorize lowering the acceptance bar. Unknown usage stays unknown.
