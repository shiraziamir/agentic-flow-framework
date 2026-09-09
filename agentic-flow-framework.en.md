# Agentic Flow Framework

**Version:** 1.1  
**Updated:** 2026-09-09

A reusable, tool-agnostic operating framework for AI coding and engineering agents. It is derived from the Yara workflow, then checked against current primary documentation from OpenAI, Anthropic/Claude Code, OpenCode, Nx and TypeScript.

> **Durable project memory; disposable, high-quality working context.**

## 1. Why this exists

The dominant failure mode in long agentic engineering is often not model intelligence. It is control-plane failure: oversized permanent instructions, whole-repository scans, stale conversation memory, silent scope expansion, unclear authority, evidence trapped in chat, and one model acting as author, executor and final judge.

The framework therefore optimizes for **signal-to-context ratio**, recoverability and bounded authority rather than merely minimizing token count.

## 2. Core lifecycle

```text
REQUEST
  ↓
TASK CONTRACT
  ↓
REVIEW / FREEZE
  ↓
APPLY AUTHORIZATION
  ↓
BOUNDED EXECUTION
  ↓
VERIFICATION + RECEIPTS
  ↓
INDEPENDENT REVIEW (risk-based)
  ↓
CLOSURE
  ↓
DURABLE CHECKPOINT
  ↓
SAFE CONTEXT RESET
```

Low-risk projects can combine some gates, but the conceptual boundaries remain useful.

## 3. Core principles

1. Repository/durable state beats conversation memory.
2. One rule has one authoritative home; link instead of duplicating policy.
3. Keep always-on instructions short. Procedures are loaded on demand as skills.
4. Definition of Done is written before implementation.
5. Drafting a task is not permission to execute it.
6. The executor is not automatically the final judge.
7. A stronger model has more capability, not magical authority or truth.
8. Execution may retry; strategy and scope may not silently mutate.
9. STOP/BLOCKED is a legitimate result when prerequisites are missing.
10. Verification must produce receipts proportional to risk.
11. Context reset happens at a durable semantic boundary, not an arbitrary token threshold.
12. Heavy exploration belongs in isolated child contexts; the parent keeps conclusions and receipts.
13. Deterministic rules belong in scripts/hooks/CI when possible.
14. Skills need activation, authority and output-contract tests.
15. Every task should be reconstructible after a session/model/provider change.

## 4. Authority hierarchy

A portable repository should keep vendor-neutral policy separate from tool adapters.

```text
POLICY / engineering constitution
        ↓
AGENTS.md (short map + essential invariants)
        ↓
Task contract
        ↓
On-demand SKILL.md procedures
        ↓
Vendor adapters: CLAUDE.md / GEMINI.md / tool config / hooks
```

A vendor adapter must not become a second policy source.

### Recommended root `AGENTS.md`

Use it as a map, not a manual. OpenAI's Harness Engineering report describes an internal failure mode where one giant `AGENTS.md` crowded out useful task/code context and became stale; the working pattern became a short map into structured repository documentation.

Keep in root instructions only:

- source-of-truth locations;
- safety invariants;
- build/test commands;
- repository boundaries;
- evidence vocabulary;
- pointers to skills/docs.

Do not put long procedures, task history, raw logs or copied architecture manuals there.

## 5. Task contract

A task should define:

```yaml
goal: observed outcome to achieve
symptom: what is actually observed
hypotheses: theories, explicitly not facts
scope: allowed edit surface
non_scope: what must not be touched
baseline: what must still pass
uncertainties: facts to resolve before mutation
definition_of_done: written before implementation
required_evidence: receipts needed for closure
stop_conditions: reasons to halt instead of improvising
escalation_conditions: when stronger judgment is required
```

### Draft → review → apply

For material work, separate authoring from execution. This prevents an agent from writing itself a conveniently easy task and immediately declaring success. If execution reveals that the contract is wrong, STOP and amend; do not silently rewrite the task being executed.

## 6. Skills and progressive disclosure

Skills are reusable task-specific procedures, not permanent context. A useful skill contract contains:

```text
PURPOSE
USE_WHEN
DO_NOT_USE_WHEN
INPUT_CONTRACT
OUTPUT_CONTRACT
MUTATION_AUTHORITY
REQUIRES
CONFLICTS_WITH
EVIDENCE_REQUIRED
FAIL_CLOSED_BEHAVIOR
```

Recommended default: select **0–3 load-bearing skills** for a task. This is a starting policy, not a hard universal limit.

Each skill should be tested for:

- positive activation;
- negative activation;
- near-miss activation;
- authority/no-mutation behavior;
- output contract;
- fresh-session discovery.

## 7. Bounded execution loop

