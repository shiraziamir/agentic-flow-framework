# Agentic Flow Framework

**Version:** 1.1.1  
**Updated:** 2026-09-09

A reusable, tool-agnostic operating framework for AI coding and engineering agents, generalized from the Yara workflow and checked against current primary documentation from OpenAI, Anthropic/Claude Code, OpenCode, Nx, and TypeScript.

> **Durable project memory; disposable, high-quality working context.**

## 1. Goal

The framework does not optimize for raw token reduction alone. It optimizes for **signal-to-context ratio**, bounded authority, reliable verification, and restart-safe project state.

Common failure modes in long agentic work are control-plane failures: giant permanent instruction files, whole-repository scans, stale chat memory, silent scope expansion, one agent acting as author/executor/judge, and evidence that disappears when a session ends.

## 2. Lifecycle

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

Low-risk projects may combine gates, but the logical boundaries remain useful.

## 3. Core principles

1. Repository/durable state beats conversation memory.
2. One rule has one authoritative home; link instead of duplicating policy.
3. Keep always-on instructions short; load procedures on demand as skills.
4. Write Definition of Done before implementation.
5. Drafting a task is not permission to execute it.
6. The executor is not automatically the final judge.
7. A stronger model has more capability, not magical authority or truth.
8. Execution may retry; strategy and scope may not silently mutate.
9. STOP/BLOCKED is a valid result when prerequisites are missing.
10. Verification must produce evidence proportional to risk.
11. Reset context at durable semantic boundaries, not arbitrary token counts.
12. Put high-volume exploration in isolated child contexts.
13. Put deterministic rules in scripts/hooks/CI where practical.
14. Skills need activation, authority, and output-contract tests.
15. A fresh agent should reconstruct the current state from durable artifacts.

## 4. Authority architecture

```text
POLICY / engineering constitution
        ↓
AGENTS.md — concise map + essential invariants
        ↓
Task contract
        ↓
On-demand SKILL.md procedures
        ↓
Vendor adapters — CLAUDE.md / GEMINI.md / hooks / tool config
```

Vendor adapters are implementation details, not a second source of policy.

### Keep root instructions small

OpenAI's Harness Engineering report describes a failed “one giant `AGENTS.md`” approach: it crowded out task/code context, became stale, and was difficult to verify. Their working approach treats a short `AGENTS.md` as a table of contents into structured repository knowledge.

Put only stable, high-value material in root instructions:

- source-of-truth locations;
- safety/repository invariants;
- build and test entrypoints;
- evidence/status vocabulary;
- pointers to deeper docs and skills.

Do not put task history, raw logs, or long procedures there.

## 5. Task contract

A material task should define:

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

For material work, separate authoring from execution. If execution proves that the task contract is wrong, STOP and amend it; do not silently rewrite the task while running it.

## 6. Skills

Skills are reusable procedures loaded only when their trigger is relevant. A useful skill contract declares:

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

Recommended starting default: **0–3 load-bearing skills** per task. This is a tunable policy, not a universal law.

Each skill should have positive, negative, near-miss, authority/no-mutation, output-contract, and fresh-session discovery tests.

## 7. Bounded execution

```text
inspect
→ hypothesis
→ cheapest discriminating test
→ act only if supported
→ verify
→ classify
```

Bound retries. A retry may repeat execution; it may not silently change strategy or scope.

## 8. Evidence

| Evidence | Meaning |
|---|---|
| CLAIM | assertion only |
| STATIC_RECEIPT | file/line/diff/config |
| TEST_RECEIPT | named test + result |
| LIVE_RECEIPT | real-stack/runtime observation |
| MUTATION_PROOF | break → test fails → restore → test passes |
| INDEPENDENT_REVIEW | cold/read-only audit or reproduction |

Do not collapse configured, implemented, and verified into one status.

## 9. Context engineering

Anthropic's current documentation describes context as working memory, warns that accuracy/recall degrade as context grows (“context rot”), and states that system prompts, messages, tool results, documents, and tool definitions all consume context.

Use four sets:

```text
CORE_CONTEXT
  stable policy + task contract + module map

WORKING_SET
  files/modules allowed to change

REFERENCE_SET
  contracts/interfaces needed to understand the task

EXCLUDED_SET
  unrelated modules, generated output, dependency trees, huge raw logs
```

A large context window is capacity, not permission to load the repository.

### Semantic reset

Reset after a durable boundary when:

- the task/phase is closed;
- decisions and evidence are durable;
- no required fact exists only in chat;
- the next exact action is recorded;
- repository state is inspectable.

Do not make “clear every N tokens” the primary policy.

### Prompt caching is not compression

Anthropic explicitly states that `input_tokens`, `cache_read_input_tokens`, and `cache_creation_input_tokens` all count toward the context window; cached prefixes still occupy context. Caching is a cost/latency optimization, not a context-capacity solution.

## 10. Large modular frontend repositories

