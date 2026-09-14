# Agentic Flow Bundle — Read This First

This is the portable distribution of Agentic Flow Framework.

## 1. Where to copy it

Extract the **contents of the `agentic-flow/` directory** from the release ZIP into the target repository as:

```text
<target-repository>/.agentic-flow/
```

Expected paths include:

```text
.agentic-flow/README.md
.agentic-flow/START_HERE.md
.agentic-flow/ARCHITECTURE.md
.agentic-flow/VERSION
.agentic-flow/docs/agent/
.agentic-flow/docs/operator/
.agentic-flow/schemas/
.agentic-flow/templates/
```

Keep `.agentic-flow/` separate from application source.

## 2. What to tell the coding agent

New/idle session:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Inspect the repository read-only first. Do not start or change product work until adoption validation is complete.
```

Work already in progress:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Follow MIDSTREAM_ADOPTION before further product mutation.
Preserve current edits and do not invent prior review or authorization.
```

A copy-ready prompt also exists at `.agentic-flow/INSTALL_PROMPT.txt`.

## 3. Choose a practical preset

Do not copy every possible framework option into the project profile.

Start with:

```text
VIBE_FAST
PRODUCT_STANDARD
HIGH_ASSURANCE
```

and override only genuine project differences in `.agentic/PROJECT_PROFILE.yaml`.

Project phase remains separate:

```text
VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE
```

For a normal maintainable product, `PRODUCT_STANDARD` is the default starting point.

## 4. New project / unclear architecture

Do not jump directly from product idea to code. Read:

```text
docs/agent/PROJECT_INCEPTION_ARCHITECTURE.md
```

Normal path:

```text
PRODUCT INTENT
→ PRODUCT / EVAL CONSTRAINTS
→ ARCHITECTURE DISCOVERY
→ SYSTEM TRUTH / DATA AUTHORITY MAP
→ CURRENT SCALE BOUNDARY
→ WALKING SKELETON
→ ARCHITECTURE CHECKPOINT
→ PRODUCT BASELINE
```

When the project needs a System Truth Map, create:

```text
<target-repository>/.agentic/SYSTEM_TRUTH_MAP.yaml
```

from:

```text
templates/SYSTEM_TRUTH_MAP.example.yaml
```

## 5. Which files are for whom

Coding Agent starts with:

```text
START_HERE.md
docs/agent/
```

Human/operator docs are present for the operator:

```text
docs/operator/
```

Reference/research layers are cold by default.

**Presence in the ZIP does not mean coding-agent preload.** The bundle is self-contained for both human and agent, while default working context remains small.

## 6. Practical task workflow

```text
PRIMARY TASK
→ bounded task contract
→ required authorization
→ implementation
→ Local Lens + risk-adaptive System Lens
→ evidence / review
→ one bounded remediation by default
→ independent closure when required
→ separate production authority
```

LOW/local work stays compact. MEDIUM/HIGH and sensitive boundaries use explicit relevant System-Lens dimensions.

Read:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

For material work, prefer separate Designer, Manager and Executor roles. Manager reviews the exact commit/PR head, not only the Executor narrative.

## 7. Evidence and production rules

A behavior-changing Executor must have an authorized environment capable of exercising the real changed path. Mock-only evidence cannot close integration-or-stronger claims.

```text
CI green             != deployed behavior
backup configured    != restore proven
model/reviewer PASS  != runtime evidence
```

Production mutation is separately authorized and requires rollback or explicit forward-recovery readiness before execution.

## 8. Deterministic helpers

Operator instructions:

```text
docs/operator/USING_PYTHON_TOOLS.en.md
docs/operator/USING_PYTHON_TOOLS.fa.md
```

The bundle includes deterministic verification/readiness/documentation helpers, including Dual-Lens wiring checks. These do not replace behavioral tests, security judgment, restore drills, deployment verification or human/independent review where required.

## 9. Sources and canonical policy

```text
ARCHITECTURE.md                    canonical policy
PRIMARY_SOURCES.md                top-level source index alias
docs/references/PRIMARY_SOURCES.md full source index
docs/VALIDATION_STATUS.md         what the framework actually proves / does not prove
```

## 10. Integrity files

The release artifact also contains:

```text
BUNDLE_MANIFEST.json
agentic-flow-agent-bundle.zip.sha256
```

`BUNDLE_MANIFEST.json` records source paths, byte counts and SHA-256 values used to create the portable bundle.
