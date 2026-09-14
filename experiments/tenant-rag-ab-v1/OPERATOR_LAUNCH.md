# Operator Launch Checklist

## Prepare two repos

Create two empty repos from the same seed containing only `PROJECT_SPEC.md`, `RUN_RECORD.md`, and `.gitignore`. Do not copy `EVALUATOR_ORACLE.md` into either implementation repo.

Recommended names:

```text
tenant-rag-baseline
tenant-rag-agentic
```

Use the same default branch, machine/tooling, network policy and execution model/provider where practical.

## Arm A

Paste `BASELINE_BOOTSTRAP.md` as the initial instruction, then release Q01 from `QUEUE.md`.

## Arm B

Make Agentic Flow 1.11 available using normal adoption. Paste `AGENTIC_FLOW_BOOTSTRAP.md`, allow adoption/read-only discovery, then release the same Q01 text.

## Queue delivery

Preferred:

```text
Q01 → wait for commit/report
Q02 → wait for commit/report
...
Q12 → freeze
```

Copy queue text verbatim. Do not add hints like “remember cost races” or “check cache invalidation”; those are part of what the trial measures.

If an agent asks a genuine environment question, answer minimally and log it. If the same fact can affect the other arm, supply it there too before the equivalent step.

## Run order / carryover

Record which arm runs first. On later repeats alternate the order:

```text
Trial 1: Baseline then Flow
Trial 2: Flow then Baseline
```

Do not inspect one arm's defects and coach the second.

## Same-model rule

Prefer the same execution model/provider/harness. In the first trial, if Agentic Flow uses separate role contexts, use the same base model for those contexts to isolate workflow effects. Record any deviation.

## Freeze and evaluation

After Q12: record frozen HEAD, stop both agents, send no fix prompts, and keep the evaluator oracle hidden from implementation agents. Then follow `FREEZE_AND_COMPARE.md` with a fresh evaluator.

Recommended evaluator instruction:

```text
Evaluate these two frozen TenantRAG implementations using FREEZE_AND_COMPARE.md,
METRICS_AND_SCORING.md and EVALUATOR_ORACLE.md.
Do not modify either frozen repository.
Run their own documented tests first, then evaluator-controlled semantic/fault tests.
Score findings by the pre-registered rubric and compare quality, efficiency,
maintainability, operational truth, evidence quality and attention/scope control.
Do not infer universal superiority from this single paired trial.
```