Do not make the model discover the working set by reading every frontend module. Determine affected scope mechanically when possible.

Useful existing mechanisms include:

- Nx `affected` + project graph;
- TypeScript Project References;
- Turbo/Bazel/workspace graphs;
- import/AST dependency tooling already present in the repo.

Nx documents that `affected` uses Git and its project graph to determine the minimum affected project set. TypeScript Project References are designed to split programs into smaller pieces, improve builds, and enforce logical separation.

Do not introduce Nx solely for the agent if the project does not otherwise benefit from it.

### Module context contract

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

Start narrow and expand only when evidence/dependency graph requires it.

### Child agents as context firebreaks

Use isolated child contexts for:

- locating code/tests/config;
- import/export inventory;
- summarizing large logs;
- classifying failures;
- repetitive pattern scans;
- collecting dependency evidence.

Return a bounded handoff, not a transcript:

```text
CONCLUSION
FILES_READ
AFFECTED_MODULES
EVIDENCE_REFS
FAILING_CHECKS
UNRESOLVED
RECOMMENDED_NEXT_STEP
```

Parallelism protects parent context but may increase total cost if agents duplicate reads. Parallelize independent bounded work, not overlapping exploration.

### Control tool output

Filter mechanically before model ingestion. Preserve full raw logs as artifacts, but send the model only the relevant slice plus the artifact path.

```bash
npm test 2>&1 | tail -n 120
rg 'useLegacyCheckout' apps/web/src/features/checkout packages/contracts -n
nx affected -t test --base=origin/main --head=HEAD
```

## 11. Model routing

Routing low-risk work to cheaper models is a practical, documented pattern. Route by **uncertainty and blast radius**, not simply prompt length.

| Tier | Work | Default authority |
|---|---|---|
| T0 Deterministic | graph, grep/AST, lint, typecheck, test selection, formatting | scripts/CI |
| T1 Cheap read-only | discovery, inventory, log reduction, repetitive classification | no mutation |
| T2 Standard execution | localized implementation, module refactor, tests, bounded bug fix | scoped edits |
| T3 Judgment/high-risk | architecture, ambiguous diagnosis, cross-module contracts, security/data, high-risk closure | decision/review; mutation explicit |

### Claude Code

A practical policy is:

```text
T1 → Haiku for explicitly configured low-risk/read-only subagents
T2 → Sonnet for normal coding/execution
T3 → Opus for architecture/judgment when justified
```

**Current-version nuance:** as of Claude Code v2.1.198, the built-in `Explore` agent does **not** always run on Haiku; it inherits the main conversation's model. To force lower-cost exploration, define a project/user `Explore` subagent with `model: haiku` or explicitly configure subagent model routing. Claude Code still uses separate context for exploration/planning, and Anthropic's current cost guide explicitly recommends `model: haiku` for simple subagent tasks, Sonnet for most coding, and Opus for complex architecture/multi-step reasoning.

### OpenAI API custom harness

Current OpenAI API model guidance provides a cost/capability ladder:

```text
T1 → GPT-5.6 Luna — cost-sensitive/high-volume bounded work
T2 → GPT-5.6 Terra — balance intelligence and cost
T3 → GPT-5.6 Sol — complex professional work
```

Current published API list prices (per 1M text tokens) are:

```text
Luna  input $0.20 / output $1.20
Terra input $2.00 / output $12.00
Sol   input $4.00 / output $20.00
```

These are API prices and routing examples. Do not assume the hosted Codex product exposes the same model menu or billing behavior.

### OpenCode

OpenCode supports per-agent/per-command model overrides and child sessions, so the same cheap explorer / standard executor / stronger reviewer pattern can be implemented directly.

### Escalation conditions

```text
UNKNOWN_ROOT_CAUSE
CROSS_MODULE_PUBLIC_CONTRACT_CHANGE
SECURITY_OR_AUTH_CHANGE
DATABASE_OR_DURABLE_DATA_CHANGE
>2 FAILED_EXECUTION_LOOPS
TESTS_FAIL_OUTSIDE_WORKING_SET
DEPENDENCY_GRAPH_EXPANDS_MATERIALLY
ARCHITECTURAL_REQUIREMENT_AMBIGUITY
CHEAP_MODEL_LOW_CONFIDENCE_OR_CONFLICTING_EVIDENCE
HIGH_RISK_CLOSURE
```

Escalation should transfer the compact task/evidence packet, not the cheaper model's full conversation.

### Benchmark routing

Same-family routing reduces adapter differences but does not guarantee quality. Use frozen fixtures:

```text
same task
same tools
same acceptance gates
cheap tier vs standard/strong tier
measure quality, rework, regressions, latency, cost
```

Promote a cheaper route only when results justify it.

## 12. Yara skill telemetry audit

The supplied `python3 scripts/skill_report.py --last 100` output needs normalization and denominator caveats.

