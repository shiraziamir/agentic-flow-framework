# Clone and Adopt Agentic Flow

**Operator guide. Coding agents should not preload this file unless adoption setup requires it.**

## Recommended distribution model

For normal use, treat the Git repository as the primary distribution source. GitHub Actions Artifacts remain release receipts/convenience packages, but they are not expected to appear in the repository file tree.

Clone the framework near the target project:

```bash
git clone https://github.com/shiraziamir/agentic-flow-framework.git
```

Example layout:

```text
workspace/
├── agentic-flow-framework/
└── my-project/
```

You may also keep the framework inside the project under a clearly separated directory such as `.agentic-flow/`, but do not mix framework source files with product source files.

## Prompt to give the coding agent

If the framework is a sibling repository:

```text
Adopt Agentic Flow for this repository.
Framework source: ../agentic-flow-framework
Start by reading ../agentic-flow-framework/docs/agent/START_HERE.md and ../agentic-flow-framework/ARCHITECTURE.md.
Inspect this project read-only first. Do not modify product files, configuration, infrastructure, data, or runtime state yet.
Use STRICT_PREVIEW mutation approval unless this project's existing .agentic/PROJECT_PROFILE.yaml explicitly says otherwise.
Before every mutation batch, tell me:
1. what is true now,
2. what you propose to change,
3. which files/resources will change,
4. behavior/security/data/operations impact,
5. tests/checks you will run,
6. rollback/recovery where relevant,
7. what you will not change.
Then wait for my explicit APPROVE/APPLY before mutating.
If coding is already in progress, follow MIDSTREAM_ADOPTION and preserve current edits.
```

If the framework is inside `.agentic-flow/`, replace the framework paths accordingly.

## First adoption output expected from the agent

Before asking for product-change approval, the agent should return a concise adoption snapshot:

```text
framework version/ref
project branch/HEAD/dirty state
existing agent instructions
existing task/issue
build/test/deploy entrypoints found
project profile status
open conflicts/gaps
recommended mutation approval mode
next proposed change batch: none until requested/approved
```

## Strict preview mode

`STRICT_PREVIEW` is useful when the operator wants visibility and control over every mutation. It does **not** mean asking permission to read files or inspect state.

The agent should group tightly related edits into one batch to avoid line-by-line approval spam.

Example:

```text
CURRENT
- API timeout is 30s in config/app.yaml.
- retry policy is not defined.
- integration test covers success only.

PROPOSED
- change timeout to 10s;
- add bounded retry policy: 2 retries with backoff;
- add timeout/retry integration tests.

WILL CHANGE
- config/app.yaml
- src/provider_client.*
- tests/integration/provider_timeout.*

IMPACT
- external-provider behavior changes;
- no database schema or public API change.

VERIFY
- focused integration tests;
- existing provider test suite;
- static/lint checks.

ROLLBACK
- revert this bounded batch.

OUT OF SCOPE
- provider replacement;
- production deployment;
- database changes.

Awaiting APPROVE/APPLY.
```

## Updating the framework

Because the framework is a normal Git repository, updates are explicit:

```bash
cd agentic-flow-framework
git fetch origin
git pull --ff-only
```

For higher-assurance projects, pin the framework to a reviewed commit/tag instead of automatically tracking the newest `main`.

The target project's durable `.agentic/` state remains project-owned and should not be overwritten merely because the framework repository was updated.
