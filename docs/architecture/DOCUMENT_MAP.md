# Documentation Map

## Newcomer route

Do **not** read the repository tree from top to bottom.

For a human/operator, start with only:

```text
1. README.md
2. docs/GETTING_STARTED.md
3. docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
4. docs/GUIDE.fa.md            # Persian reader
```

For an Executor agent, start with only:

```text
1. docs/agent/START_HERE.md
2. current project profile + current task
```

Then load a schema, production profile, verification profile, prompt or skill only when the active task triggers it.

## Authority hierarchy

```text
ARCHITECTURE.md      canonical framework policy
schemas/             durable contracts
verification/        claim/change verification profiles
production/          environment/production-readiness profiles
skills/              lazy procedures
current project/task approved state
receipts/gaps/overrides/judgments
```

Reader guides explain the system; they do not override canonical policy.

## Directory purpose

```text
README.md                 human landing page
ARCHITECTURE.md           canonical policy; not required for first read
schemas/                  contracts loaded when relevant
verification/             task verification detail; cold by default
production/               production/environment detail; cold by default
skills/                   on-demand procedures
prompts/                  copy-ready role/workflow prompts
docs/agent/               Executor/adoption workflow
docs/operator/            advanced human setup and role separation
docs/architecture/        explanatory architecture docs
docs/references/          external source provenance
docs/examples/            worked examples
research/                 dated research/history; non-canonical
scripts/                  deterministic lint/build/helpers
templates/                starting examples
bundle/                   portable bundle support
adapters/                 vendor/harness adapters; non-authoritative
```

## What to ignore initially

A newcomer normally does not need to read every schema, unrelated production/verification profiles, `research/`, generated/exported root documents, provider-specific adapters or historical changelog details.

The framework is designed for progressive disclosure: **small entrypoint, triggered detail**.