Inspection of Yara branch `claude` confirms:

- `_audit/SKILL_EVENTS.jsonl` is local/gitignored, so its raw aggregate cannot be independently recomputed from GitHub;
- `--last N` selects the latest N distinct **task IDs present in the event log**, not necessarily the latest N project tasks;
- canonical skill IDs are basenames **without `.md`**;
- historical telemetry contains both forms and the project documentation explicitly records this fragmentation;
- `effectiveness_report()` groups the raw `skill` string, so `.md` and non-`.md` forms appear separately;
- positive `effect_recorded` outcomes are association evidence unless a controlled fixture isolates the skill as the changed variable.

After stripping `.md`, the 14 displayed rows collapse to **12 canonical skill IDs**.

Fragmented pairs:

```text
yara_01_live_verify_against_real_stack
  normalized: triggered 2, applied 1

yara_eval_02_evaluating_a_test
  normalized: triggered 3, applied 3
```

Strongest positive observed-association signals in the supplied sample:

```text
model-routing-and-delegation : 3
diagnose-before-fix          : 2
yara_06_fix_the_fix          : 2
craft-and-apply-task          : 1
```

These are not causal proofs. Do not delete rarely triggered skills simply because the sample is small; keep them lazy/cold until stronger evidence exists.

Normalize at report/read time rather than rewriting append-only history:

```python
def canonical_skill_id(value: str) -> str:
    return value[:-3] if value.endswith('.md') else value
```

Add reporting fields such as:

```text
instrumented_task_count
project_task_count_if_known
telemetry_coverage_pct
eligible_trigger_count
activation_count
positive/neutral/negative outcomes
evidence tier
```

For causal skill evaluation, run the same frozen task fixture twice with the skill enabled vs removed/neutralized and hold other variables constant.

## 13. Tool adapters

- **Claude Code:** thin `CLAUDE.md`, on-demand skills, explicit subagent models/permissions, hooks for deterministic enforcement.
- **Codex:** concise hierarchical `AGENTS.md`, durable repository-visible plans/evidence, isolated worktrees/agents.
- **OpenCode:** `AGENTS.md`, lazy references, skills, per-agent model and permission settings.
- **Gemini CLI:** use `GEMINI.md` hierarchy/imports carefully; compression/checkpoints do not replace durable task state.
- **GitHub Copilot:** share standing rules; avoid policy duplication across instruction surfaces.
- **OpenCloud:** treat as an execution/deployment adapter, not reasoning authority; keep validate → deploy → verify and scoped credentials.

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

Use high assurance for production, multi-tenant, security/data-sensitive, or long autonomous campaigns.

## 15. Starter policy

```yaml
context_policy:
  root_instruction_target_lines: 120
  default_edit_modules: 1
  default_reference_modules: 2
  raw_log_to_model: false
  semantic_reset_after_closed_task: true

routing:
  deterministic_first: true
  cheap_readonly_for: [discovery, inventory, log_summarization, classification]
  standard_executor_for: [localized_feature_work, module_scoped_refactor, tests]
  judgment_tier_for: [cross_module_contract_change, architecture, security, ambiguous_root_cause, high_risk_closure]

escalation:
  execution_retry_limit_before_judgment: 2
  expand_scope_only_with_evidence: true
  transfer_raw_conversation: false

verification:
  use_affected_graph_when_available: true
  run_local_checks_first: true
  broaden_tests_on_shared_contract_change: true
```

The numeric values are starting defaults, not universal laws. Tune against real project fixtures.

## 16. Primary sources

### OpenAI

- https://openai.com/index/harness-engineering/
- https://openai.com/index/unrolling-the-codex-agent-loop/
- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/gpt-5.6-luna
- https://developers.openai.com/api/docs/models/gpt-5.6-terra
- https://developers.openai.com/api/docs/models/gpt-5.6-sol

### Anthropic / Claude Code

- https://platform.claude.com/docs/en/build-with-claude/context-windows
- https://platform.claude.com/docs/en/build-with-claude/prompt-caching
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/costs
- https://platform.claude.com/docs/en/about-claude/models/choosing-a-model

### OpenCode

- https://opencode.ai/docs/agents
- https://opencode.ai/docs/rules

### Frontend/monorepo mechanics

- https://nx.dev/docs/features/ci-features/affected
- https://www.typescriptlang.org/docs/handbook/project-references

### Yara implementation inspected

- `scripts/skill_report.py` — branch `claude`
- `scripts/skill_events.py` — branch `claude`
- `docs/SKILL_ACTIVATION_TRACE.md` — branch `claude`

## 17. Vendor-drift rule

Product defaults, model names, context limits, commands, and prices can change. Role-level policy should remain stable while concrete adapters are re-verified against current official documentation. Do not turn a vendor default into a permanent framework invariant.

---

> **The ideal agentic workflow does not require long-lived agent memory. It requires durable project memory and disposable, high-quality working context.**
