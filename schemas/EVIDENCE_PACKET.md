# Evidence Packet Schema

**Schema version:** 1.1  
**Updated:** 2026-09-09T10:04:00Z

Use this packet for handoff to a supervisor, especially when the supervisor has no direct repository access.

```yaml
packet_id: <stable-id>
task_id: <task-id>
contract_ref: <path/hash/version>
classification_ref: <path/hash/version>
report_ref: <schemas/STATUS_REPORT.md-conformant report or NONE>

identity:
  repository: <owner/repo or local identity>
  base_ref: <commit/ref>
  head_ref: <commit/ref>
  working_tree_state: CLEAN|DIRTY|UNKNOWN
  artifact_ref: <image/build/hash or NONE>
  environment: <local/testenv/staging/prod identity or NONE>
  verified_at: <RFC3339>

claims:
  - id: C1
    statement: <exact bounded claim submitted for judgment>
    claim_kind: <schemas/CLAIM_RECEIPT.md kind>
    truth_class: OBSERVED|DERIVED|INFERRED|UNKNOWN|CONTRADICTED
    verification_status: VERIFIED|PARTIAL|UNVERIFIED|CONTRADICTED
    minimum_receipt: <required rung>
    evidence_refs: [E1, E2]
    validity_boundary: <ref/artifact/environment/method scope>

changes:
  paths: [<path>]
  diff_artifact: <path/url/hash or NONE>
  unexpected_paths: [<path or NONE>]

evidence:
  - id: E1
    type: IDENTITY|STATIC|BUILD|FOCUSED_TEST|PATH_PROOF|INTEGRATION_CONTRACT|LIVE_BEHAVIOR|DEPLOYED_ARTIFACT|EXHAUSTIVE_BOUNDED_NEGATIVE|EXTERNAL_PRIMARY|JUDGMENT
    command_or_source: <exact command/source/method>
    result: PASS|FAIL|PARTIAL|SKIPPED|OBSERVED
    bounded_result: <concise result; preserve counts>
    artifact_ref: <path/hash/url>
    repository_ref: <commit/ref or NONE>
    environment: <identity or NONE>
    observed_at: <RFC3339>
    independently_reproducible: true|false
    method_boundary: <what this receipt does and does not establish>

checks:
  executed:
    - <exact check + result/ref>
  not_executed:
    - check: <important omitted check>
      reason: <reason>

dod_matrix:
  - dod_id: D1
    status: PASS|FAIL|PARTIAL|UNVERIFIED
    evidence_refs: [E1]

known_failures:
  - <exact failure, baseline/new status, disposition>
unexpected_findings:
  - <finding and scope relation>
unresolved:
  - <fact still unknown>
residual_risk:
  - <risk that remains after performed checks>
executor_statement:
  requested_decision: ACCEPT_CLOSURE|AMEND_SAME_TASK|CREATE_BOUNDED_FOLLOWUP|NO_SAFE_PATH|NEEDS_EVIDENCE
```

## Integrity rules

- Do not include private chain-of-thought. Include observable receipts and concise rationale only.
- Bind material evidence to the exact repository/artifact/environment identity it describes.
- Preserve `SKIPPED`/`PARTIAL`/`UNVERIFIED`; do not normalize them into PASS.
- `JUDGMENT` is evidence that a reviewer made a decision, not evidence that underlying runtime behavior occurred.
- For a claim requiring a stronger verification rung than the packet contains, mark it PARTIAL/UNVERIFIED rather than relying on narrative confidence.
- Evidence collected before a later material mutation is stale unless its continued validity is explicitly established.
- Negative/global claims follow `schemas/CLAIM_RECEIPT.md`: define the finite universe/exhaustive method or narrow the wording.
