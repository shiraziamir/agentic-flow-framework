# Supervisor Decision Schema

**Schema version:** 1.1  
**Updated:** 2026-09-09T10:04:00Z

Every material supervisor decision should be durable, bounded and tied to the exact work/evidence it judged.

```yaml
decision_id: <stable-id>
task_id: <task-id>
decision_version: <version>
created_at: <RFC3339>

review_mode: DIRECT_ACCESS|EVIDENCE_ONLY
independence_level: SELF_REVIEW|COLD_SAME_MODEL|COLD_DIFFERENT_MODEL_OR_HUMAN
reviewer_identity: <human/model/session/harness identity>

reviewed_contract_ref: <path/hash/version>
reviewed_classification_ref: <path/hash/version>
reviewed_evidence_packet_ref: <path/hash/version or NONE>
reviewed_status_report_ref: <path/hash/version or NONE>
reviewed_head_ref: <commit/ref or UNAVAILABLE>
reviewed_artifact_ref: <build/image/hash or NONE>
reviewed_environment: <identity or NONE>

review_scope:
  verification_profiles: [<profiles/annexes>]
  checks_performed: [<falsifying/spot checks or NONE>]
  checks_not_performed: [<important limitations>]

decision: ACCEPT_DRAFT|AMEND_DRAFT|REJECT_DRAFT|NEEDS_EVIDENCE|ACCEPT_CLOSURE|AMEND_SAME_TASK|CREATE_BOUNDED_FOLLOWUP|NO_SAFE_PATH

claim_findings:
  - claim_id: C1
    status: VERIFIED|PARTIAL|CONTRADICTED|UNVERIFIED|VERIFIED_FROM_PACKET|PARTIAL_FROM_PACKET|CONTRADICTED_BY_PACKET|UNVERIFIED_FROM_PACKET
    evidence_refs: [E1]
    finding: <bounded rationale>
    validity_boundary: <what the judgment actually covers>

required_amendment:
  scope: <bounded change or NONE>
  reclassification: <required surface/flags or NONE>
  required_tests: []
  required_evidence: []

residual_risk: []
access_limitations: []
next_step: <exact authorized next action>
```

## Rules

- A closure decision is valid only for the contract/classification/head/artifact/environment it identifies.
- Later material mutation does not inherit an older `ACCEPT_CLOSURE`; re-verification/review is required unless continued validity is explicitly established.
- A supervisor decision is a `JUDGMENT` receipt. It proves that the review occurred and what was decided; it does not replace missing runtime, persistence, deployment, contract or security receipts.
- Evidence-only review must preserve packet limitations (`PARTIAL_FROM_PACKET` / `UNVERIFIED_FROM_PACKET`) rather than converting them into direct verification.
- The supervisor grants only the authority explicitly defined by the owner/project workflow. A model cannot create owner-only production authority by writing this file.
