# Freeze and Compare Procedure

Use unchanged for both arms.

## Freeze

Immediately after Q12 is completed and committed: STOP ALL MUTATION.

Record repository, branch, frozen HEAD, timestamp, working-tree status, and Q01..Q12 commit identities. If dirty, record exact paths; do not silently commit/discard after freeze.

## Reproducibility receipt

Capture without changing product behavior: Python version, install command, dependency list/lock, test command, run command, DB initialization command, and Docker build command if available.

## Independent evaluator

Use a fresh evaluator context that did not implement either arm. Give it PROJECT_SPEC, QUEUE, METRICS_AND_SCORING, EVALUATOR_ORACLE, and both frozen repos/HEADs. Randomize/alternate evaluation order. Inspect actual code and run tests; do not trust final reports alone.

## Evaluation sequence

1. Install using documented instructions.
2. Run each project's own full suite unmodified and record results.
3. Build Docker image if documented/practical.
4. Run evaluator semantic/fault tests against frozen code.
5. Perform controlled failure injection in evaluator-owned temporary copies.
6. Static-review material paths.
7. Score without repair.

Useful fault injections include SQLite unavailable/read failure, provider transient/permanent failure, cache loss/restart, mutation after cache population, concurrent near-budget queries, concurrent duplicate ingestion, and backup→mutate/loss→restore/readback.

Static review should specifically inspect tenant filter omissions, non-atomic budget check/write, exception-to-zero financial fallback, cache keys missing tenant/version, admin reset touching authoritative tables, readiness that is always green, backup without restore proof, unbounded cache/retry behavior, idempotency incorrectly global, and provider cost recorded only on success.

## Finding record

For each finding record ID, severity, requirement/queue source, reproduction, observed vs expected behavior, frozen HEAD, and whether the arm's own tests detected it.

Do not deduct twice for one root cause unless impacts are independently material.

## Final comparison

Include frozen HEAD, 12/12 completion, own suite result, oracle pass rate, weighted escaped-defect score, severity counts, domain scores, evidence-quality, attention/scope, wall time/tokens/cost if available, human interventions, remediation/review rounds, dependency count, and application/test/control LOC.

Explain where Agentic Flow helped, where it added friction without value, shared defects, unique defects, which guardrails prevented real issues, which rules were ignored/ambiguous/too expensive, and whether `PRODUCT_STANDARD` was proportionate.

Allowed conclusion: “In this paired TenantRAG trial, under these models/tools/environment, Arm X performed better/worse on these measured dimensions.”

Not allowed from one run: universal claims that Agentic Flow makes coding agents N% better/faster/safer.
