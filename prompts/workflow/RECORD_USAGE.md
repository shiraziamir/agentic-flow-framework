# Workflow prompt — RECORD USAGE

**Version:** 1.0  
**Updated:** 2026-09-09

```text
Record privacy-safe agent usage for the current task/phase.

Read:
- schemas/USAGE_EVENT.md
- skills/token-efficiency/SKILL.md
- current task budget/routing fields

Use only counters observable from the current provider/harness/CLI/API. Do not infer missing token counts, costs, model identity, or cache behavior.

Record:
- task/phase/agent role;
- provider/model/source when observable;
- input/cache-read/cache-create/output/context tokens when exposed;
- estimated cost only when provider/harness billing data supports it;
- tool-call/child-agent counts when observable;
- waste flags only when backed by an observable pattern;
- concise evidence refs.

Never store prompts, responses, chain-of-thought, transcripts, or private scratchpads.

If a material waste pattern or soft/hard budget breach exists, emit TOKEN_WASTE_WARNING according to token-efficiency before continuing.

Write/append the usage event to the project's configured usage ledger and return only a compact receipt.
```
