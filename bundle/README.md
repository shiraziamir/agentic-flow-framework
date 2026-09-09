# Agentic Flow Bundle — Read This First

This is the portable distribution of Agentic Flow Framework.

## 1. Where to copy it

Extract the **contents of the `agentic-flow/` directory** from the release ZIP into the target repository as:

```text
<target-repository>/.agentic-flow/
```

After extraction, these paths should exist:

```text
.agentic-flow/README.md
.agentic-flow/START_HERE.md
.agentic-flow/ARCHITECTURE.md
.agentic-flow/VERSION
.agentic-flow/docs/agent/
.agentic-flow/docs/operator/
```

Do not merge the framework files into the application's source folders. Keep `.agentic-flow/` as a distinct framework directory.

## 2. What to tell the coding agent

For a new or idle session, paste:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Do not start or change product work until adoption validation is complete.
```

If coding is already in progress, paste:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Work is already in progress, so follow MIDSTREAM_ADOPTION before further product mutation.
Preserve current edits and do not invent prior review or authorization.
```

A copy-ready prompt also exists at:

```text
.agentic-flow/INSTALL_PROMPT.txt
```

## 3. Which files are for whom

Coding Agent starts with:

```text
START_HERE.md
docs/agent/
```

Human/operator documentation is separate:

```text
docs/operator/
```

Architecture explanation and source provenance are separate and cold by default:

```text
ARCHITECTURE.md
docs/architecture/
PRIMARY_SOURCES.md
docs/references/
```

The presence of operator/reference files in the ZIP does **not** mean the coding agent should preload them.

## 4. Practical workflow

For material changes the normal flow is:

```text
DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION when required
→ APPLY
→ VERIFY + REPORT
→ independent closure when required
```

Read:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

For context and token efficiency read:

```text
docs/agent/TOKEN_EFFICIENT_WORKFLOW.md
```

## 5. Python tools

Operator instructions for the deterministic Python helpers are here:

```text
docs/operator/USING_PYTHON_TOOLS.en.md
docs/operator/USING_PYTHON_TOOLS.fa.md
```

These tools check mechanical invariants and build/verify the bundle. They do not replace behavioral tests, security judgment, restore drills, deployment verification, or human/independent review where required.

## 6. Best practices and sources

English plain-text summary of the practices used:

```text
BEST_PRACTICES_USED.en.txt
```

Primary external sources:

```text
PRIMARY_SOURCES.md
docs/references/PRIMARY_SOURCES.md
```

Canonical framework policy:

```text
ARCHITECTURE.md
```

## 7. Integrity files

The release artifact also contains:

```text
BUNDLE_MANIFEST.json
agentic-flow-agent-bundle.zip.sha256   # supplied next to the bundle by CI
```

`BUNDLE_MANIFEST.json` records the source files, byte counts, and SHA-256 values used to create the portable bundle.
