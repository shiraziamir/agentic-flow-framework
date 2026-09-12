# Getting Started

This guide takes a new operator from “what is this?” to one bounded, reviewable task. Read [Why Agentic Flow](WHY_AGENTIC_FLOW.md) first if the problem is not yet clear.

## Prerequisites

- a target Git repository;
- a coding agent that can read repository files and run the project’s normal tools;
- at least one safe environment capable of exercising the behavior you intend to change;
- an operator who can decide task, mutation and environment authority.

Agentic Flow is documentation, schemas, prompts and deterministic helpers. It is not an orchestration service and does not create production credentials or environments.

## 1. Place and pin the framework

Keep the framework beside the target repository, or use the portable bundle. For higher-assurance projects, pin a reviewed tag/commit.

```text
workspace/
├── agentic-flow-framework/
└── target-project/
```

## 2. Start read-only

Ask the target project’s coding agent to read `docs/agent/START_HERE.md` and `ARCHITECTURE.md`, then inspect the project without mutation. If work is already underway, it must follow `docs/agent/MIDSTREAM_ADOPTION.md` and preserve the branch, HEAD, dirty paths, current task, tests already run and environment mutations.

## 3. Establish the project profile

Copy the shape from `templates/PROJECT_PROFILE.example.yaml` into:

```text
target-project/.agentic/PROJECT_PROFILE.yaml
```

Confirm:

- project surfaces and readiness tier;
- `STRICT_PREVIEW` or another explicit mutation policy;
- required test layers;
- execution-readiness requirements;
- permissions for local, ephemeral, shared, staging and production environments;
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

Start separate sessions/identities where practical:

1. Designer uses [the initial prompt](../prompts/operator/TASK_DESIGNER.md) and reads an identified repository ref.
2. Manager uses [the review prompt](../prompts/operator/MANAGER_REVIEWER.md), checks repository reality and freezes only an adequate task.
3. Executor works from the frozen task, performs the implementation-design preflight, and waits for the required mutation approval.
4. Executor implements and verifies on an isolated branch/PR.
5. Manager reviews the exact base/head diff, surrounding source and raw receipts before approving closure/merge.

Use [Designer/Manager Setup](operator/DESIGNER_MANAGER_SETUP.md) for permission details. If one role lacks Git access, use a [bounded context packet](operator/CONTEXT_PACKET.md).

## 6. Preserve authority boundaries

Keep four questions separate:

| Boundary | Question |
|---|---|
| task authority | What outcome and scope are approved? |
| mutation authority | What files/resources may change in this batch? |
| environment authority | Where may the agent run/read/deploy/mutate? |
| closure evidence | What current receipt establishes each claim? |

Under `STRICT_PREVIEW`, the Executor reports current state, proposed state, affected resources, impact, checks, recovery and out-of-scope items, then waits for `APPROVE/APPLY`. A frozen task is not blanket mutation or production authority.

## 7. Run one task

Follow [the worked example](examples/END_TO_END_TASK.md). Keep the first adoption small but real: choose a bounded change with an observable path and a disposable integration environment.

## 8. Validate the framework checkout

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
