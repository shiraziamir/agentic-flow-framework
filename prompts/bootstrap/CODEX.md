# Bootstrap prompt — Codex

**Version:** 1.1  
**Updated:** 2026-09-09

```text
Bootstrap Codex from this framework.

First apply every rule in prompts/bootstrap/GENERIC.md. The following are Codex-specific additions only.

Canonical authority: ARCHITECTURE.md, schemas/, skills/. Generated Codex/AGENTS.md surfaces remain adapters and must identify the canonical architecture version.

Create/update the smallest useful hierarchical AGENTS.md map for this target repository. Keep it short and point to canonical project docs, task state and on-demand skills instead of copying history/manuals.

Where the current Codex/Agents harness supports skills, sandboxed tools, memory/thread persistence or other orchestration primitives, use them only as adapters to the portable roles and lifecycle. Do not assume product-specific model menus or token counters that are not observable in the current environment.

Keep completed plans/judgments/usage/story artifacts cold. Ordinary runs read current state/indexes only. Use cheaper/bounded workers only when the current harness exposes them and acceptance quality can be preserved.

Validate fresh-session discovery, adaptive governance, TOKEN_WASTE_WARNING behavior for long work, and report any provider-specific limitations.
```
