# Target Project Durable Layout

**Schema version:** 1.5  
**Updated:** 2026-09-09T11:30:00Z

A target project may adapt names, but responsibilities should remain distinct. Reuse existing equivalent stores rather than creating shadow state.

```text
.agentic/
├── PROJECT_PROFILE.yaml        # HOT-ish: compact stable baseline/guardrails
├── CURRENT.md                  # HOT: recovery pointer only
├── INDEX.md                    # HOT: compact pointers, no long history
├── overrides/
│   ├── ACTIVE_INDEX.md         # HOT only when active exceptions exist
│   └── <override-id>.yaml      # schemas/TEMPORARY_OVERRIDE.md artifacts
├── production/
│   ├── PROFILE.yaml            # current schemas/PRODUCTION_PROFILE.md posture artifact
│   ├── GAP_INDEX.md            # compact open-gap pointers
│   └── gaps/                   # schemas/OPERATIONAL_GAP.md artifacts
├── tasks/
│   ├── active/                 # HOT
│   └── completed/              # COLD concise task summaries/contracts
├── classifications/
├── amendments/
├── authorizations/
├── evidence/
├── reports/
├── judgments/
│   └── INDEX.md
├── decisions/
│   └── INDEX.md
├── runbooks/
│   └── INDEX.md
├── incidents/
│   └── INDEX.md
├── usage/
│   ├── events.jsonl
│   └── SUMMARY.md
├── checkpoints/
├── history/
│   ├── EXECUTION_LEDGER.jsonl
│   └── PROJECT_TIMELINE.md
├── retrospectives/
├── stories/
└── README.md
```

## Baseline vs reality

`PROJECT_PROFILE.yaml` defines durable project expectations/permissions: testing policy, readiness tier, environment authority, required operating controls and architecture-pattern governance. It is **not** proof that those controls are satisfied.

`production/PROFILE.yaml`, open gaps, receipts and reports reflect current operational reality. A project may require `backup: REQUIRED` while the current gap says restore capability is `UNVERIFIED`.

Temporary deviations from the baseline live under `overrides/` and conform to `schemas/TEMPORARY_OVERRIDE.md`. An override is not a permanent baseline edit. Material overrides have owner/reason/expiry/risk/compensating-controls/restore verification; expired unresolved overrides become visible gaps or require explicit renewal.

## Hot-state rule

Normal execution may preload only:

- `PROJECT_PROFILE.yaml` or the relevant bounded section;
- `CURRENT.md` / `INDEX.md`;
- current task/amendment/classification;
- active override pointers when relevant;
- production profile + open-gap pointers only when current work affects production posture;
- directly relevant evidence/report/decision/runbook pointers;
- canonical architecture, selected verification/production profiles and triggered Skills.

Do **not** recursively read completed tasks, historical overrides/gaps/incidents/runbooks/judgments/evidence/reports/usage/history/retrospectives/stories or the entire profile/Skill shelf unless a trigger requires them.

## Artifact relationships

```text
PROJECT_PROFILE.yaml             desired baseline / permissions
  -> ACTIVE OVERRIDES            temporary deviations
  -> PRODUCTION PROFILE          current operating posture
       -> OPEN GAPS              missing/partial/unverified reality

TASK
  -> CLASSIFICATION / PROFILE IMPACT
  -> AUTHORIZATION / AMENDMENT
  -> EVIDENCE PACKET
  -> STATUS REPORT
  -> SUPERVISOR JUDGMENT
  -> PROFILE/GAP/OVERRIDE UPDATE only when receipts justify it
  -> CHECKPOINT / EXECUTION LEDGER boundary
```

Reference authoritative artifacts rather than duplicating the same status prose in every file.

## Midstream adoption

When Agentic Flow is introduced during active coding, the adoption snapshot records real branch/HEAD/dirty paths/current task/tests/environment mutations before any framework-driven product mutation. Existing work is preserved/reconciled and is never retroactively claimed as reviewed or authorized by this framework.

## Production / verification artifacts

- `production/PROFILE.yaml` records current scale/tier/runtime/recovery/observability/security/resilience posture.
- `production/gaps/` records absent/partial/unverified/accepted-risk operating capabilities.
- `runbooks/` stores tested deployment/rollback/recovery/troubleshooting procedures; load only the relevant runbook.
- `incidents/` stores bounded incident summaries; raw telemetry stays in the telemetry system.
- `classifications/`, `evidence/` and `reports/` preserve claim-aware task truth bound to ref/artifact/environment.
- deterministic repository validators may check mechanical contradictions, but they do not replace runtime receipts.

## Cold-history rule

Completed tasks, expired/historical overrides, closed gaps, evidence/reports/judgments/incidents/usage/retrospectives/stories remain durable and indexed but open only for regression, provenance, audit, incident investigation, architecture history, retrospective/storytelling, token/cost analysis or explicit request.

## Artifact rules

- Do not store private chain-of-thought, raw transcripts, full model prompts/responses, secrets or large raw log archives.
- Evidence contains observable receipts rather than confident summaries only.
- Reports distinguish `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED` and preserve skipped/not-run checks.
- Gaps distinguish `NOT_IMPLEMENTED / PARTIAL / UNVERIFIED / BLOCKED / ACCEPTED_RISK / CLOSED`.
- Reviewer judgment does not substitute for missing behavioral/deployment/restore/security receipts.
- Missing usage telemetry is unknown, never zero.
- `CURRENT.md` is a recovery pointer, not a second policy/task board.
- Canonical/index/profile/report/retrospective/story artifacts carry version/update timestamp where practical.