```text
inspect
→ form hypothesis
→ cheapest discriminating test
→ act only if supported
→ verify
→ classify
```

Bound retries. More importantly, execution retry is different from strategy retry. Evidence that invalidates the contract must cause amendment/escalation, not an invisible strategy switch.

## 8. Evidence model

| Evidence | Meaning |
|---|---|
| CLAIM | model/human assertion only |
| STATIC_RECEIPT | file, line, diff, config |
| TEST_RECEIPT | named test command and result |
| LIVE_RECEIPT | real-stack/runtime observation |
| MUTATION_PROOF | break behavior → test fails → restore → test passes |
| INDEPENDENT_REVIEW | cold/read-only reviewer reproduces or audits |

Do not collapse configured, implemented and verified into one status word.

## 9. Context engineering

### Context is working memory, not durable memory

Anthropic's current context-window guidance explicitly warns that more context is not automatically better and describes degradation as context grows. Prompt/tool history, retrieved documents and tool results all compete for the same working context.

Use this mental model:

```text
CORE_CONTEXT
  stable policy + task contract + module map

WORKING_SET
  files/modules that may be edited

REFERENCE_SET
  contracts/interfaces needed for understanding

EXCLUDED_SET
  unrelated modules, generated output, huge logs, dependency trees
```

A large context window is capacity, not permission to load the whole repository.

### Semantic reset

Reset when:

- the current task/phase is closed;
- decisions and receipts are durable;
- no required fact exists only in chat;
- next exact action is written;
- repository state is inspectable.

Do not use a mechanical rule such as “clear every 120k tokens” as the primary policy.

### Prompt caching is not compression

Anthropic explicitly documents that cache-read and cache-creation input still count toward the context window. Prompt caching is a cost/latency optimization for stable prefixes, not an excuse for an endlessly growing session.

## 10. Large modular frontend repositories

Large frontend/monorepo work should be scoped by a **dependency graph**, not by giving the model every module.

### Mechanical discovery first

Prefer existing project mechanics:

- Nx `affected` and project graph;
- TypeScript Project References;
- Turbo/Bazel/workspace dependency graphs;
- import/AST graph tools already present in the repository.

Nx's `affected` mechanism uses Git plus the project graph to calculate the minimum impacted project set. TypeScript Project References are specifically designed to split a large program into smaller projects with explicit boundaries and build order.

Do not introduce a monorepo framework solely for the agent if the project does not otherwise need it; use the graph already available.

### Module context contract

For each task produce a small context descriptor:

```yaml
module: checkout
edit_modules: [checkout]
reference_modules: [cart, identity]
public_contracts:
  - packages/contracts/payment.ts
exclude:
  - node_modules/**
  - dist/**
  - coverage/**
local_checks:
  - npm run test:checkout
  - npm run typecheck:checkout
escalate_if:
  - public_contract_changes
  - tests_fail_outside_working_set
```

Start with one edit module and a small number of reference modules; expand only when evidence shows the dependency graph requires it. Numeric defaults are tunable heuristics, not laws.

### Subagents as context firebreaks

Use separate child contexts for high-volume work:

- locate implementation/test/config files;
- inventory imports/exports;
- summarize a large build log;
- classify failing tests;
- compare repetitive patterns;
- collect dependency evidence.

The parent should receive a bounded handoff:

```text
CONCLUSION
FILES_READ
AFFECTED_MODULES
EVIDENCE_REFS
FAILING_CHECKS
UNRESOLVED
RECOMMENDED_NEXT_STEP
```

Do not return the full subagent transcript unless a specific debugging need exists.

### Parallelism is not automatically cheaper

Parallel child agents protect parent context but may increase total spend if they repeatedly scan the same files. Parallelize independent bounded work, not overlapping discovery.

### Control tool output

Use mechanical filtering before sending data to the model. Save full logs as artifacts, but feed the model only the relevant slice plus the raw-log path.

```bash
npm test 2>&1 | tail -n 120
rg 'useLegacyCheckout' apps/web/src/features/checkout packages/contracts -n
nx affected -t test --base=origin/main --head=HEAD
```

## 11. Model routing

Yes: routing bounded work to cheaper models is a practical, documented engineering pattern.

### T0 — deterministic

No LLM where scripts are more reliable:

- dependency graph;
- grep/AST query;
- formatter;
- lint/typecheck;
- test selection;
- schema validation.

### T1 — cheap read-only

Use the cheapest model that is reliable for:

- code/file discovery;
- inventory;
- log summarization;
- repetitive classification/extraction;
- simple comparison.

Default mutation authority: **none**.

