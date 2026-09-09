# Target Project Durable Layout

A target project may use this portable durable state layout. Names can be adapted, but responsibilities should remain distinct.

```text
.agentic/
├── tasks/
│   ├── <task-id>.draft.md
│   └── <task-id>.frozen.md
├── authorizations/
│   └── <task-id>.apply.md
├── evidence/
│   └── <task-id>.evidence.yaml
├── judgments/
│   └── <decision-id>.yaml
├── checkpoints/
│   └── CURRENT.md
└── README.md
```

Rules:

- Do not store chain-of-thought or raw private deliberation.
- Keep exact task/contract identity durable.
- Evidence files hold observable receipts, not confident summaries only.
- Judgment files identify review mode: `DIRECT_ACCESS` or `EVIDENCE_ONLY`.
- `CURRENT.md` is a recovery pointer, not a second task board or policy source.
- Projects that already have equivalent durable locations should reuse them instead of creating parallel shadow state.
