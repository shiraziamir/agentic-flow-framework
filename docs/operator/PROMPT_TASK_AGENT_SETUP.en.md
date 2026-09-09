# Prompting, Task Writing, and Agent Setup Best Practices

**Operator-facing guide**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

## Prompting

Use clear, direct instructions. Put critical constraints and desired output early. Separate instructions from untrusted/context data with headings, tags, or code fences. Define ambiguous terms, expected output shape, evidence requirements, environment/permission boundaries, and what the agent must do when information is missing.

Prefer:

```text
Goal: fix duplicate payment on provider timeout.
Constraints: no schema change; no production mutation.
Evidence: focused test + mutation/path proof + integration receipt.
Stop if: retry semantics differ from current task assumptions.
Output: changed paths, exact tests, remaining unknowns.
```

Avoid vague prompts such as `fix it`, `make it production ready`, or `check everything` unless the agent first drafts a bounded task.

Use examples when format/semantics are easy to misunderstand. Iterate prompts based on observed failure modes instead of endlessly adding generic rules. Do not ask models to produce or expose private chain-of-thought; ask for concise rationale, assumptions, checks, receipts and uncertainty.

## Task writing

A material task should answer:

```text
What is observed?
What outcome must become true?
What is only a hypothesis?
What may be edited/referenced/excluded?
Which engineering/production surfaces are affected?
What claims will be made at closure?
What receipt proves each claim?
What environment is needed?
What checks are intentionally not required?
When must the agent STOP or escalate?
```

Write DoD before APPLY. Use observable outcomes rather than implementation-only wording. Preserve `UNKNOWN` when facts are not available.

## Test strategy

Use test-first for material claims where practical, but do not force strict TDD for every edit. Choose the smallest test layer that can directly establish the claim. Important new regression/safety tests should receive mutation/path proof when failure-detection ability matters. Do not optimize implementation merely to satisfy a test that bypasses the real path.

## Agent setup

Permanent agent instructions should be a map, not a manual. They should contain project-specific build/lint/test commands, source-of-truth pointers, important architecture boundaries, permissions, and lazy references to detailed profiles/skills.

Keep operator docs, research, historical tasks and large checklists out of always-on context. Use hierarchical/local instruction files only when a subtree genuinely differs.

## Subagents and model routing

Use deterministic tools first. Use cheap read-only subagents for bounded discovery/log reduction when outputs can be checked. Use standard execution models for localized changes and stronger judgment models for architecture/security/ambiguity/high-risk closure. Transfer compact evidence, not full transcripts.

## Mid-task setup

When introducing a new agent/framework in the middle of work, first snapshot repository ref, dirty paths, current task, tests already run and active environment mutations. Never pretend earlier work was reviewed by the new framework. Reconcile remaining work instead of restarting blindly.

## Sources

These recommendations align with current official guidance from OpenAI (clear/specific instructions and explicit output formats), Anthropic (clarity, structured prompts, examples, autonomy/safety and agentic context discipline), Google Gemini (precise instructions, consistent structure and hierarchical context files), and OpenCode (concise committed `AGENTS.md`, modular references and on-demand skills). See `docs/references/PRIMARY_SOURCES.md` for dated links and usage notes.
