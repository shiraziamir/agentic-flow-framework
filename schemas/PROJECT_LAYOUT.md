# Target Project Durable Layout

**Schema version:** 1.3  
**Updated:** 2026-09-09T10:04:00Z

A target project may use this portable durable state layout. Names can be adapted, but responsibilities should remain distinct. Projects that already have equivalent stores should reuse them instead of creating shadow state.

```text
.agentic/
├── CURRENT.md                  # HOT: recovery pointer only
├── INDEX.md                    # HOT: compact pointers, no long history
├── tasks/
│   ├── active/                 # HOT
│   └── completed/              # COLD concise task summaries/contracts
├── classifications/            # current/archived change-surface classifications
├── amendments/                 # COLD except active amendment
├── authorizations/             # COLD except current authorization
├── evidence/                   # evidence packets + referenced receipts
├── reports/                    # reality-reflecting status/closure reports
├── judgments/                  # COLD; expensive reviews/decisions live here
│   └── INDEX.md                # compact decision lookup
├── decisions/                  # architecture/product decision summaries
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
- directly relevant evidence/report/decision pointers;
- canonical architecture, selected verification profiles and triggered skills required for current scope.

It must **not** recursively read completed tasks, all classifications, judgments, evidence, reports, usage ledger, execution ledger, retrospectives, stories, all Skills or all verification profiles unless a trigger requires them.

## Artifact relationships

A material current task should be reconstructible through pointers rather than copied prose:

```text
TASK
  -> CLASSIFICATION
  -> AUTHORIZATION / AMENDMENT
  -> EVIDENCE PACKET
       -> raw/bounded receipt refs
  -> STATUS REPORT
  -> SUPERVISOR JUDGMENT
  -> CHECKPOINT / EXECUTION LEDGER boundary
```

The same fact should not be rewritten independently into every artifact. Reference the authoritative artifact/hash/ref.

## Verification artifacts

- `classifications/` records the `schemas/CHANGE_CLASSIFICATION.md` result when kept separately from the task.
- `evidence/` stores `schemas/EVIDENCE_PACKET.md` packets and referenced small receipts/artifact pointers.
- `reports/` stores `schemas/STATUS_REPORT.md` reality snapshots.
- material JSON/YAML artifacts may be mechanically checked with `scripts/verification_lint.py`.
- report/evidence validity is bound to repository/artifact/environment identity; later material mutation may require reverification/new version.

## Cold-history rule

Completed task/evidence/report/judgment/usage/retrospective/story artifacts stay durable and indexed. They are opened on demand for:

- regression or decision provenance;
- audit/compliance;
- architecture history;
- execution retrospective/work reconstruction;
- project storytelling/self-branding;
- token/cost analysis;
- explicit user request.

## Execution ledger

Use [`EXECUTION_RETROSPECTIVE_LEDGER.md`](EXECUTION_RETROSPECTIVE_LEDGER.md) for compact boundary entries such as draft review, amendment, freeze, apply start, STOP, evidence-ready, closure review and close.

The ledger stores pointers and small counters, not narrative. It exists so final retrospectives do not require excavating every artifact from scratch. It is append-only in spirit and COLD by default.

## Artifact rules

- Do not store chain-of-thought, private deliberation, full prompts, full model responses or raw transcripts.
- Keep exact task/amendment/classification/contract identity durable.
- Evidence files hold observable receipts, not confident summaries only.
- Status reports distinguish `OBSERVED / DERIVED / INFERRED / UNKNOWN / CONTRADICTED`, preserve skipped/not-run checks and state residual risk.
- Judgment files identify review mode/independence level, model/provider when observable, timestamp, decision, evidence refs and validity boundary.
- A judgment does not replace missing behavioral receipts.
- Usage telemetry records only observable counters/flags; missing telemetry is unknown, not zero.
- Retrospective metrics classify facts as `PROVEN`, `RECONSTRUCTED` or `UNKNOWN`; early incomplete history is never backfilled with invented precision.
- `CURRENT.md` is a recovery pointer, not a second task board or policy source.
- Canonical/index/report/retrospective/story documents carry version and `Updated` timestamp/date where practical.
