# Target Project Durable Layout

**Schema version:** 1.2  
**Updated:** 2026-09-09T08:22:00Z

A target project may use this portable durable state layout. Names can be adapted, but responsibilities should remain distinct. Projects that already have equivalent stores should reuse them instead of creating shadow state.

```text
.agentic/
├── CURRENT.md                 # HOT: recovery pointer only
├── INDEX.md                   # HOT: compact pointers, no long history
├── tasks/
│   ├── active/                # HOT
│   └── completed/             # COLD concise task summaries/contracts
├── amendments/                # COLD except active amendment
├── authorizations/            # COLD except current authorization
├── evidence/                  # COLD except current task packet
├── judgments/                 # COLD; expensive reviews/decisions live here
│   └── INDEX.md               # compact decision lookup
├── decisions/                 # architecture/product decision summaries
│   └── INDEX.md
├── usage/
│   ├── events.jsonl           # append-only provider/harness usage events
│   └── SUMMARY.md             # compact aggregate, timestamped/versioned
├── checkpoints/               # durable resume boundaries
├── history/
│   ├── EXECUTION_LEDGER.jsonl # append-only boundary facts; never preloaded
│   └── PROJECT_TIMELINE.md    # compact dated milestones, not full receipts
├── retrospectives/            # on-demand audit/work-reconstruction reports
├── stories/                   # on-demand case studies/self-branding artifacts
└── README.md
```

## Hot-state rule

Normal execution may preload only:

- `CURRENT.md`;
- `INDEX.md`;
- current task/amendment and directly relevant evidence/decision pointers;
- canonical architecture/instructions required for the current scope.

It must **not** recursively read completed tasks, all judgments, all evidence, the usage ledger, execution ledger, retrospectives, or project stories unless a trigger requires history/audit/provenance.

## Cold-history rule

Completed task/evidence/judgment/usage/retrospective/story artifacts stay durable and indexed. They are opened on demand for:

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

- Do not store chain-of-thought, private deliberation, full prompts, full model responses, or raw transcripts.
- Keep exact task/amendment/contract identity durable.
- Evidence files hold observable receipts, not confident summaries only.
- Judgment files identify review mode: `DIRECT_ACCESS` or `EVIDENCE_ONLY`, model/provider when observable, timestamp, decision, evidence refs, and validity boundary.
- Usage telemetry records only observable counters/flags; missing telemetry is unknown, not zero.
- Retrospective metrics classify facts as `PROVEN`, `RECONSTRUCTED`, or `UNKNOWN`; early incomplete history is never backfilled with invented precision.
- `CURRENT.md` is a recovery pointer, not a second task board or policy source.
- Canonical/index/retrospective/story documents carry version and `Updated` timestamp/date.
