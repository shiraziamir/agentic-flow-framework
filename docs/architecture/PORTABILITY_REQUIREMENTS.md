# Portability Requirements

A portable Agentic Flow bundle should satisfy these properties:

1. **Self-describing** — `VERSION`, `ARCHITECTURE.md`, and `docs/agent/START_HERE.md` identify authority and adoption flow.
2. **Vendor-neutral** — vendor adapters are generated after inspecting the target harness; the bundle does not assume Claude/Codex/OpenCode/Gemini semantics are identical.
3. **Midstream-safe** — active coding state is snapshotted and reconciled, not reset or retroactively reclassified.
4. **Context-bounded** — operator/reference/history material is excluded from normal agent runtime context.
5. **Integrity-checkable** — bundle manifest records SHA-256 hashes for included files.
6. **Project-adaptive** — existing CI/CD, task stores, observability, security and architecture are reused when they already satisfy required semantics.
7. **Gap-honest** — missing capabilities become explicit gaps rather than generated placeholder PASS values.
8. **Regenerable** — the ZIP is built deterministically from the canonical repository using `scripts/build_agent_bundle.py`.
