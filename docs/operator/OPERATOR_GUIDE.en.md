# Operator Guide — Agentic Flow

**Operator-only document; agents should not preload this file.**  
**Version:** 1.7  
**Updated:** 2026-09-09

## Goal

Use Agentic Flow without turning it into ceremony. The operator owns business risk, production authority, accepted risk and major architecture decisions. The agent owns bounded execution inside those guardrails and should surface evidence/gaps rather than hide uncertainty.

## Install / drop-in adoption

The portable Artifact contains its own root `README.md`. Extract the `agentic-flow/` directory into the target repository as:

```text
.agentic-flow/
```

Then give the coding agent:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Do not start or change product work until adoption validation is complete.
```

For an already-active coding session, the same root entrypoint routes the agent to midstream adoption. You can also say:

```text
Read .agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md.
Adopt the framework without discarding current edits or fabricating prior review/authorization.
Return the adoption snapshot and conflicts before continuing product mutation.
```

## Project baseline

Create one `.agentic/PROJECT_PROFILE.yaml` from `templates/PROJECT_PROFILE.example.yaml`. Keep it small. It should define the required engineering bar, environment permissions, testing policy, production/readiness expectations and pattern-selection policy. It should not contain task history or large prose.

## Task workflow

For material changes use the project workflow rather than asking the agent to jump straight into code:

```text
DRAFT
→ REVIEW
→ FREEZE / APPLY AUTHORIZATION when required
→ APPLY
→ VERIFY + REPORT
→ independent closure when required
```

The practical agent-facing explanation is:

```text
docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
```

Use the workflow prompts under `prompts/workflow/` for the actual task artifacts. Scale ceremony with risk; do not require HIGH-risk governance for trivial edits.

## Python deterministic tools

The framework ships Python helpers for mechanical checks and bundle generation. The complete command-by-command guide is:

```text
docs/operator/USING_PYTHON_TOOLS.en.md
```

Persian version:

```text
docs/operator/USING_PYTHON_TOOLS.fa.md
```

Typical framework release check:

```bash
python3 scripts/test_verification_lint.py
python3 scripts/test_production_readiness_lint.py
python3 scripts/test_build_agent_bundle.py
python3 scripts/build_agent_bundle.py
```

What the scripts are for:

```text
verification_lint.py
  mechanical contradictions in task/evidence/status artifacts

production_readiness_lint.py
  mechanical contradictions in production profiles/gaps

build_agent_bundle.py
  build the portable ZIP and manifest

usage_ledger.py
  record/report observable provider usage counters when available
```

Do not interpret a linter PASS as proof that behavior, security, deployment, monitoring or restore actually works. The scripts enforce deterministic invariants; real-world claims still need real receipts.

## Operator decisions that should remain explicit

Operator/human authority is normally required for:

- production mutation or destructive data action;
- accepting material security/data/recovery gaps;
- permanent reduction of readiness/security/backup/observability requirements;
- cross-module/public architectural pattern adoption when it materially changes design;
- overriding a frozen HIGH-risk task;
- accepting known failing acceptance gates.

## Temporary exceptions

Do not edit the baseline just because a control must be temporarily suppressed. Use `schemas/TEMPORARY_OVERRIDE.md` with owner, reason, expiry, risk, compensating controls and restore verification. Review expired overrides regularly.

## Environment policy

Prefer the lowest environment able to prove the claim. Enable disposable/ephemeral test environments when practical. Shared staging and production access should use explicit permissions. A request from an agent for an environment is not authorization.

## Review model

For ordinary work, independent closure may be a cold separate model/session. For security, persistence, public contracts, production semantics or major architecture, use a stronger independent reviewer or human where risk warrants it. Reviewers inspect task/diff/raw receipts before the executor narrative when possible.

## Cost/context controls

Read:

```text
docs/agent/TOKEN_EFFICIENT_WORKFLOW.md
```

for the practical execution pattern. Keep operator documents, research and historical artifacts cold during normal coding. Strong models should be reserved for judgment/ambiguity; deterministic tools and cheap read-only agents can handle inventory, log reduction and mechanically checkable discovery.

The operator should treat token savings as an optimization constraint, not permission to lower the evidence bar.

## Periodic operator checks

Periodically ask for:

- project-profile/gap review;
- expired override review;
- restore-test freshness;
- SLO/alert ownership review;
- dependency/security posture review;
- token/cost/waste report where telemetry exists;
- retrospective/governance efficiency review.

Use `project-retrospective` and `project-storytelling` only on demand; they are cold history workflows.
