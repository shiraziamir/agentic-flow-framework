# Evidence Packet Schema

Use this packet for handoff to a supervisor, especially when the supervisor has no direct repository access.

```yaml
packet_id: <stable-id>
task_id: <task-id>
contract_ref: <path/hash/version>
repository: <owner/repo or local identity>
base_ref: <commit/ref>
head_ref: <commit/ref>

claims:
  - id: C1
    statement: <exact claim submitted for judgment>
    evidence_refs: [E1, E2]

changes:
  paths: [<path>]
  diff_artifact: <path/url/hash or NONE>

evidence:
  - id: E1
    type: STATIC|TEST|LIVE|MUTATION|EXTERNAL
    command_or_source: <exact command/source>
    result: <bounded result>
    artifact_ref: <path/hash/url>
    independently_reproducible: true|false

dod_matrix:
  - dod_id: D1
    status: PASS|FAIL|PARTIAL|UNVERIFIED
    evidence_refs: [E1]

known_failures:
  - <exact failure, baseline status, disposition>
unresolved:
  - <fact still unknown>
residual_risk:
  - <risk that remains>
executor_statement:
  requested_decision: ACCEPT_CLOSURE|AMEND_SAME_TASK|...
```

Do not include private chain-of-thought. Include observable receipts and concise rationale only.
