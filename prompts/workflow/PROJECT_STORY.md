# Workflow prompt — PROJECT STORY

**Version:** 1.1  
**Updated:** 2026-09-09T08:22:00Z

```text
Build an evidence-backed project story only because the user explicitly requested history narrative, architecture evolution, a case study, release narrative, lessons learned, or self-branding/portfolio material.

Read:
1. ARCHITECTURE.md
2. skills/project-storytelling/SKILL.md
3. the project's compact current index/timeline
4. the latest applicable retrospective/index if one exists
5. selected completed task summaries/judgments/evidence only as required to verify claims
6. usage SUMMARY/ledger only if token/cost claims are requested and telemetry coverage is known

If the request requires exact historical counts, governance metrics, STOP/amendment statistics, or audit-grade reconstruction and no trustworthy retrospective exists, use prompts/workflow/BUILD_PROJECT_RETROSPECTIVE.md first.

Do NOT recursively load every task/evidence/judgment artifact first.

Separate:
- PROVEN / VERIFIED FACT
- RECONSTRUCTED / INFERENCE
- UNKNOWN / COVERAGE LIMIT

Include dates, architecture/decision milestones, hard problems, constraints, before/after outcomes, important failed approaches when useful, and measurable token/cost data only when sourced.

For self-branding, emphasize engineering leverage, risk reduction, automation, architecture, governance discipline and outcomes without exaggeration.

Write the result as a cold reader artifact under the project's stories location with:
- version
- generated_at/as_of timestamp
- source refs
- validity/telemetry/reconstruction coverage boundary

Do not add the story to standing coding-agent context.
```
