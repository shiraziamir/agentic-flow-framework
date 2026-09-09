# Agentic Flow Framework

A repository-first, tool-agnostic operating system for reliable coding agents.

> **Durable project memory; disposable, high-quality working context.**

This GitHub repository is the authoritative home of the framework. The old Google Drive folder is an archived snapshot only.

## What this solves

Coding agents usually fail at scale for reasons beyond raw model intelligence: context pollution, giant instruction files, uncontrolled scope expansion, stale chat memory, expensive models doing mechanical work, weak evidence, and the same agent acting as author, executor and final judge.

This framework adds a small control plane:

```text
request
→ draft task
→ supervisor review
→ freeze
→ apply authorization
→ bounded execution
→ evidence packet
→ independent closure review
→ durable checkpoint
→ fresh context
```

## Source of truth

Read this first:

1. [`ARCHITECTURE.md`](ARCHITECTURE.md) — **canonical policy, authority and lifecycle**.
2. [`schemas/`](schemas/) — task, evidence and supervisor-decision contracts.
3. [`skills/`](skills/) — reusable on-demand procedures.
4. The frozen task contract for the current task.
5. Durable evidence and supervisor decisions.
6. Generated vendor adapters.
7. Conversation memory.

**Vendor files are not authority.** `CLAUDE.md`, OpenCode config, Gemini context files, subagent definitions, or generated `AGENTS.md` variants are projections of the canonical architecture.

## Quick start

### 1. Clone or reference the framework

Make this repository available beside or inside the project you want an agent to work on.

### 2. Bootstrap your agent

Give the coding agent the matching bootstrap prompt:

- [Generic](prompts/bootstrap/GENERIC.md)
- [Claude Code](prompts/bootstrap/CLAUDE_CODE.md)
- [Codex](prompts/bootstrap/CODEX.md)
- [OpenCode](prompts/bootstrap/OPENCODE.md)
- [Gemini CLI](prompts/bootstrap/GEMINI_CLI.md)

The bootstrap agent reads the **latest** canonical architecture and generates/updates the minimum vendor-specific files in the target repository. It must not copy the whole framework into permanent context or invent conflicting policy.

Example after cloning:

```text
Read agentic-flow-framework/prompts/bootstrap/CLAUDE_CODE.md and apply it to this project.
Do not execute product work yet; only bootstrap and validate the agent operating layer.
```

### 3. Use the workflow prompts

You do not have to hand-write lifecycle prompts each time:

- [DRAFT TASK](prompts/workflow/DRAFT_TASK.md)
- [AMEND TASK](prompts/workflow/AMEND_TASK.md)
- [APPLY TASK](prompts/workflow/APPLY_TASK.md)
- [BUILD EVIDENCE PACKET](prompts/workflow/BUILD_EVIDENCE_PACKET.md)

A material task should move through:

```text
DRAFT
→ SUPERVISOR REVIEW
→ AMEND if needed
→ FREEZE
→ APPLY AUTHORIZATION
→ EXECUTION
→ EVIDENCE_READY
→ SUPERVISOR CLOSURE
```

A draft is not execution permission. If execution later disproves scope or strategy, the executor must STOP and request amendment rather than silently rewrite the frozen task.

### 4. Choose a supervisor

The supervisor may be a person, a different model, or a separate cold session/harness. Independence is a **role/property of the review**, not a model brand.

#### Supervisor with direct repo/tool access — preferred

Use [the direct-access supervisor prompt](prompts/supervisor/DIRECT_ACCESS.md).

A separate human/model/session reads the actual frozen contract, diff, source, tests and evidence and remains **read-only during the review pass**. It should try to falsify claims, not merely restate the executor's report.

#### Supervisor without repo access

Use [the evidence-only supervisor prompt](prompts/supervisor/EVIDENCE_ONLY.md).

The executor supplies a packet conforming to [`schemas/EVIDENCE_PACKET.md`](schemas/EVIDENCE_PACKET.md): commit/ref identity, changed paths, diff/patch artifact, commands/results, DoD matrix, failures, live receipts, unresolved facts and residual risk.

Anything the supervisor cannot verify from the packet stays `UNVERIFIED_FROM_PACKET`. Missing access never becomes confident approval.

Supervisor decisions can be persisted using [`schemas/SUPERVISOR_DECISION.md`](schemas/SUPERVISOR_DECISION.md).

### 5. Keep lifecycle state durable

A target project may use the portable layout in [`schemas/PROJECT_LAYOUT.md`](schemas/PROJECT_LAYOUT.md):

```text
.agentic/
├── tasks/
├── authorizations/
├── evidence/
├── judgments/
└── checkpoints/
```

If the project already has equivalent durable task/evidence locations, reuse them instead of creating shadow state.

### 6. Close with evidence

Before material closure load `evidence-integrity`. High-risk work should additionally use an `independent-review` pass. Closure maps every frozen DoD item to a receipt. The executor prepares evidence; the supervisor decides closure.

## Skills: why only some fire often

The Yara telemetry that inspired this project showed the strongest repeated **observed-association** signals mainly around:

- model routing/delegation;
- diagnose-before-fix;
- sibling/fix audit;
- task-contract drafting/apply.

That does **not** imply the rest should be deleted. Skills are classified as:

- **CORE** — expected to recur;
- **COMMON** — broad but task-family-specific;
- **RISK_TRIGGERED** — intentionally rare (live stack, mutation proof, concurrency/stress);
- **EXPERIMENTAL** — requires evidence before promotion.

A concurrency skill that activates once in 100 tasks may be exactly correct. Frequency is not causal usefulness. See [`skills/00_INDEX.md`](skills/00_INDEX.md).

## Large frontend / monorepo workflow

Do not solve context limits by feeding a larger model the whole repository.

```text
mechanical dependency/affected graph
→ small EDIT/REFERENCE/EXCLUDED/CHECK sets
→ cheap read-only discovery child
→ compact evidence handoff
→ standard coding tier
→ strong judgment only on escalation
```

Use [`context-curation`](skills/context-curation/SKILL.md) and [`model-routing`](skills/model-routing/SKILL.md). Prefer project graphs, TypeScript project references, import graphs, or build-system affected sets over LLM-wide scans.

## Model tiers

Semantic roles are portable:

```text
T0 deterministic
T1 cheap read-only
T2 standard execution
T3 judgment
```

Map them to models your current harness actually exposes. Model names are configuration, not authority. Benchmark cheap routing on frozen fixtures before making it a default.

## Repository map

```text
ARCHITECTURE.md          canonical source of truth
schemas/                 task/evidence/judgment/durable-layout contracts
skills/                  portable on-demand skills
prompts/bootstrap/       prompts that generate vendor adapters
prompts/workflow/        executable lifecycle prompts
prompts/supervisor/      independent review prompts
templates/               routing/context examples
research/                dated source research, not policy
adapters/                 adapter-generation guidance
```

## Updating the framework

Research notes may inform changes, but policy changes belong in `ARCHITECTURE.md`, schemas, and skills. Generated adapters should then be regenerated.

Prefer current primary sources: official vendor documentation, official engineering reports, standards/compiler/build-system documentation. Label inference and uncertainty.

## Primary-source basis

The design is derived from Yara's real agent-control workflow and checked against current primary material including OpenAI's harness-engineering report, Claude Code documentation for skills/subagents/cost controls, OpenCode's rules/skills documentation, Gemini CLI context-file documentation, and the Agent Skills ecosystem. Dated evidence belongs under `research/`.
