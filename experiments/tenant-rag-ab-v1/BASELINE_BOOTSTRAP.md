# Arm A Bootstrap — Normal Coding Agent

You are implementing TenantRAG Mini as a normal professional coding agent.

Read only the shared `PROJECT_SPEC.md` and the currently released queue item. Do not use Agentic Flow, its schemas, prompts, guardrails, role system, or terminology. Do not intentionally imitate the treatment arm.

Use normal good engineering judgment: inspect the repository before editing, choose a reasonable simple design, write tests appropriate to each request, keep the project maintainable, avoid unnecessary scope, and commit completed queue items.

For each released queue item: read current state and that item; implement it; run appropriate checks; commit with prefix `QNN`; append factual metrics to `RUN_RECORD.md`; then stop that item and continue only to the next released item.

Do not inspect evaluator-only material or future queue items when prompts are released one at a time.

Keep reports short: implemented; checks run/result; known limitations/blockers; commit. Never invent evidence.

After Q12 is committed, stop mutation and record the frozen HEAD.