Claude Code's built-in Explore agent is a real example: separate context, read-only tools, Haiku model. Anthropic also recommends cheaper model routing for simple subagent tasks.

### T2 — standard execution

Use an everyday coding model for:

- localized implementation;
- module-scoped refactor;
- test authoring;
- bounded bug fix.

Default authority: scoped edits inside the task contract.

### T3 — judgment/high risk

Escalate for:

- architecture;
- ambiguous root cause;
- cross-module public-contract changes;
- security/auth/tenant isolation;
- database/durable-data changes;
- repeated failed loops;
- acceptance of known failures;
- high-risk final closure.

Use the strongest justified model or human/independent reviewer.

### Example Claude mapping

```text
T1 → Haiku (read-only exploration/inventory)
T2 → Sonnet (normal coding/execution)
T3 → Opus (architecture/judgment)
```

### Example OpenAI API mapping

For a custom API harness, current GPT-5.6 tiers provide a similar capability/cost ladder:

```text
T1 → GPT-5.6 Luna
T2 → GPT-5.6 Terra
T3 → GPT-5.6 Sol
```

This is API-harness guidance. Do not assume the hosted Codex product exposes the same menu or billing behavior.

### OpenCode

OpenCode supports per-agent and per-command model overrides, so the same cheap-reader / standard-executor / stronger-reviewer pattern is straightforward.

### Escalation rules

Start cheap only when the work is safely bounded. Escalate on:

```text
UNKNOWN_ROOT_CAUSE
CROSS_MODULE_PUBLIC_CONTRACT_CHANGE
SECURITY_OR_AUTH_CHANGE
DATABASE_OR_DURABLE_DATA_CHANGE
>2 FAILED_EXECUTION_LOOPS
TESTS_FAIL_OUTSIDE_WORKING_SET
DEPENDENCY_GRAPH_EXPANDS_MATERIALLY
REQUIREMENT_AMBIGUITY_AFFECTS_ARCHITECTURE
CHEAP_MODEL_LOW_CONFIDENCE_OR_CONFLICTING_EVIDENCE
HIGH_RISK_CLOSURE
```

On escalation send a compact evidence packet, not the previous model's full conversation.

### Benchmark routing; do not assume it

Same-family routing reduces adapter differences, but it is not magically safe. Build frozen fixtures and compare:

```text
same task
same tools
same acceptance gates
cheap vs standard/strong tier
measure quality, rework, regressions, latency, cost
```

Promote cheap routing only where the empirical results justify it.

## 12. Yara skill-telemetry audit

The supplied `python3 scripts/skill_report.py --last 100` output should not be read as “only these skills existed” or “these were used across the last 100 project tasks” without qualification.

Inspection of Yara branch `claude` found:

- `_audit/SKILL_EVENTS.jsonl` is local/gitignored and therefore cannot be independently recomputed from GitHub;
- `--last N` selects the latest N distinct **task IDs present in the event log**, not necessarily the latest N project tasks;
- the canonical skill identifier is the basename **without `.md`**;
- historical telemetry contains both forms and the documentation explicitly records this identifier-fragmentation defect;
- `effectiveness_report()` groups the raw skill string, so `.md` and non-`.md` rows appear separately;
- observed positive outcomes are association evidence unless a controlled skill-present/skill-absent fixture isolates causality.

### Normalized interpretation of the supplied report

After stripping `.md`, the 14 displayed rows collapse to **12 canonical skill identifiers**.

The two fragmented pairs are:

```text
yara_01_live_verify_against_real_stack
  reported as both basename and basename.md
  normalized: triggered 2, applied 1

yara_eval_02_evaluating_a_test
  reported as both basename and basename.md
  normalized: triggered 3, applied 3
```

The strongest observed-association signals in the supplied output are:

```text
model-routing-and-delegation : 3 positive effect events
diagnose-before-fix          : 2
yara_06_fix_the_fix          : 2
craft-and-apply-task          : 1
```

These numbers do **not** establish causality. Rarely triggered skills also should not be deleted simply because their sample is small; keep them cold/lazy until enough evidence exists.

### Telemetry improvements

Normalize at report/read time rather than rewriting the append-only historical log:

```python
def canonical_skill_id(value: str) -> str:
    return value[:-3] if value.endswith('.md') else value
```

Also report:

```text
instrumented_task_count
project_task_count_if_known
telemetry_coverage_pct
eligible_trigger_count
activation_count
positive/neutral/negative outcomes
evidence tier
```

For causal evaluation, use a frozen task fixture twice with one isolated variable: skill enabled vs removed/neutralized.

## 13. Tool adapters

### Claude Code

Use a thin `CLAUDE.md`, on-demand Skills, separate-context subagents and deterministic hooks where a rule must always fire.

