# Bootstrap prompt — Gemini CLI

**Version:** 1.2  
**Updated:** 2026-09-09T10:04:00Z

```text
Bootstrap Gemini CLI from this framework.

Canonical authority is ARCHITECTURE.md + schemas/ + verification/ + skills/. GEMINI.md and generated Gemini-facing files are adapters only.

Inspect the target project's existing GEMINI.md/context files plus actual frontend/backend/shared/data/infra/CI layout, build/test commands and task stores. Generate a concise adapter that:
- points to canonical authority/version;
- exposes change classification and verification profiles lazily;
- exposes DRAFT_TASK -> REVIEW_DRAFT -> freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> supervisor workflow;
- records claim -> minimum receipt requirements before APPLY;
- keeps reports bounded to actual ref/artifact/environment and checks executed/not executed;
- uses current Gemini capabilities for delegation/usage reporting only when actually available;
- keeps cold history and unused profiles out of normal context.

If structured JSON/YAML task/evidence/status artifacts are used, make scripts/verification_lint.py discoverable.

Do not make generated context files a second policy source. Document any unsupported feature instead of pretending it exists.
```
