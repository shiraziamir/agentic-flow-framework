# Bootstrap prompt — Gemini CLI

```text
Bootstrap Gemini CLI from this framework.

Canonical authority is ARCHITECTURE.md, schemas/, skills/.

Inspect existing GEMINI.md hierarchy, imports, settings and custom commands. Create/update a concise GEMINI.md adapter that points to canonical authority and project-specific commands. Use imports/lazy references carefully so permanent context does not become a copy of the entire framework.

Where Gemini-specific agent/subagent functionality is unavailable or materially different, preserve role separation through separate sessions and the evidence packet schema rather than inventing unsupported behavior.

Compression/checkpointing is capacity management, not durable task state.
Validate that a fresh session can locate the source of truth and task workflow.
```
