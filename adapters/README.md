# Generated adapters

**Guide version:** 1.7  
**Updated:** 2026-09-09T11:30:00Z

Files such as `CLAUDE.md`, Codex `AGENTS.md`, OpenCode configuration and `GEMINI.md` belong to the **target project**. Generate them with `prompts/bootstrap/*` after inspecting the target repository.

They are adapters, not source of truth. If an adapter conflicts with `ARCHITECTURE.md`, amend/regenerate from canonical authority; never silently fork policy in a vendor file.

## Adoption

For a drop-in bundle, begin at `docs/agent/START_HERE.md`. For active coding state, use `docs/agent/MIDSTREAM_ADOPTION.md` before further product mutation.

The adapter should preserve existing valid project-specific rules and mechanisms. It should not replace working CI/CD, task stores, observability, security or architecture simply because framework examples use different filenames.

## Preferred adapter properties

- short permanent context;
- framework version + pointer to canonical `ARCHITECTURE.md`;
- pointer to current `.agentic/PROJECT_PROFILE.yaml` and current task/checkpoint;
- project-local build/lint/test/affected-project/deploy commands;
- lazy/on-demand Skill discovery;
- lazy verification routing: only the classified surface + triggered annexes;
- lazy production routing: only profiles triggered by the current work;
- discoverable DRAFT → REVIEW → required authorization → APPLY → VERIFY → supervisor flow;
- explicit claim/receipt/gap/override pointers instead of copied manuals;
- deterministic validators/hooks only where mechanically reliable;
- vendor-specific permissions/model/tool configuration based on capabilities actually available;
- operator docs, external research and cold history excluded from normal context;
- log-analysis workers read-only/least privilege with log payload treated as untrusted data;
- reproducible regeneration from current framework version.

An adapter may translate mechanics to a harness, but it may not weaken receipt/readiness requirements, silently change project baseline/tier, hide gaps/overrides, invent production authority, or turn model/reviewer confidence into behavioral evidence.
