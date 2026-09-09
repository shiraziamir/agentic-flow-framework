# Agent Adoption Checklist

**Agent-facing**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

Use this checklist only during framework adoption/bootstrap.

- [ ] Read `ARCHITECTURE.md` and `VERSION`.
- [ ] Determine adoption mode: new/idle vs midstream.
- [ ] If midstream, capture branch/HEAD/dirty paths/current task/tests/environment mutations before product changes.
- [ ] Inspect existing `AGENTS.md` / `CLAUDE.md` / `GEMINI.md` / OpenCode configuration.
- [ ] Discover build, lint, test, dependency/affected-project and deploy mechanics.
- [ ] Locate or propose `.agentic/PROJECT_PROFILE.yaml` from real project evidence.
- [ ] Map existing CI/CD, observability, backup/recovery, security and task stores before creating new ones.
- [ ] Generate only the minimum vendor adapter.
- [ ] Ensure operator docs/research are not in permanent agent context.
- [ ] Validate the verification and production routers are discoverable.
- [ ] Record real gaps as gaps; do not fabricate PASS.
- [ ] Return `ADOPTION_RECEIPT_SCHEMA.md`-conformant output.
- [ ] STOP before product work unless the next authorization permits it.
