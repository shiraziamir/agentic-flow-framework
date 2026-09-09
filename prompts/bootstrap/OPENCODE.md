# Bootstrap prompt — OpenCode

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

```text
Bootstrap OpenCode from this framework.

Treat ARCHITECTURE.md, schemas/, verification/ and skills/ as canonical. OpenCode rules/agents/config generated in the target project are adapters.

Inspect the target project's real frontend/backend/shared/data/infra/CI boundaries and existing OpenCode rules/agents. Generate the smallest useful adapter:
- concise rules pointing to canonical authority and project commands;
- lazy Skill discovery and lazy verification-profile pointers keyed by change classification;
- bounded cheap read-only discovery agents when current configured models/permissions support them;
- a standard executor and read-only independent reviewer only when useful;
- DRAFT_TASK -> REVIEW_DRAFT -> freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> closure workflow pointers.

Material drafts classify engineering surface/cross-cutting risk and freeze claim -> minimum receipt requirements. Reports keep identity, skipped/not-run checks and bounded truth classes. Reviewer output is judgment, not a replacement for runtime evidence.

Expose scripts/verification_lint.py if structured JSON/YAML artifacts are adopted.

Do not preload all rules/skills/profiles/history. Preserve quality when using cheaper agents and document unsupported harness capabilities rather than simulating them.
```
