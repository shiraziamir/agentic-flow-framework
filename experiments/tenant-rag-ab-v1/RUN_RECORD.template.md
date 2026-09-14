# Run Record Template

Copy to each implementation repo as `RUN_RECORD.md` before Q01. Do not delete failed attempts. Use `UNAVAILABLE` for metrics not observable reliably.

## Run identity

```text
arm: BASELINE | AGENTIC_FLOW
model/provider:
harness/version:
machine/environment:
network policy:
framework version/ref: N/A | 1.11 + ref
started_at:
operator:
future_queue_visibility: ONE_AT_A_TIME | FULL_QUEUE_VISIBLE
```

## Per-queue record

Repeat Q01..Q12:

```text
queue_item: QNN
started_at:
finished_at:
wall_clock_seconds:
starting_head:
ending_head:
commits:
files_changed:
focused_test_runs:
full_suite_runs:
tests_final_result:
model_calls:
input_tokens:
output_tokens:
provider_cost_usd:
shell_tool_calls:
human_interventions:
clarification_requests:
review_rounds:
remediation_rounds:
authorization_round_trips:
failed_test_or_ci_iterations:
side_task_drift_event: YES|NO|N/A
swamp_state: CLEAR|WATCH|ALERT|STOP_REBASELINE|N/A
new_runtime_dependencies:
known_unverified_items:
notes:
```

## Operator intervention log

| Time | Arm | During Q | Message purpose | Identical info given to other arm? |
|---|---|---|---|---|
| | | | | |

## Final freeze receipt

```text
frozen_at:
frozen_head:
branch:
working_tree_clean: YES|NO
if_dirty_paths:
Q01_commit:
Q02_commit:
Q03_commit:
Q04_commit:
Q05_commit:
Q06_commit:
Q07_commit:
Q08_commit:
Q09_commit:
Q10_commit:
Q11_commit:
Q12_commit:
total_wall_clock_seconds:
total_model_calls:
total_input_tokens:
total_output_tokens:
total_provider_cost_usd:
total_shell_tool_calls:
total_human_interventions:
total_review_rounds:
total_remediation_rounds:
total_authorization_round_trips:
total_failed_test_or_ci_iterations:
```

## Freeze artifact counts

```text
source_file_count:
test_file_count:
doc_file_count:
runtime_dependency_count:
application_LOC:
test_LOC:
doc_LOC:
framework_control_artifact_LOC:
```

## Agent's own final assessment

```text
what_is_proven:
what_is_unverified:
known_risks:
recovery_summary:
```

No product-repo edits after frozen HEAD. If the run record must be finalized later, keep the post-freeze evaluator record outside the frozen product repository.
