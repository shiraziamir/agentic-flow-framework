# Task Contract Schema

A portable task contract should contain:

```yaml
task_id: <stable-id>
status: DRAFT|FROZEN|AUTHORIZED|IN_PROGRESS|EVIDENCE_READY|CLOSED|BLOCKED
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
  - <condition requiring stronger judgment>
skills:
  selected: [<canonical-skill-id>]
supervision:
  draft_review_required: true
  closure_review_required: true
```

A frozen contract is immutable except through explicit amendment. Drafting the task does not authorize execution.
