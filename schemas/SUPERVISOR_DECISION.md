# Supervisor Decision Schema

Every material supervisor decision should be durable and structured.

```yaml
decision_id: <stable-id>
task_id: <task-id>
review_mode: DIRECT_ACCESS|EVIDENCE_ONLY
reviewer_identity: <human/model/session/harness identity>
reviewed_contract_ref: <path/hash/version>
reviewed_head_ref: <commit/ref or UNAVAILABLE>

decision: ACCEPT_DRAFT|AMEND_DRAFT|REJECT_DRAFT|NEEDS_EVIDENCE|ACCEPT_CLOSURE|AMEND_SAME_TASK|CREATE_BOUNDED_FOLLOWUP|NO_SAFE_PATH

claim_findings:
  - claim_id: C1
    status: VERIFIED|CONTRADICTED|UNVERIFIED|VERIFIED_FROM_PACKET|CONTRADICTED_BY_PACKET|UNVERIFIED_FROM_PACKET
    evidence_refs: [E1]

required_amendment:
  scope: <bounded change or NONE>
  required_tests: []
  required_evidence: []

residual_risk: []
next_step: <exact authorized next action>
```

A supervisor decision grants only the authority explicitly defined by the project/owner workflow. A model cannot create owner-only production authority by writing this file.