### Codex

Use concise hierarchical `AGENTS.md`, durable plans/evidence and isolated worktrees/agents. OpenAI's own harness guidance strongly favors repository-visible state over giant instruction blobs.

### OpenCode

Use `AGENTS.md`, lazy references, skills and per-agent model/permission settings.

### Gemini CLI

Use `GEMINI.md` hierarchy/imports carefully. Compression/checkpointing helps capacity but does not replace durable task state.

### GitHub Copilot

Keep standing rules in shared repository instructions/`AGENTS.md`; keep task procedures as reusable skills when available. Avoid copying the same policy into multiple instruction surfaces.

### OpenCloud

Treat it as an execution/deployment adapter rather than the reasoning authority. Keep deploy credentials scoped, use structured output/idempotency where available, and preserve validate → deploy → verify separation.

## 14. Governance levels

### Minimal

```text
AGENTS.md
Task/issue + DoD
focused tests
short evidence note
semantic reset
```

### Standard — recommended default

```text
canonical policy
concise AGENTS.md
on-demand skills
explicit task contract
bounded model routing
risk-based verification
durable checkpoint
independent review for material changes
```

### High assurance

```text
draft/freeze/apply separation
contract identity/hash
judgment ledger
read-only independent reviewer
negative tests / mutation proof
locks or isolated worktrees
durable evidence
fresh-session recovery test
```

Use high assurance for production, multi-tenant, security/data-sensitive or long autonomous campaigns.

## 15. Recommended starter policy

```yaml
context_policy:
  root_instruction_target_lines: 120
  default_edit_modules: 1
  default_reference_modules: 2
  raw_log_to_model: false
  semantic_reset_after_closed_task: true

routing:
  deterministic_first: true
  cheap_readonly_for:
    - discovery
    - inventory
    - log_summarization
    - repetitive_classification
  standard_executor_for:
    - localized_feature_work
    - module_scoped_refactor
    - test_authoring
  judgment_tier_for:
    - cross_module_contract_change
    - architecture
    - security
    - ambiguous_root_cause
    - high_risk_closure

escalation:
  execution_retry_limit_before_judgment: 2
  expand_scope_only_with_evidence: true
  transfer_raw_conversation: false

verification:
  use_affected_graph_when_available: true
  run_local_checks_first: true
  broaden_tests_on_shared_contract_change: true
```

These numeric values are starting defaults, not universal laws. Tune against real project fixtures.

## 16. Metrics worth measuring

Measure outcomes that can change decisions:

- context resets per task;
- repeated files/tool-output bytes read;
- affected-module count;
- cheap → standard → judgment escalation rate;
- failed loops before escalation;
- rework/regression count by route;
- verification completeness;
- cost and latency per accepted task;
- skill activation/effect evidence tier;
- fresh-session recovery success.

Do not optimize cache-hit percentage or raw token count in isolation.

## 17. Primary sources

### OpenAI

- Harness Engineering: https://openai.com/index/harness-engineering/
- Unrolling the Codex agent loop: https://openai.com/index/unrolling-the-codex-agent-loop/
- How OpenAI uses Codex: https://openai.com/business/guides-and-resources/how-openai-uses-codex/
- Models: https://developers.openai.com/api/docs/models
- GPT-5.6 Luna: https://developers.openai.com/api/docs/models/gpt-5.6-luna
- GPT-5.6 Terra: https://developers.openai.com/api/docs/models/gpt-5.6-terra
- GPT-5.6 Sol: https://developers.openai.com/api/docs/models/gpt-5.6-sol

### Anthropic / Claude Code

- Context windows: https://platform.claude.com/docs/en/build-with-claude/context-windows
- Prompt caching: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- Manage tool context: https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
- Claude Code context window: https://code.claude.com/docs/en/context-window
- Subagents: https://code.claude.com/docs/en/subagents
- Manage costs: https://code.claude.com/docs/en/costs
- Choosing a model: https://platform.claude.com/docs/en/about-claude/models/choosing-a-model

### OpenCode

- Agents: https://opencode.ai/docs/agents
- Rules: https://opencode.ai/docs/rules

### Frontend / monorepo mechanics

- Nx affected: https://nx.dev/docs/features/ci-features/affected
- TypeScript Project References: https://www.typescriptlang.org/docs/handbook/project-references

### Yara implementation inspected

- `scripts/skill_report.py` — branch `claude`
- `scripts/skill_events.py` — branch `claude`
- `docs/SKILL_ACTIVATION_TRACE.md` — branch `claude`

---

## Closing principle

> **The ideal agentic workflow does not require a long-lived agent memory. It requires durable project memory and a disposable, high-quality working context.**
