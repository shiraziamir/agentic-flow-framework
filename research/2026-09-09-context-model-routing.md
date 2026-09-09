# Research note — context engineering and model routing

Date: 2026-09-09

This note records the primary evidence used for Agentic Flow Framework v1.1. It is source material, not a second policy file.

## Findings

### 1. Bigger context is not automatically better

Anthropic's context-window documentation explicitly describes context as working memory and warns that accuracy/recall degrade as context grows (“context rot”). OpenAI's Harness Engineering report describes a failed experiment with one giant `AGENTS.md`: it crowded out task/code context, became stale, and made guidance less useful. OpenAI's working pattern became a short `AGENTS.md` as a map into structured repository docs.

Sources:
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://openai.com/index/harness-engineering/
- https://openai.com/index/unrolling-the-codex-agent-loop/

### 2. Separate-context subagents are a real context-control mechanism

Claude Code documents subagents as separate context windows. Its built-in Explore agent is read-only and uses Haiku for codebase search/analysis specifically to preserve parent context and control cost. OpenCode subagents run as child sessions with fresh context and permit per-agent model choice.

Sources:
- https://code.claude.com/docs/en/subagents
- https://code.claude.com/docs/en/context-window
- https://opencode.ai/docs/agents

### 3. Cheap-model routing is officially supported and practical

Claude Code supports `model: haiku|sonnet|opus|inherit` in subagent definitions and Anthropic's cost guide recommends Haiku for simple subagent work. OpenCode supports per-agent and per-command model overrides. For custom OpenAI API harnesses, GPT-5.6 currently provides Luna/Terra/Sol cost/capability tiers.

Sources:
- https://code.claude.com/docs/en/subagents
- https://code.claude.com/docs/en/costs
- https://platform.claude.com/docs/en/about-claude/models/choosing-a-model
- https://developers.openai.com/api/docs/models/gpt-5.6-luna
- https://developers.openai.com/api/docs/models/gpt-5.6-terra
- https://developers.openai.com/api/docs/models/gpt-5.6-sol
- https://opencode.ai/docs/agents

### 4. Prompt caching lowers cost/latency but does not create context capacity

Anthropic explicitly states that `input_tokens + cache_read_input_tokens + cache_creation_input_tokens` all count toward the context window and that cached prefixes still occupy the window. Prompt caching should therefore be treated as a cost/latency lever, not a reason to keep polluted sessions alive.

Sources:
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context

### 5. Frontend/monorepo scoping should use mechanical project graphs

Nx `affected` uses Git plus its project graph to calculate the minimum affected project set. TypeScript Project References are intended to break a program into smaller projects, enforce logical separation, improve build/editor performance, and make dependency/build order explicit. These mechanisms are better working-set inputs than an LLM-wide repository scan.

Sources:
- https://nx.dev/docs/features/ci-features/affected
- https://www.typescriptlang.org/docs/handbook/project-references

### 6. Yara skill telemetry needs denominator and identifier normalization

Inspected from `shiraziamir/yara` branch `claude`:

- `scripts/skill_report.py`
- `scripts/skill_events.py`
- `docs/SKILL_ACTIVATION_TRACE.md`

The project documentation itself states that canonical skill IDs omit `.md` and records historical rows with both forms. It explicitly defers historical aggregation normalization. `effectiveness_report()` currently groups the raw skill string, confirming why the user's aggregate displays duplicates. `--last N` selects the most recently active task IDs that exist in the event log; it does not include uninstrumented tasks.

The telemetry's causal boundary is sound: observed rule conformance and positive outcomes are not automatically causal evidence for the skill.

## Engineering recommendation distilled

For large modular frontends:

1. Determine affected modules mechanically.
2. Give the parent agent a small task contract and module map.
3. Use cheap, read-only child agents for discovery/log reduction.
4. Use the normal coding tier for bounded implementation.
5. Escalate architecture/cross-module/security/ambiguous work to a stronger judgment tier.
6. Transfer compact evidence packets across tiers, not transcripts.
7. Run module-local checks first; broaden according to dependency impact.
8. Make state durable and reset sessions at completed semantic boundaries.
9. Measure model-route quality using frozen fixtures before making routing permanent.
10. Treat cache hit as a cost metric, not a context-health metric.
