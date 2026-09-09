# Operator Guide — Using the Python Tools

**Operator-facing. Coding agents should load this only when a task actually uses these tools.**

The Python scripts in `scripts/` are deterministic helpers. Their purpose is to check facts that do not require model judgment and to build/verify the portable bundle.

They do **not** prove that an application is secure, production-ready, recoverable, correctly deployed, or behaviorally correct. Those claims still require the appropriate runtime/test/security/recovery receipts.

## Requirements

Python 3.11+ is recommended. CI currently validates the tools with Python 3.13.

JSON input uses only the Python standard library. YAML input for the linters requires PyYAML.

## 1. Verification artifact linter

Script:

```text
scripts/verification_lint.py
```

Use it to detect mechanical contradictions in task/evidence/status artifacts, such as:

- a `VERIFIED` claim with no evidence reference;
- a receipt tied to a stale repository ref;
- a receipt weaker than the task's frozen minimum;
- `UNKNOWN` combined with `VERIFIED`;
- a DoD item marked PASS without evidence;
- broad/global wording without an exhaustive bounded receipt.

Run:

```bash
python3 scripts/verification_lint.py path/to/task-or-evidence.json
```

Multiple files:

```bash
python3 scripts/verification_lint.py file1.json file2.json file3.json
```

Treat warnings as failures:

```bash
python3 scripts/verification_lint.py --strict file.json
```

YAML, when PyYAML is available:

```bash
python3 scripts/verification_lint.py evidence.yaml
```

Self-test the checker:

```bash
python3 scripts/test_verification_lint.py
```

Expected repository self-test result: six test scenarios pass.

### What it does not prove

It cannot decide whether a real-world test is semantically sufficient, whether the UI truly works, whether production received the artifact, or whether security is adequate.

## 2. Production-readiness profile/gap linter

Script:

```text
scripts/production_readiness_lint.py
```

Use it to catch deterministic contradictions in production profiles and operational gaps, for example:

- HIGH-criticality durable data without required backup/restore/RPO/RTO declarations;
- `STANDARD` or `HIGH_ASSURANCE` without required metrics/logs/vulnerability-management declarations;
- user-facing `HIGH_ASSURANCE` without SLO requirement;
- HIGH_ASSURANCE without failure-mode analysis, recovery drill or threat model requirement;
- accepted risk without owner/accepting authority;
- a CLOSED gap without evidence references.

Run:

```bash
python3 scripts/production_readiness_lint.py .agentic/production/PROFILE.yaml
```

Check profile plus gaps:

```bash
python3 scripts/production_readiness_lint.py \
  .agentic/production/PROFILE.yaml \
  .agentic/production/gaps/*.yaml
```

Strict mode:

```bash
python3 scripts/production_readiness_lint.py --strict <files...>
```

Self-test:

```bash
python3 scripts/test_production_readiness_lint.py
```

Expected self-test result: six scenarios pass.

### What it does not prove

It does not prove backup restore success, SLO health, useful observability, runtime security, successful deployment, or actual production readiness.

## 3. Agent Bundle builder

Script:

```text
scripts/build_agent_bundle.py
```

Use it from the framework repository root to build the portable distribution:

```bash
python3 scripts/build_agent_bundle.py
```

Default output:

```text
dist/agentic-flow-agent-bundle.zip
```

Custom output:

```bash
python3 scripts/build_agent_bundle.py \
  --output dist/my-agentic-flow-bundle.zip
```

Self-test the builder logic:

```bash
python3 scripts/test_build_agent_bundle.py
```

The builder creates a deterministic ZIP layout, copies root entry files, and writes `BUNDLE_MANIFEST.json` containing source file paths, SHA-256 hashes and byte counts.

The GitHub Action performs an additional **full-checkout** verification after the self-test; that CI receipt is stronger than running only the synthetic builder self-test.

## 4. Usage ledger helper

Script:

```text
scripts/usage_ledger.py
```

Use this only when the agent provider/harness exposes observable usage numbers. Never invent token/cost values.

Record an event:

```bash
python3 scripts/usage_ledger.py record \
  --task-id TASK-123 \
  --phase APPLY \
  --role EXECUTION_TIER \
  --provider example-provider \
  --model example-model \
  --input-tokens 1200 \
  --output-tokens 300 \
  --tool-calls 4
```

Generate a report:

```bash
python3 scripts/usage_ledger.py report
```

Report one task:

```bash
python3 scripts/usage_ledger.py report --task-id TASK-123
```

Default durable path:

```text
.agentic/usage/events.jsonl
```

The ledger stores counters/metadata, not prompts, responses, reasoning or transcripts.

## 5. Recommended local release check

Before publishing framework changes:

```bash
python3 -m py_compile \
  scripts/verification_lint.py \
  scripts/production_readiness_lint.py \
  scripts/usage_ledger.py \
  scripts/build_agent_bundle.py

python3 scripts/test_verification_lint.py
python3 scripts/test_production_readiness_lint.py
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

Then let GitHub Actions rebuild and verify the bundle from a clean checkout.

## 6. When to use scripts vs. an agent

Use a script/tool for deterministic questions:

```text
Does this artifact have a missing field?
Do these hashes match?
Is the version marker present?
Is a VERIFIED claim missing evidence?
Does the bundle contain the required file?
```

Use agent/human judgment for questions such as:

```text
Is this test actually adequate for the customer behavior?
Is this architecture appropriate?
What is the likely root cause?
Is this security risk acceptable?
Does this restore drill demonstrate the required RPO/RTO?
```

The rule is: automate deterministic truth; spend model judgment on ambiguity.
