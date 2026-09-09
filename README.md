# Agentic Flow Framework

**Framework version:** 1.4  
**Updated:** 2026-09-09T08:22:00Z  
**Canonical policy:** [`ARCHITECTURE.md`](ARCHITECTURE.md)

A repository-first, tool-agnostic operating system for reliable, cost-aware coding agents.

> **Durable project memory; disposable, high-quality working context.**

This GitHub repository is the authoritative home of the framework. The old Google Drive folder is an archived snapshot only.

## What this solves

Coding agents often lose efficiency because of context pollution, giant instruction files, whole-repo scans, repeated rereads, expensive models doing mechanical discovery, stale chat memory, uncontrolled scope expansion, duplicated ceremony, weak evidence, and the same agent acting as author/executor/final judge.

Version 1.4 optimizes five things together:

1. **quality/risk control** — evidence, STOP boundaries, independent judgment;
2. **task-management efficiency** — governance proportional to risk;
3. **token/cost efficiency** — small working sets, cheap read-only workers, usage/waste visibility;
4. **durable but cold project memory** — history/decisions/usage remain reconstructible without being loaded on every task;
5. **audit-grade project reconstruction** — compact execution ledger + on-demand retrospective/storytelling instead of permanent long-history context.

## Source of truth

Read/order of authority:

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — **canonical policy, authority and lifecycle**.
2. [`schemas/`](schemas/) — task, amendment, evidence, supervisor, usage and history contracts.
3. [`skills/`](skills/) — reusable on-demand procedures.
4. Current approved/frozen task or amendment.
5. Durable evidence and supervisor decisions.
6. Generated vendor adapters.
7. Conversation memory.

**Vendor files are not policy authority.** `CLAUDE.md`, Gemini/OpenCode configuration, subagents and generated instruction files are projections of canonical policy and should identify the architecture version they were generated from.

## Quick start

### 1. Bootstrap the target project

Make this repository available beside/inside the target project, then give the coding agent the matching bootstrap prompt:

- [Generic](prompts/bootstrap/GENERIC.md)
- [Claude Code](prompts/bootstrap/CLAUDE_CODE.md)
- [Codex](prompts/bootstrap/CODEX.md)
- [OpenCode](prompts/bootstrap/OPENCODE.md)
- [Gemini CLI](prompts/bootstrap/GEMINI_CLI.md)

Example:

```text
Read agentic-flow-framework/prompts/bootstrap/CLAUDE_CODE.md and apply it to this project.
Do not execute product work yet; only bootstrap and validate the agent operating layer.
```

The bootstrap agent reads the latest canonical architecture and generates only the minimum vendor adapter. It must not copy the whole framework into permanent context.

### 2. Classify governance before creating ceremony

Use the minimum level that preserves safety:

| Level | Use for | Lifecycle |
|---|---|---|
| `HIGH` | architecture, persistence, production/security/trust, durable data, major public contracts | draft → supervisor → freeze → separate apply → evidence → independent closure |
| `MEDIUM` | bounded same-task correction | owner-approved amendment → bounded apply → tests/evidence → independent closure |
| `EVIDENCE_ONLY` | docs/evidence/test-contract correction with no new runtime authority | durable approved amendment + hash/ref; no separate freeze/apply unless execution follows |

The boundaries that remain mandatory are in [`ARCHITECTURE.md`](ARCHITECTURE.md) and [`schemas/AMENDMENT.md`](schemas/AMENDMENT.md).

### 3. Draft/apply a material task

Use:

- [`prompts/workflow/DRAFT_TASK.md`](prompts/workflow/DRAFT_TASK.md)
- [`schemas/TASK_CONTRACT.md`](schemas/TASK_CONTRACT.md)
- [`prompts/workflow/APPLY_TASK.md`](prompts/workflow/APPLY_TASK.md)

A draft is not execution permission. If execution disproves scope/strategy/prerequisites, STOP and classify an amendment instead of silently rewriting the task.

### 4. Review with a separate supervisor

#### Direct repository/tool access — preferred for high assurance

