# Operator Guide — Agentic Flow

**Operator-only document; agents should not preload this file.**  
**Version:** 1.7  
**Updated:** 2026-09-09T11:30:00Z

## Goal

Use Agentic Flow without turning it into ceremony. The operator owns business risk, production authority, accepted risk and major architecture decisions. The agent owns bounded execution inside those guardrails and should surface evidence/gaps rather than hide uncertainty.

## Install / drop-in adoption

Build or obtain the generated Agent Bundle, extract it into a stable project directory such as `.agentic-flow/`, and give the agent one instruction:

```text
Read .agentic-flow/START_HERE.md and adopt Agentic Flow for this repository.
Do not start or change product work until adoption validation is complete.
```

For an already-active coding session, the same root entrypoint will route the agent to midstream adoption. You can also say:

```text
Read .agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md.
Adopt the framework without discarding current edits or fabricating prior review/authorization.
Return the adoption snapshot and conflicts before continuing product mutation.
```

## Project baseline

Create one `.agentic/PROJECT_PROFILE.yaml` from `templates/PROJECT_PROFILE.example.yaml`. Keep it small. It should define the required engineering bar, environment permissions, testing policy, production/readiness expectations and pattern-selection policy. It should not contain task history or large prose.

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

Keep operator documents, research and historical artifacts cold. Do not put this guide into every agent prompt. Strong models should be reserved for judgment/ambiguity; deterministic tools and cheap read-only agents can handle inventory, log reduction and mechanically checkable discovery.

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
