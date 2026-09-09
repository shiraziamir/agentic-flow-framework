# Task Contract Schema

**Schema version:** 1.1  
**Updated:** 2026-09-09

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
scope:
  edit: [<paths/modules>]
  reference: [<paths/modules>]
  exclude: [<paths/modules>]
baseline:
  - <checks that must still pass>
uncertainties:
  - <facts to resolve before mutation>
definition_of_done:
  - id: D1
    requirement: <observable completion condition>
required_evidence:
  - <receipt>
stop_conditions:
  - <condition that forbids improvisation>
escalation_conditions:
  - <condition requiring stronger judgment or higher governance>
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
content_hash: <hash/ref when frozen|null>
```

Governance defaults:

- `HIGH`: architecture/persistence/production/security/public-contract or otherwise high-impact work. Full draft → review → freeze → separate apply → independent closure.
- `MEDIUM`: bounded same-task correction. Prefer an approved `schemas/AMENDMENT.md` artifact rather than restarting the whole lifecycle.
- `EVIDENCE_ONLY`: docs/evidence/test-contract correction with no new runtime authority. Durable owner-approved amendment + hash/ref is normally sufficient.

Budget fields are optional. They make spend/context visible; they never authorize lowering the acceptance bar. Unknown usage stays unknown.
