# Generated adapters

**Guide version:** 1.2  
**Updated:** 2026-09-09T10:40:00Z

Files such as `CLAUDE.md`, Codex `AGENTS.md`, tool-specific agent definitions, OpenCode config and `GEMINI.md` belong to the target project, not necessarily this framework repo. Generate them with `prompts/bootstrap/*`.

They are adapters, not source of truth. If an adapter conflicts with `ARCHITECTURE.md`, amend/regenerate from canonical authority; do not silently fork policy.

Preferred adapter properties:

- short permanent context;
- pointer to canonical authority + framework version generated from;
- project-local surface/dependency map and build/test/affected-project commands;
- for production-bound projects, pointer to current project production profile + open-gap index;
- lazy/on-demand Skill discovery;
- lazy verification routing: GENERAL + classified surface + triggered annexes only;
- lazy production routing: only delivery/observability/data/troubleshooting/security/AI-log/resilience/architecture profiles triggered by current task;
- discoverable DRAFT_TASK → REVIEW_DRAFT → APPLY → VERIFY_AND_REPORT → supervisor workflow;
- explicit claim/receipt/reality-report/gap pointers rather than copied manuals;
- deterministic validator/hook integration only when mechanically reliable (`verification_lint`, `production_readiness_lint` where compatible);
- vendor-specific permissions/hooks/model configuration only;
- cold completed tasks, historical gaps/incidents/runbooks/reviews excluded from normal context;
- log-analysis workers read-only/least privilege and log payload treated as untrusted data;
- reproducible regeneration from current framework version.

An adapter may translate mechanics to a vendor/harness, but it may not weaken receipt/readiness requirements, silently reclassify risk/tier, hide operational gaps, or turn model/reviewer confidence into evidence.