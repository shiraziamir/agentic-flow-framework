# Research note — context engineering and model routing

**Date:** 2026-09-09  
**Research note version:** 1.1  
**Status:** evidence retained for framework v1.3; not an independent policy source

This note records primary evidence behind the framework's context/model-routing guidance. Later policy lives in `ARCHITECTURE.md`; product-specific behavior must be rechecked when material.

## Findings

### 1. Bigger context is not automatically better

Anthropic's context-window documentation explicitly describes context as working memory and warns that accuracy/recall degrade as context grows (“context rot”). OpenAI's Harness Engineering report describes a failed experiment with one giant `AGENTS.md`: it crowded out task/code context, became stale, and made guidance less useful. OpenAI's working pattern became a short `AGENTS.md` as a map into structured repository docs.

Sources:
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://openai.com/index/harness-engineering/
- https://openai.com/index/unrolling-the-codex-agent-loop/

### 2. Separate-context workers are a real context-control mechanism

Claude Code documents subagents as separate contexts and supports explicit model selection for custom subagents. OpenCode supports child sessions/agents and per-agent model choice. Exact built-in defaults are version-specific and must not be treated as permanent policy.

Sources:
- https://code.claude.com/docs/en/sub-agents
- https://opencode.ai/docs/agents

### 3. Cheap-model routing is practical when bounded and measured

Claude's cost/intelligence guidance supports cheaper workers/advisors/orchestrators for appropriate workloads and emphasizes local measurement. OpenCode supports per-agent/per-command model overrides. Custom API harnesses may map semantic tiers to provider model families, but hosted product menus and billing must be verified at decision time.

Sources:
- https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence
- https://opencode.ai/docs/agents

### 4. Prompt caching lowers cost/latency but does not create context capacity

Anthropic explicitly states cached input still counts toward the context window. Cache-read/cache-creation/uncached input together form total input. Treat caching as a cost/latency lever, not context-health proof.

Sources:
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching

### 5. Frontend/monorepo scoping should use mechanical project graphs

Nx `affected` uses Git plus its project graph to calculate the minimum affected project set. TypeScript Project References are intended to split a program into smaller projects, enforce logical separation, improve build/editor performance, and make dependency/build order explicit. These mechanisms are better working-set inputs than an LLM-wide repository scan.

Sources:
- https://nx.dev/docs/features/ci-features/affected
- https://www.typescriptlang.org/docs/handbook/project-references

### 6. Yara skill telemetry needs denominator and identifier normalization

Inspected from `shiraziamir/yara` branch `claude`:

- `scripts/skill_report.py`
- `scripts/skill_events.py`
- `docs/SKILL_ACTIVATION_TRACE.md`

The project documentation states canonical skill IDs omit `.md` and records historical rows with both forms. `effectiveness_report()` groups the raw skill string, explaining duplicate rows. `--last N` selects recently active task IDs present in the event log, not uninstrumented project tasks. Positive outcomes are association evidence unless a controlled fixture isolates causality.

## Engineering recommendation distilled

For large modular frontends:

1. Determine affected modules mechanically.
2. Give the parent agent a small task contract and module map.
3. Use cheap, read-only child agents for discovery/log reduction when outputs can be checked.
4. Use the normal coding tier for bounded implementation.
5. Escalate architecture/cross-module/security/ambiguous work to a stronger judgment tier.
6. Transfer compact evidence packets across tiers, not transcripts.
7. Run module-local/affected checks first; broaden according to dependency impact.
8. Make state durable and reset sessions at completed semantic boundaries.
9. Measure model-route quality using frozen fixtures before making routing permanent.
10. Treat cache hit as a cost metric, not a context-health metric.
