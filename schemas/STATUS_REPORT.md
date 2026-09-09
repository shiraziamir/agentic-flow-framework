# Reality-Reflecting Status Report

**Schema version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for executor completion reports, closure packets, release notes, and any engineering status where overclaiming would matter.

```yaml
report_id: <stable-id>
task_id: <task-id>
report_version: <version>
generated_at: <RFC3339>
repository_ref: <commit/ref>
artifact_ref: <build/image/hash or NONE>
environment: <identity or NONE>
classification_ref: <change classification ref>

claims:
  - claim_id: C1
    statement: <bounded claim>
    truth_class: OBSERVED|DERIVED|INFERRED|UNKNOWN|CONTRADICTED
    verification_status: VERIFIED|PARTIAL|UNVERIFIED|CONTRADICTED
    evidence_refs: [E1]
    validity_boundary: <where/when this remains true>

checks:
  executed:
    - command_or_method: <exact check>
      result: PASS|FAIL|PARTIAL|SKIPPED
      evidence_ref: <ref>
  not_executed:
    - <important check intentionally/not-available, with reason>

unexpected_findings:
  - <finding and disposition>
known_failures:
  - <failure and whether baseline/new>
unresolved:
  - <unknown fact>
residual_risk:
  - <risk not eliminated by performed checks>
next_state: EVIDENCE_READY|BLOCKED|AMENDMENT_REQUIRED|...
```

## Reporting rules

1. Lead with identity: what ref/artifact/environment was actually checked.
2. Report exact counts (`M/N`) and exact check scope. Never collapse partial/skipped/unexecuted checks into `all passed`.
3. Separate `OBSERVED`, `DERIVED`, `INFERRED`, `UNKNOWN`, and `CONTRADICTED` statements.
4. A reviewer/model judgment is reported as judgment, not as direct runtime evidence.
5. State material checks that were **not** run. Silence is not equivalent to coverage.
6. If CI is green, report which relevant jobs/checks actually executed and which were skipped/neutral when that distinction matters.
7. Do not report `no regressions`, `secure`, `production-ready`, `fully tested`, or equivalent global language unless the claim universe and verification method justify it.
8. If an exact acceptance gate was replaced with a proxy, report `PARTIAL/UNVERIFIED` unless the task was explicitly amended.
9. New mutations after verification invalidate stale report evidence according to `schemas/CLAIM_RECEIPT.md`.

## Preferred human-readable shape

```text
Identity
Observed changes
Verified claims (claim -> receipt)
Checks executed
Important checks not executed
Failures / unexpected findings
Unknowns / residual risk
Requested supervisor decision / next state
```

The report should describe reality at a bounded point in time, not sell completion.