Use [`prompts/supervisor/DIRECT_ACCESS.md`](prompts/supervisor/DIRECT_ACCESS.md). The separate human/model/session inspects actual source/diff/tests/evidence and stays read-only during the review pass.

#### Evidence-only supervisor

Use [`prompts/supervisor/EVIDENCE_ONLY.md`](prompts/supervisor/EVIDENCE_ONLY.md). Supply [`schemas/EVIDENCE_PACKET.md`](schemas/EVIDENCE_PACKET.md). Anything not provable from the packet stays `UNVERIFIED_FROM_PACKET`.

If an expensive/stronger model performs review, store the compact durable decision—not its transcript or private reasoning—under the project's judgment store. Future tasks read it only when a decision dependency exists.

## Token/context efficiency

For long, expensive or multi-agent work load [`token-efficiency`](skills/token-efficiency/SKILL.md).

The hierarchy is:

```text
mechanical/deterministic tools
→ bounded affected/dependency graph
→ cheap read-only discovery/partitions when checkable
→ compact evidence handoff
→ standard executor
→ stronger judgment only on escalation
```

Never weaken DoD/tests/security just to save tokens.

### Waste warnings

The agent must emit `TOKEN_WASTE_WARNING` when it observes material, unjustified patterns such as:

- whole-repo scan without dependency/scope reason;
- repeated large-file rereads;
- full historical task/judgment trail loaded during ordinary execution;
- huge raw logs read instead of filtered slices;
- strong/expensive model doing mainly mechanical discovery;
- overlapping subagents scanning the same surface;
- more than two failed loops without new discriminating evidence;
- soft/hard task budget overrun.

The warning names the evidence, a cheaper/smaller alternative, and the quality guard. Hard-budget breach or any quality tradeoff requires operator/judgment approval.

### Usage ledger

When usage counters are observable, record privacy-safe events with [`schemas/USAGE_EVENT.md`](schemas/USAGE_EVENT.md) and the portable CLI:

```bash
python3 scripts/usage_ledger.py record \
  --task-id TASK-123 \
  --phase EXECUTION \
  --role EXECUTION_TIER \
  --provider anthropic \
  --model '<observable-model>' \
  --source API_USAGE \
  --input-tokens 12000 \
  --output-tokens 1800

python3 scripts/usage_ledger.py report --task-id TASK-123
python3 scripts/usage_ledger.py report
```

Only record values the provider/harness exposes. Missing telemetry is **unknown, not zero**. Cost is optional because hosted products/providers expose billing differently.

Current primary sources support this design: Anthropic documents separate usage counters for uncached input, cache creation/read, output and tool usage; its tool-context guidance recommends lazy tool search, programmatic/batched tool calling, prompt caching and context editing for different sources of context bloat. OpenAI's agent-first harness report similarly uses short maps plus versioned active/completed plans instead of permanent giant history in context. citeturn438345search1turn438345search4turn438345search0

## Large frontend / monorepo workflow

Do not solve context limits by feeding a bigger model the entire repository.

```text
mechanical dependency/affected graph
→ EDIT/REFERENCE/EXCLUDED/CHECK sets
→ cheap read-only discovery child
→ compact handoff
→ bounded implementation
→ local/affected tests
→ stronger judgment only on escalation
```

Use [`context-curation`](skills/context-curation/SKILL.md), [`model-routing`](skills/model-routing/SKILL.md), and `token-efficiency` when cost/context is material.

## Skills and why rare use can be correct

See [`skills/00_INDEX.md`](skills/00_INDEX.md).

Yara telemetry showed repeated observed-association mainly around task contracts, model routing, diagnose-before-fix, and sibling/fix auditing. Those are broad procedures. Risk-specific skills such as live verification, mutation proof, or concurrency/stress should be rare if their risks are rare.

Do not rank skills by activation count alone. Use eligible-trigger denominator, activation correctness, outcome/evidence quality, rework/regression impact, token/cost effect when observable, and controlled fixtures for causal claims.

## Durable project state without history pollution

Recommended target layout: [`schemas/PROJECT_LAYOUT.md`](schemas/PROJECT_LAYOUT.md).

