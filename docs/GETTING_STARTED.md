# Getting Started

This guide takes a new operator from “what is this?” to one bounded, reviewable task. Read [Why Agentic Flow](WHY_AGENTIC_FLOW.md) first if the problem is not yet clear.

## Prerequisites

- a target Git repository;
- a coding agent that can read repository files and run the project’s normal tools;
- at least one safe environment capable of exercising the behavior you intend to change;
- an operator who can decide task, mutation, environment and production authority.

Agentic Flow is documentation, schemas, prompts and deterministic helpers. It is not an orchestration service and does not create production credentials or environments.

## 1. Place and pin the framework

Keep the framework beside the target repository, or use the portable bundle. For higher-assurance projects, pin a reviewed tag/commit.

```text
workspace/
├── agentic-flow-framework/
└── target-project/
```

## 2. Start read-only

Ask the target project’s coding agent to read `docs/agent/START_HERE.md` and inspect the project without mutation. If work is already underway, follow `docs/agent/MIDSTREAM_ADOPTION.md` and preserve branch, HEAD, dirty paths, current task, tests already run and environment mutations.

## 3. Establish the project profile

Copy the shape from `templates/PROJECT_PROFILE.example.yaml` into:

```text
target-project/.agentic/PROJECT_PROFILE.yaml
```

Confirm:

- project surfaces and readiness tier;
- mutation policy and bounded remediation settings;
- required test layers and execution-readiness requirements;
- permissions for local, ephemeral, shared, staging and production environments;
- role-specific access for Designer, Executor, Manager and Independent Judge;
- review independence requirements;
- model/cost routing preferences;
- production rollback/forward-recovery requirements;
- operational/security expectations and temporary-override rules.

The profile says what should be true. It is not proof that those capabilities exist.

## 4. Confirm execution readiness

Before authorizing behavior-changing work, name the planned closure claims and ask what environment can directly prove each one.

```text
Claim: transaction rollback works against PostgreSQL
Adequate: real application + disposable PostgreSQL + actual transaction path
Inadequate alone: mocked connection returning expected calls
```

Use the lowest adequate authorized environment. If none exists, resolve or approve an environment request, narrow the task/claim honestly, or leave it `UNVERIFIED/BLOCKED`. Never let a mock-only pass inherit integration semantics.

## 5. Separate roles for material work

Use separate sessions/identities where practical:

1. **Designer** — read-only task contract + engineering advisory.
2. **Manager** — reviews/freezes the task and controls bounded authority.
3. **Executor** — implements on an isolated branch/PR and produces receipts.
4. **Cold reviewer** — read-only quality filter for MEDIUM/HIGH when useful.
5. **Independent Judge** — read-only closure for HIGH-risk work when required.
6. **Operator** — retains business, risk and production authority.

Copy-ready prompts:

- [Task Designer](../prompts/operator/TASK_DESIGNER.md)
- [Manager / Reviewer](../prompts/operator/MANAGER_REVIEWER.md)
- [Independent Judge](../prompts/operator/INDEPENDENT_JUDGE.md)

Use [Role Setup](operator/DESIGNER_MANAGER_SETUP.md) for Git/permission details. If a role lacks Git access, use a [bounded context packet](operator/CONTEXT_PACKET.md).

## 6. Do not confuse multiple models with independent evidence

Different models or vendors can improve review coverage, but they may share assumptions or accept the same weak test oracle.

```text
model A says PASS
+ model B says PASS
+ model C says PASS
!= stronger behavioral receipt
```

For independent closure, separate four things where risk justifies it:

- **implementation** — Judge did not materially implement the change;
- **context** — Judge inspects task/source/diff/receipts, not only summaries;
- **authority** — Executor cannot self-approve or self-merge material work;
- **evidence** — Judge sees the raw receipt/runtime evidence needed for the claim.

Model diversity is useful defense-in-depth, not an evidence-class upgrade.

## 7. Preserve authority boundaries

Keep these questions separate:

| Boundary | Question |
|---|---|
| task authority | What outcome and scope are approved? |
| mutation authority | What files/resources may change in this batch? |
| environment authority | Where may the agent run/read/deploy/mutate? |
| external-effect authority | May it call real providers/send/deploy? |
| closure evidence | What current receipt establishes each claim? |
| production authority | Who may approve the live change? |

Under `STRICT_PREVIEW`, the Executor reports current state, proposed state, affected resources, impact, checks, recovery and out-of-scope items, then waits for `APPROVE/APPLY`. A frozen task is not blanket mutation or production authority.

## 8. Prefer one consolidated remediation round

For MEDIUM/HIGH work, aim for:

```text
implementation
→ cold/adversarial review
→ Manager consolidated findings
→ one bounded remediation round
→ final review
```

A second iteration is exceptional: require a new material finding, remain inside the configured maximum and do not use it as a substitute for a comprehensive first review.

## 9. Make the repository the handoff bus

The operator should not permanently copy/paste engineering reports between agents.

Use this principle:

```text
Human transports authority.
Repository transports engineering state.
```

A durable checkpoint should make these recoverable:

```text
current task / frozen contract
base + head identity
review findings
active remediation window
receipts / gaps / omitted checks
closure state
next required authority decision
```

Once that checkpoint is durable, a session can be cleared/replaced and the next session can re-read current state. Vendor-specific reset commands are optional adapters, not framework policy.

## 10. Route models by capability and cost, not brand

A project may use a cheaper capable model for execution and stronger reasoning for review/judgment:

```text
Executor          → task-adequate / cost-efficient
Manager           → stronger reasoning when justified
Independent Judge → high reasoning + separate context
```

This is optional and vendor-neutral. Cost optimization never lowers acceptance or evidence requirements.

## 11. Production remains separate

Production mutation is not implied by source approval or Judge PASS.

Before every production change, require:

```text
exact target/change identity
success + health signals
abort condition
rollback OR explicit forward-recovery path
stateful/data constraints
recovery owner/authority
post-change verification
```

The Independent Judge is read-only by default. Production mutation requires separate Operator/project authority.

## 12. Run one task

Follow [the worked example](examples/END_TO_END_TASK.md). Keep the first adoption small but real: choose a bounded change with an observable path and a disposable integration environment.

## 13. Validate the framework checkout

```bash
python3 -m unittest discover -s scripts -p 'test_*.py'
python3 scripts/test_docs_onboarding.py
python3 scripts/build_agent_bundle.py
```

These checks validate repository tooling and packaging, not the effectiveness of the framework in your organization. Record project-specific outcomes separately.

## What to read next

- [Comparison](COMPARISON.md)
- [Validation Status](VALIDATION_STATUS.md)
- [Comprehensive Persian Guide](GUIDE.fa.md)
- [Canonical Architecture](../ARCHITECTURE.md)
