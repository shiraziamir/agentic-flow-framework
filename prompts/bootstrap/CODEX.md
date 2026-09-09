# Bootstrap prompt — Codex

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

```text
Bootstrap a Codex-compatible project adapter from Agentic Flow Framework.

Canonical authority is ARCHITECTURE.md + schemas/ + verification/ + skills/. Generated AGENTS.md or other Codex-facing instruction files are adapters, not independent policy.

Read the canonical architecture, change-classification schema, claim-receipt contract, verification router and skills index. Inspect the target project's actual frontend/backend/shared/data/infra/CI structure, build/test/affected-project commands and existing AGENTS.md files.

Generate the smallest useful Codex-facing map:
- short AGENTS.md pointers to source of truth, current task state and project commands;
- lazy verification-profile discovery keyed by change classification;
- workflow pointers for DRAFT_TASK -> REVIEW_DRAFT -> freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> independent closure;
- deterministic checks/hooks/scripts where exact rules can be enforced mechanically;
- model/delegation routing only when capabilities actually exposed by the current Codex harness justify it.

Material task drafts must classify engineering surface/risk and freeze claim -> minimum receipt requirements before APPLY. Reports must preserve ref/artifact/environment identity, checks not executed and bounded truth classes. A green CI summary or reviewer judgment cannot substitute for missing execution evidence.

If structured JSON/YAML task/evidence/status artifacts are used, make scripts/verification_lint.py discoverable.

Do not copy the whole framework, all verification profiles or historical tasks into AGENTS.md. Validate a fresh Codex session can navigate to what it needs progressively.
```
