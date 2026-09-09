# Target Project Durable Layout

**Schema version:** 1.4  
**Updated:** 2026-09-09T10:40:00Z

A target project may use this portable durable state layout. Names can be adapted, but responsibilities should remain distinct. Projects that already have equivalent stores should reuse them instead of creating shadow state.

```text
.agentic/
├── CURRENT.md                  # HOT: recovery pointer only
├── INDEX.md                    # HOT: compact pointers, no long history
├── production/
│   ├── PROFILE.yaml            # current schemas/PRODUCTION_PROFILE.md artifact
│   ├── GAP_INDEX.md            # compact open-gap pointers
│   └── gaps/                   # schemas/OPERATIONAL_GAP.md artifacts
├── tasks/
│   ├── active/                 # HOT
│   └── completed/              # COLD concise task summaries/contracts
├── classifications/            # current/archived change-surface classifications
├── amendments/                 # COLD except active amendment
├── authorizations/             # COLD except current authorization
├── evidence/                   # evidence packets + referenced receipts
├── reports/                    # reality-reflecting status/closure/readiness reports
├── judgments/                  # COLD; expensive reviews/decisions live here
│   └── INDEX.md                # compact decision lookup
├── decisions/                  # architecture/product decision summaries
│   └── INDEX.md
├── runbooks/                   # operational/recovery/troubleshooting procedures
│   └── INDEX.md
├── incidents/                  # significant incident summaries/timelines when used
│   └── INDEX.md
├── usage/
│   ├── events.jsonl            # append-only provider/harness usage events
│   └── SUMMARY.md              # compact aggregate, timestamped/versioned
├── checkpoints/                # durable resume boundaries
├── history/
│   ├── EXECUTION_LEDGER.jsonl  # append-only boundary facts; never preloaded
│   └── PROJECT_TIMELINE.md     # compact dated milestones, not full receipts
├── retrospectives/             # on-demand audit/work-reconstruction reports
├── stories/                    # on-demand case studies/self-branding artifacts
└── README.md
```

## Hot-state rule

Normal execution may preload only:

- `CURRENT.md`;
- `INDEX.md`;
- current task/amendment/classification;
- production `PROFILE` + open-gap pointers only when current task can affect production posture;
- directly relevant evidence/report/decision/runbook pointers;
- canonical architecture, selected verification/production profiles and triggered skills required for current scope.

It must **not** recursively read completed tasks, all gaps, incidents, runbooks, judgments, evidence, reports, usage ledger, execution ledger, retrospectives, stories, all Skills or all profiles unless a trigger requires them.

## Artifact relationships

```text
PROJECT PRODUCTION PROFILE
  -> OPEN OPERATIONAL GAPS

TASK
  -> CLASSIFICATION
  -> PRODUCTION IMPACT / GAP REFS
  -> AUTHORIZATION / AMENDMENT
  -> EVIDENCE PACKET
       -> raw/bounded receipt refs
  -> STATUS REPORT
  -> SUPERVISOR JUDGMENT
  -> PROFILE/GAP UPDATE when verified posture changed
  -> CHECKPOINT / EXECUTION LEDGER boundary
```

The same fact should not be rewritten independently into every artifact. Reference the authoritative artifact/hash/ref.

## Production artifacts

- `production/PROFILE.yaml` records scale/tier, runtime, recovery, observability, security/resilience requirements and current gap refs.
- `production/gaps/` records absent/partial/unverified/accepted-risk operational capabilities.
- `runbooks/` stores tested procedures for deployment, rollback, recovery and troubleshooting; routine tasks should open only the relevant runbook.
- `incidents/` stores bounded post-incident timelines/findings when project risk justifies them; raw telemetry remains in its telemetry system.
- production readiness changes are receipts-based. A scanner/config/backup checkbox does not by itself close a gap.

## Verification artifacts

- `classifications/` records `schemas/CHANGE_CLASSIFICATION.md` results when kept separately from the task.
- `evidence/` stores `schemas/EVIDENCE_PACKET.md` packets and referenced small receipts/artifact pointers.
- `reports/` stores `schemas/STATUS_REPORT.md` reality snapshots/readiness reports.
- material JSON/YAML artifacts may be mechanically checked with repository scripts when available.
- report/evidence validity is bound to repository/artifact/environment identity; later material mutation may require reverification/new version.

## Cold-history rule

Completed tasks, closed gaps, evidence/reports/judgments/incidents/usage/retrospectives/stories stay durable and indexed. They are opened on demand for regression, provenance, audit, incident investigation, architecture history, retrospective/storytelling, token/cost analysis or explicit user request.

## Execution ledger

Use `EXECUTION_RETROSPECTIVE_LEDGER.md` for compact boundary entries such as draft review, amendment, freeze, apply start, STOP, evidence-ready, closure review and close. Store pointers/counters, not narrative or raw logs.

## Artifact rules

- Do not store chain-of-thought, private deliberation, full prompts/model responses or raw transcripts.
- Keep exact task/amendment/classification/production-profile identity durable.
- Evidence files hold observable receipts, not confident summaries only.
- Status reports distinguish `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED`, preserve skipped/not-run checks and residual risk.
- Production gaps distinguish `NOT_IMPLEMENTED / PARTIAL / UNVERIFIED / BLOCKED / ACCEPTED_RISK / CLOSED`.
- Judgment files identify review mode/independence, timestamp, decision, evidence refs and validity boundary; judgment does not replace missing behavioral receipts.
- Usage telemetry records observable counters; missing telemetry is unknown, not zero.
- Retrospective metrics classify facts as `PROVEN`, `RECONSTRUCTED` or `UNKNOWN`.
- `CURRENT.md` is a recovery pointer, not a second task board/policy source.
- Canonical/index/profile/report/retrospective/story documents carry version and update timestamp/date where practical.