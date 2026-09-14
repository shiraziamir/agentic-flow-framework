# Reality-Reflecting Status Report

**Schema version:** 1.2  
**Updated:** 2026-09-14

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
system_truth_map_ref: <ref or NONE>

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

mutation_or_path_proof:
  performed: true|false
  mutations_caught: []
  mutations_survived_or_not_tested: []

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

external_effects:
  environment_mutations: []
  provider_calls: []
  observed_or_billed_spend: <value|UNKNOWN|NOT_APPLICABLE>

rollback_or_recovery:
  applicable: true|false
  ref_or_summary: <ref|summary|NOT_APPLICABLE>

usage_quota: <optional schemas/USAGE_QUOTA_SNAPSHOT.md object or null>

unexpected_findings:
  - <finding and disposition>
known_failures:
  - <failure and whether baseline/new>
unresolved:
  - <unknown fact>
residual_risk:
  - <risk not eliminated by performed checks>
next_state: EVIDENCE_READY|BLOCKED|AMENDMENT_REQUIRED|...
next_authorized_action: <action/ref|NONE>
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
10. For material changes, report the System-Lens effect matrix. `OPEN_RISK` stays visible; `UNAFFECTED` is a reviewed conclusion, not a default.
11. For load-bearing tests, report mutation/path proof when required, including target defects that were caught or survived.
12. Report real provider calls, external effects, environment mutations and spend/accounting observations separately from code-test results.
13. Report rollback/recovery readiness when the change can affect an environment or durable state.
14. If quota reporting is enabled, append one compact `usage_quota` snapshot after a material task/checkpoint using `schemas/USAGE_QUOTA_SNAPSHOT.md`; quota telemetry is not engineering evidence.
15. Missing/stale quota telemetry is reported explicitly and must never be fabricated.

## Preferred human-readable shape

```text
Identity
What changed
Why it is correct / bounded claims
Checks executed
Mutation/path proof caught
Important checks not executed
Cross-system effects / OPEN_RISKs
Failures / unexpected findings
Environment mutations / provider calls / spend
Rollback or recovery
Unknowns / residual risk
Usage quota (optional)
Next authorized action / requested supervisor decision
```

The report should describe reality at a bounded point in time, not sell completion.