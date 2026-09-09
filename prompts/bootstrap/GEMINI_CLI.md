# Bootstrap prompt — Gemini CLI

**Version:** 1.1  
**Updated:** 2026-09-09

```text
Bootstrap Gemini CLI from this framework.

First apply every rule in prompts/bootstrap/GENERIC.md. The following are Gemini-specific additions only.

Canonical authority: ARCHITECTURE.md, schemas/, skills/. Generated GEMINI.md/settings/context files remain adapters and must identify the canonical architecture version.

Use Gemini context-file hierarchy/imports as a concise map, not as a place to concatenate the full framework/history. Preserve hot-state/cold-history separation and only expose skills/procedures needed by current triggers.

Where current Gemini CLI supports checkpointing/compaction/session statistics, treat them as adapter capabilities rather than replacements for durable task state. If `/stats` exposes token/session usage, it may feed the portable usage ledger; unavailable counters remain unknown.

Do not assume compression means evidence/history is safely durable. Do not encode a model name as authority.

Validate fresh-session discovery, adaptive governance, TOKEN_WASTE_WARNING behavior for long work, and report unsupported features.
```
