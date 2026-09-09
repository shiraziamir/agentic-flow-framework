# Agent Usage Event Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09

Usage telemetry exists to make cost/context behavior visible without storing prompts, chain-of-thought, or full transcripts.

```yaml
timestamp: <RFC3339>
task_id: <task-id|null>
phase: DISCOVERY|DRAFT|REVIEW|EXECUTION|VERIFY|CLOSURE|STORY
agent_role: ORCHESTRATOR|CHEAP_READONLY|EXECUTION_TIER|JUDGMENT_TIER|INDEPENDENT_REVIEWER
provider: <provider>
model: <exact model if observable>
source: API_USAGE|SESSION_STATS|CLI_STATS|HARNESS|MANUAL|UNKNOWN
usage:
  input_tokens: <integer|null>
  cache_read_input_tokens: <integer|null>
  cache_creation_input_tokens: <integer|null>
  output_tokens: <integer|null>
  total_context_tokens: <integer|null>
  estimated_cost_usd: <number|null>
operations:
  tool_calls: <integer|null>
  child_agents: <integer|null>
waste_flags:
  - WHOLE_REPO_SCAN_WITHOUT_JUSTIFICATION
  - REPEATED_LARGE_FILE_REREAD
  - FULL_HISTORY_READ_WITHOUT_TRIGGER
  - LARGE_RAW_LOG_IN_CONTEXT
  - STRONG_MODEL_FOR_MECHANICAL_WORK
  - OVERLAPPING_SUBAGENT_DISCOVERY
  - REPEATED_FAILED_LOOP
  - UNUSED_TOOLSET_CONTEXT
  - CACHE_BREAKING_VOLATILE_PREFIX
  - OTHER
note: <short observable explanation|null>
evidence_refs: []
```

Provider fields are optional because not every hosted product exposes the same telemetry. Never fabricate missing token counts or cost. Record `null`/`UNKNOWN` instead.

The ledger is append-only. Reports may aggregate it, but daily agents should not preload historical rows. Only current-task budget state and a compact project aggregate belong in hot context.
