# Research note — adaptive governance, token efficiency, and cold history

**Date:** 2026-09-09  
**Research note version:** 1.0  
**Status:** evidence for framework v1.3; not an independent policy source

## Triggering feedback from Yara

A Yara task-management review rated risk control highly but found the same full ceremony too expensive for ordinary work. Three distinctions were empirically useful:

1. High-risk architecture/persistence/production work justified draft + freeze + separate apply + independent review.
2. Medium-risk same-task corrections could use a durable owner-approved amendment + bounded apply + tests + independent closure.
3. Evidence/docs/test-contract-only corrections could use one durable hashed owner amendment when no new runtime authority followed.

The review also identified safeguards that caught real defects: prerequisite/storage checks, pre-closure review finding missing gateway-level coverage, and durable authority checks for evidence/query/smoke matrices. Therefore v1.3 reduces duplicated ceremony without removing source-of-truth, durable identity, STOP-before-scope-creep, no-self-certification, evidence integrity, or independent closure where risk warrants it.

## Primary-source findings

### OpenAI — repository knowledge and progressive disclosure

OpenAI's February 2026 Harness Engineering report describes a large Codex-built repository where a giant `AGENTS.md` failed because it crowded context, became stale, and was difficult to verify. Their working pattern uses a short `AGENTS.md` as a map, structured repository docs as the system of record, versioned active/completed execution plans, progress/decision logs, mechanical documentation checks, and recurring doc-gardening. This supports hot indexes + cold historical artifacts rather than replaying project history into every task.

Source: https://openai.com/index/harness-engineering/

OpenAI's April 2026 Agents SDK update explicitly lists progressive disclosure via skills and `AGENTS.md` as harness primitives. This supports keeping procedures discoverable/on-demand rather than permanent prompt text.

Source: https://openai.com/index/the-next-evolution-of-the-agents-sdk/

### Anthropic — identify where context tokens are going

Anthropic's current tool-context documentation separates four sources of context pressure and four corresponding controls:

- large upfront tool definitions → tool search/lazy tool loading;
- many tool-result roundtrips → programmatic tool calling/batching;
- repeated stable prefixes → prompt caching;
- stale old tool results → context editing.

These mechanisms solve different problems and can be combined.

Source: https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context

### Anthropic — cost/intelligence routing

Anthropic's current optimization guide distinguishes quality-preserving/free-win levers from capability/cost tradeoffs. It recommends prompt caching/token hygiene first; running checkable workloads at lower effort and rerunning failures stronger in measured cases; frontier advisor/orchestrator patterns for hard decisions; and cheaper workers for partitions that exceed one context window. The document explicitly treats benchmark results as directional and says workloads must be measured locally.

Source: https://platform.claude.com/docs/en/about-claude/models/optimizing-for-cost-and-intelligence

This supports the framework rule: cheap workers may gather/check bounded evidence when acceptance can be mechanically verified, but routing policy must preserve quality gates and be benchmarked on project fixtures.

### Anthropic — usage observability and caching semantics

Claude responses expose usage fields, and Anthropic provides an organization Usage API that can break usage down by uncached input, cached input, cache creation, output, model, workspace and time bucket.

Source: https://platform.claude.com/docs/en/manage-claude/usage-cost-api

Prompt caching reduces cost/latency for stable prefixes, but cached input still counts as context-window input; total input is the sum of uncached + cache-read + cache-creation input tokens.

Sources:
- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching

Therefore cache-hit rate is a cost metric, not proof of healthy context.

### Gemini CLI — session usage visibility

Gemini CLI documents `/stats` as showing session statistics including token usage, cached token savings when available, and session duration. This is a concrete example of a CLI adapter being able to feed the portable usage ledger without making Gemini-specific fields canonical policy.

Source: https://google-gemini.github.io/gemini-cli/docs/cli/commands.html

### Provider-agnostic caution

Different hosted coding-agent products expose different levels of token/cost telemetry. The portable schema therefore permits unknown fields. It is incorrect to treat missing telemetry as zero usage or to fabricate costs from model names when billing details are unavailable.

## Derived engineering policy

1. Governance is risk-adaptive, not ceremony-maximal.
2. Preserve high-value boundaries while removing duplicate receipts/status fields.
3. Every material task may declare soft/hard usage budgets, but budget cannot weaken acceptance quality.
4. Waste warnings are based on observable anti-patterns and budget state, not an arbitrary global token threshold.
5. Use deterministic tools before models, small working sets before whole-repo scans, filtered artifacts before raw logs, and cheap read-only partitions before expensive discovery when quality can be checked.
6. Strong/expensive review results are stored as compact cold decision artifacts, not full transcripts.
7. Completed tasks, judgments, usage events and project stories are cold history. Normal execution reads indexes/current state only.
8. Storytelling/self-branding is an explicit on-demand workflow that reconstructs evidence-backed history from indexes first.
9. Documentation carries timestamps/version and material changes run a freshness check.

## Limits

- Anthropic benchmark savings are vendor/workload-specific and must not be copied as guaranteed percentages.
- Not every coding-agent product exposes per-task token/cost counters.
- Token reduction is not the only objective; extra tokens are justified when they materially improve evidence, safety, or quality.
