# Generated adapters

**Guide version:** 1.1  
**Updated:** 2026-09-09T10:04:00Z

Files such as `CLAUDE.md`, Codex `AGENTS.md`, tool-specific agent definitions, OpenCode config and `GEMINI.md` belong to the **target project**, not necessarily this framework repo.

Generate them with `prompts/bootstrap/*`.

They are adapters, not source of truth. If an adapter conflicts with `ARCHITECTURE.md`, fix/amend the canonical architecture or regenerate the adapter; do not silently fork policy in the adapter.

Preferred adapter properties:

- short permanent context;
- explicit pointer to canonical authority + framework version generated from;
- project-local surface/dependency map and build/test/affected-project commands;
- lazy/on-demand Skill discovery;
- lazy `verification/00_INDEX.md` routing: load GENERAL + classified surface + triggered annexes only;
- discoverable `DRAFT_TASK → REVIEW_DRAFT → APPLY → VERIFY_AND_REPORT → supervisor` workflow;
- explicit claim/receipt and reality-report pointers rather than copied verification prose;
- deterministic linter/hook integration only when mechanically reliable;
- vendor-specific permissions/hooks/model configuration only;
- cold history excluded from normal context;
- reproducible regeneration from current framework version.

An adapter may translate mechanics to a vendor/harness, but it may not weaken receipt requirements, reclassify risk silently, or turn model/reviewer confidence into evidence.
