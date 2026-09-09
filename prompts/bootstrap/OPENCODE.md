# Bootstrap prompt — OpenCode

**Version:** 1.1  
**Updated:** 2026-09-09

```text
Bootstrap OpenCode from this framework.

First apply every rule in prompts/bootstrap/GENERIC.md. The following are OpenCode-specific additions only.

Canonical authority: ARCHITECTURE.md, schemas/, skills/. Generated OpenCode files remain adapters and must identify the canonical architecture version.

Use AGENTS.md as a concise map. Reuse canonical SKILL.md directories through the OpenCode-compatible discovery paths where practical instead of duplicating skill prose. Configure per-agent model and permissions only from capabilities actually available in this environment.

Prefer a cheap read-only subagent for bounded discovery/log reduction when quality is mechanically checkable; use standard execution and stronger judgment roles only where justified. Keep completed task/judgment/usage/story history cold.

If session/model/token telemetry is not exposed by the current OpenCode/provider setup, record it as unavailable/unknown rather than fabricating counters.

Validate fresh-session discovery, adaptive governance, lazy skill use, TOKEN_WASTE_WARNING behavior for long work, and report unsupported features.
```