Normal execution reads **hot state** only: current task/amendment/checkpoint/index and directly relevant docs. Completed tasks, judgments, evidence, usage events, the execution ledger, retrospectives and stories are **cold history** and are loaded only on provenance/audit/regression/storytelling triggers.

This preserves expensive supervisor decisions and a full project trail without making each new agent pay to reread that trail.

## Formal execution retrospective

For long campaigns/rescues/migrations, use a compact append-only boundary ledger rather than waiting until the end to excavate everything from scratch:

- schema: [`schemas/EXECUTION_RETROSPECTIVE_LEDGER.md`](schemas/EXECUTION_RETROSPECTIVE_LEDGER.md)
- cold skill: [`skills/project-retrospective/SKILL.md`](skills/project-retrospective/SKILL.md)
- prompt: [`prompts/workflow/BUILD_PROJECT_RETROSPECTIVE.md`](prompts/workflow/BUILD_PROJECT_RETROSPECTIVE.md)

Recommended project file:

```text
.agentic/history/EXECUTION_LEDGER.jsonl
```

Append only meaningful boundaries such as review, amendment, freeze, apply, STOP, evidence-ready and closure. Each row contains short counters/pointers—not narrative, raw logs, prompts or transcripts.

The final retrospective can then reconstruct, where evidence permits:

```text
tasks closed
amendment loops
independent reviews
pre-closure defects caught
STOP conditions triggered
false-complete states prevented
implementation commits
evidence/governance commits
tests and suite-count evolution
production/testenv mutations
provider calls/spend/token usage
deferred findings
governance overhead and method evolution
```

Every historical claim is classified as:

```text
PROVEN FROM GIT / DURABLE ARTIFACTS
RECONSTRUCTED FROM OWNER JOURNAL / RECEIPTS
UNKNOWN / NOT LOGGED RELIABLY
```

Early incomplete logging is reported honestly; exact counts are never fabricated.

## Project history, storytelling and self-branding

`project-retrospective` and `project-storytelling` are deliberately separate.

- `project-retrospective` is audit-grade reconstruction: timeline, metrics, truth classes, governance value/overhead.
- `project-storytelling` turns verified/reconstructed evidence into architecture narrative, case study, lessons learned and portfolio/self-branding content.

When a retrospective exists, storytelling should consume that bounded report/index first instead of rereading all completed tasks and judgments.

Generated retrospectives live under cold `retrospectives/`; generated stories under cold `stories/`. Neither becomes permanent coding-agent context.

## Documentation freshness

Canonical/index/retrospective/story documents should carry a version and update timestamp. Material verified changes use [`documentation-freshness`](skills/documentation-freshness/SKILL.md) before closure. Update the authoritative source first, then regenerate/synchronize projections/adapters.

OpenAI's published Codex harness experience similarly treats repository docs/plans as versioned system-of-record artifacts, uses progressive disclosure, and performs recurring doc-gardening rather than relying on chat history. citeturn438345search0

## Repository map

```text
ARCHITECTURE.md          canonical policy/source of truth
schemas/                 task/amendment/evidence/supervisor/usage/history contracts
skills/                  portable on-demand skills
prompts/bootstrap/       generate vendor adapters from latest architecture
prompts/workflow/        draft/amend/apply/evidence/usage/retrospective workflows
prompts/supervisor/      independent review prompts
scripts/                 portable local control-plane utilities
research/                dated primary-source research, not policy
templates/               optional examples
adapters/                 adapter-generation guidance
```

## Research basis

Current dated research notes:

- [`research/2026-09-09-context-model-routing.md`](research/2026-09-09-context-model-routing.md)
- [`research/2026-09-09-bootstrap-supervision.md`](research/2026-09-09-bootstrap-supervision.md)
- [`research/2026-09-09-adaptive-governance-token-efficiency.md`](research/2026-09-09-adaptive-governance-token-efficiency.md)

Prefer primary/current sources: official vendor docs, official engineering reports, standards/compiler/build-system documentation. Product-specific model names/defaults/pricing/CLI behavior must be rechecked when they materially affect a decision.
