# Getting Started

This guide takes a new operator from “what is this?” to a coherent project baseline and one bounded, reviewable task.

## Prerequisites

- a target Git repository;
- a coding agent that can read repository files and run normal project tools;
- an operator who can decide product, task, mutation, environment and production authority;
- for behavior work, at least one safe environment capable of exercising the changed path.

Agentic Flow is documentation, schemas, prompts and deterministic helpers. It is not an orchestration service and does not create production credentials or environments.

## 1. Place and pin the framework

Keep the framework beside the target repository, or use the portable bundle. For higher-assurance projects, pin a reviewed tag/commit.

```text
workspace/
├── agentic-flow-framework/
└── target-project/
```

## 2. Start read-only

Ask the agent to read `docs/agent/START_HERE.md` and inspect the project without mutation. If work is already underway, follow `docs/agent/MIDSTREAM_ADOPTION.md` and preserve branch, HEAD, dirty paths, current task, tests and environment mutations.

## 3. Choose the project mode

Do this before serious coding:

```text
VIBE_PROTOTYPE  → learn fast; provisional/sacrificial code; not production baseline
PRODUCT_BUILD   → establish product/eval/architecture baseline before broad feature work
MAINTENANCE     → existing trustworthy baseline; normal task flow
```

If the project is greenfield, early-stage, architecture is untrusted, or the operator mainly knows the product outcome, read [Project Inception & Architecture Discovery](agent/PROJECT_INCEPTION_ARCHITECTURE.md) and use the [Project Architect prompt](../prompts/operator/PROJECT_ARCHITECT.md).

Do not jump directly from a product idea to a technology stack.

## 4. If using Vibe mode

Vibe mode is explicitly supported:

```yaml
project_mode:
  mode: VIBE_PROTOTYPE
```

Use it for fast questions like “can this interaction work?” or “is this provider useful?”. It is allowed to be provisional and even disposable.

But:

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
```

Before moving to `PRODUCT_BUILD`:

1. preserve useful learnings/evals;
2. establish product constraints and quality/eval contract;
3. run architecture discovery;
4. define security/data boundaries;
5. classify prototype code as `REUSE_AS_IS | REUSE_AFTER_REVIEW | REWRITE | DISCARD`;
6. build the intended product walking skeleton;
7. pass an architecture checkpoint.

## 5. Establish the project profile

Copy `templates/PROJECT_PROFILE.example.yaml` into:

```text
target-project/.agentic/PROJECT_PROFILE.yaml
```

Confirm:

- `project_mode` and promotion rules;
- `swamp_guard` behavior;
- project surfaces/readiness tier;
- mutation/remediation policy;
- test and execution-readiness requirements;
- local/test/staging/production permissions;
- role-specific access;
- review independence;
- model/cost routing;
- production rollback/forward-recovery requirements;
- operational/security expectations.

The profile says what should be true. It is not proof those capabilities exist.

## 6. Run Product Inception before broad feature work

For new/unclear projects, the normal sequence is:

```text
PRODUCT INTENT
→ PRODUCT BRIEF
→ QUALITY / EVAL CONTRACT
→ ARCHITECTURE DISCOVERY
→ 2–3 MINIMAL OPTIONS when useful
→ LOAD-BEARING DECISIONS
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PROJECT BASELINE
```

The Product Owner should decide business trade-offs—not low-level technologies they do not need to own.

Freeze hard-to-change invariants such as data/security boundaries, provenance/version/delete semantics, public contracts and recovery expectations. Keep easy experiment variables open until evidence supports them.

For AI/RAG/search systems, create a representative eval set before serious tuning. Do not choose/tune chunking, vector vendor, embedding model, top-k, reranker or prompts only from demo impressions.

## 7. Keep the Swamp Guard active

At material checkpoints classify:

```text
CLEAR | WATCH | ALERT | STOP_REBASELINE
```

Typical alerts:

- repeated redesign/rework in the same subsystem;
- tooling/framework/datastore proliferation without product need;
- multiple mechanisms competing for one responsibility;
- tuning without evals;
- features growing before the critical end-to-end path works;
- architecture decisions trapped in chat;
- source-of-truth/state ownership ambiguity;
- prototype code quietly acquiring production expectations.

`STOP_REBASELINE` means local patches are no longer the right fix. Stop, restore a coherent architecture baseline, then continue.

## 8. Confirm execution readiness

Before behavior-changing work, name the planned closure claims and ask what environment can directly prove each one.

```text
Claim: transaction rollback works against PostgreSQL
Adequate: real app + disposable PostgreSQL + actual transaction path
Inadequate alone: mocked connection returning expected calls
```

Use the lowest adequate authorized environment. If none exists, request it, narrow the claim honestly, or leave it `UNVERIFIED/BLOCKED`.

## 9. Separate roles for material work

Use separate sessions/identities where practical:

1. **Project Architect** — greenfield/product architecture discovery, no product mutation.
2. **Designer** — task contract + engineering advisory.
3. **Manager** — reviews/freezes tasks and controls bounded authority.
4. **Executor** — implements on an isolated branch/PR and produces receipts.
5. **Cold reviewer** — read-only quality filter for MEDIUM/HIGH when useful.
6. **Independent Judge** — read-only closure for HIGH when required.
7. **Operator** — product, business, risk and production authority.

Copy-ready prompts:

- [Project Architect](../prompts/operator/PROJECT_ARCHITECT.md)
- [Task Designer](../prompts/operator/TASK_DESIGNER.md)
- [Manager / Reviewer](../prompts/operator/MANAGER_REVIEWER.md)
- [Independent Judge](../prompts/operator/INDEPENDENT_JUDGE.md)

## 10. Preserve authority and evidence boundaries

Keep task, mutation, environment, external-effect, production and closure-evidence authority separate.

Under `STRICT_PREVIEW`, the Executor reports current state, proposed state, affected resources, impact, checks, recovery and out-of-scope items, then waits for `APPROVE/APPLY`.

Different models agreeing does not upgrade the evidence class. Independent closure separates implementation, context, authority and evidence.

## 11. Prefer one consolidated remediation round

For MEDIUM/HIGH work, aim for:

```text
implementation
→ cold/adversarial review
→ Manager consolidated findings
→ one bounded remediation round
→ final review
```

A second iteration is exceptional and requires a new material finding within the configured maximum. Repeated remediation is also a Swamp Guard signal.

## 12. Make the repository the handoff bus

```text
Human transports authority.
Repository transports engineering state.
```

A durable checkpoint should make project mode/baseline, current task, base/head identity, findings, remediation state, receipts/gaps and next authority decision recoverable. A fresh session should continue from repository state instead of replaying old chat.

## 13. Production remains separate

Production mutation is not implied by source approval, prototype success or Judge PASS. Before every production change require exact target/change identity, health/success signals, abort condition, rollback or forward-recovery path, state/data constraints, recovery authority and post-change verification.

## 14. Validate the framework checkout

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```

These checks validate repository mechanics, not the effectiveness of the framework in your organization.

## What to read next

- [Project Inception](agent/PROJECT_INCEPTION_ARCHITECTURE.md)
- [Task Workflow](agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md)
- [Comparison](COMPARISON.md)
- [Validation Status](VALIDATION_STATUS.md)
- [Comprehensive Persian Guide](GUIDE.fa.md)
- [Canonical Architecture](../ARCHITECTURE.md)
