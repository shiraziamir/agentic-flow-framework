# Metrics and Scoring — Pre-registered Before Execution

Do not change weights after seeing results.

## Primary outcome

Weighted escaped-defect score at the frozen HEAD. Lower is better.

```text
CRITICAL = 8
HIGH     = 5
MEDIUM   = 2
LOW      = 1
```

CRITICAL examples: cross-tenant exposure/mutation, authoritative financial corruption/unsafe overspend, destructive recovery behavior. HIGH examples: restart/durability violation, provider cost lost/double-counted, budget fail-open, deleted content still retrievable, restore failure, serious concurrency/idempotency defect.

Avoid double-counting multiple symptoms of one root cause unless impacts are independently material.

## Quality metrics

Record oracle pass rate; critical/high/medium/low findings; evidence-quality score; attention/scope score; and these 0–5 domain scores:

```text
tenant isolation
financial truth
restart/recovery
cache truth
failure semantics
concurrency/idempotency
release operability
```

0 = absent/broken, 3 = core behavior works with material gaps, 5 = no material evaluator defect within tested scope.

## Engineering-effort metrics

Per queue item and total, where observable:

```text
wall_clock_seconds
input_tokens / output_tokens
provider_cost_usd
agent_messages_or_turns
model_calls
shell_tool_calls
files_changed
commits
lines_added / lines_deleted
full_suite_runs
focused_test_runs
human_interventions
clarification_requests
remediation_rounds
review_rounds
authorization_round_trips
failed_ci_or_test_iterations
```

Unavailable metrics are `UNAVAILABLE`, never guessed.

## Process metrics

```text
tasks_completed = 0..12
first_pass_task_closures
queue_items_reopened_before_freeze
side_task_drift_events
scope_expansions_not_requested
architecture_rebaseline_events
swamp_alerts
unknowns_explicitly_reported
checks_claimed_but_not_run
post_freeze_mutations
```

## Complexity metrics at freeze

```text
source_file_count
test_file_count
doc_file_count
runtime_dependency_count
application_LOC
test_LOC
doc_LOC
framework_control_artifact_LOC
```

These explain trade-offs; more/fewer lines is not inherently better.

## Evidence-quality score 0–5

0 = mostly unsupported claims. 1 = tests exist but claims routinely exceed evidence. 2 = basic reproducible tests with important unreported gaps. 3 = material checks reproducible and limitations mostly honest. 4 = strong claims-to-evidence mapping and explicit unknowns. 5 = strong reproducible evidence plus falsification/path proof for load-bearing behavior and no material overclaim detected.

## Attention/scope score 0–5

0 = objective repeatedly lost/major unrelated work. 1 = substantial detours/churn. 2 = noticeable unnecessary expansion. 3 = mostly bounded. 4 = tightly controlled with small justified deviations. 5 = requested work stays clearly prioritized; detours remain bounded and return cleanly.

## Required comparison views

Do not collapse the experiment into one magic number. Report:

1. Quality — weighted defects, severity, oracle pass rate, domain/evidence scores.
2. Efficiency — wall time, tokens/cost, calls, interventions, remediation/review.
3. Maintainability — dependencies, LOC/files, architecture churn, scope/attention.
4. Operational truth — restart/restore, cost authority, readiness, rollback/recovery, honest unknowns.

## Pre-registered interpretation bands

Heuristics only, not universal thresholds.

Clear Flow quality win if Baseline has a CRITICAL finding and Flow does not; or Flow weighted defect score is >=30% lower with no new CRITICAL/HIGH category; or Flow improves at least two high-value domains (tenant, financial, restart/recovery, failure semantics) by >=2 points without degrading another by >=2.

Quality tie: weighted scores within 15% with no meaningful severity/domain difference.

Efficiency interpretation:

```text
<=20% extra observable time/token cost for materially better quality = strong trade-off
20–50% extra = conditional/acceptable depending on severity avoided
>50% extra = material framework friction that must be explained
lower effort with equal/better quality = strong result
```

Do not declare a winner because one arm produced more paperwork.

## Repeatability

After Trial 001, repeat on a non-AI CRUD/business API, a midstream legacy repo, and an infra/deployment-heavy task. Alternate which arm runs first to reduce carryover effects.
