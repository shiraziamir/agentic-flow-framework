# Bootstrap prompt — Claude Code

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

```text
Bootstrap Claude Code from this framework.

Canonical authority: ARCHITECTURE.md, schemas/, verification/, skills/. Generated Claude files remain adapters.

Read ARCHITECTURE.md, schemas/CHANGE_CLASSIFICATION.md, schemas/CLAIM_RECEIPT.md, verification/00_INDEX.md and skills/00_INDEX.md first. Then inspect existing CLAUDE.md, .claude/agents, .claude/skills, settings/hooks and the target project's real frontend/backend/shared/data/infra/CI layout/build graph.

Create/update only what is justified:
- a SHORT CLAUDE.md mapping to canonical authority, project surface map, repo commands and local gotchas;
- Claude-compatible skills from canonical skills, preferably exposing/synchronizing SKILL.md directories rather than duplicating prose;
- lazy pointers to verification profiles rather than copying all profiles into CLAUDE.md;
- a cheap/read-only discovery subagent only if explicitly configured with an available cheap model; do not assume built-in Explore always uses a cheap model;
- a standard executor when useful;
- an independent reviewer/supervisor with read-only tools and cold review order: task/classification -> diff -> raw receipts -> falsifying checks -> executor narrative;
- deterministic hooks only for exact rules that must always fire and can be checked mechanically.

Material task flow exposed to Claude:
DRAFT_TASK -> REVIEW_DRAFT -> freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> required closure review.

Ensure task drafts classify FRONTEND/BACKEND/SHARED/DATA/INFRA/CI/etc. and freeze claim -> minimum receipt requirements. A reviewer/model judgment cannot replace missing behavioral evidence.

If structured JSON/YAML artifacts are used, expose scripts/verification_lint.py where practical.

Do not copy all skills/profiles/history into permanent context. Do not make the supervisor edit the work it reviews. Do not encode model names as authority; map semantic roles to current available models.

Validate a fresh session can discover canonical version, surface classification, verification router, draft review, apply/verify workflow, supervisor path and project commands without loading cold history.
```
