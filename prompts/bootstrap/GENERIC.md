# Bootstrap prompt — generic coding agent

**Version:** 1.3  
**Updated:** 2026-09-09T10:40:00Z

Use this after cloning Agentic Flow Framework into a project or making it available as a reference.

```text
You are bootstrapping this repository's agent operating layer.

1. Read, in order:
   - ARCHITECTURE.md
   - schemas/TASK_CONTRACT.md
   - schemas/CHANGE_CLASSIFICATION.md
   - schemas/CLAIM_RECEIPT.md
   - schemas/PRODUCTION_PROFILE.md
   - schemas/OPERATIONAL_GAP.md
   - schemas/EVIDENCE_PACKET.md
   - schemas/STATUS_REPORT.md
   - schemas/PROJECT_LAYOUT.md
   - verification/00_INDEX.md
   - production/00_INDEX.md
   - skills/00_INDEX.md
2. Record the canonical architecture version you are generating from.
3. Inspect existing agent instructions, source/dependency graph, frontend/backend/shared/data/infra/CI boundaries, build/test/deploy mechanics, runtime environments, data stores, observability, security tooling, task/history stores and model/subagent capabilities. Do not create parallel shadow systems when working equivalents exist.
4. Derive a project-local surface map and mechanically discoverable affected-consumer/build/test commands without assuming a language/framework.
5. If this repository is or will be production-bound, create/update a compact project production profile conforming to schemas/PRODUCTION_PROFILE.md. Separate codebase_scale from readiness_tier; risk overrides repository size.
6. Discover production capabilities before proposing tools:
   - source -> build -> immutable artifact -> deploy -> running artifact identity -> rollback/forward recovery;
   - metrics/logs/traces/health/SLO/alerts appropriate to tier;
   - durable data inventory, RPO/RTO, backup and restore evidence;
   - security/authz/secrets/dependencies/supply-chain/runtime controls;
   - troubleshooting/runbooks/release correlation;
   - resilience/failure assumptions;
   - external/provider boundaries and code changeability.
7. Any material missing/partial/unverified production requirement becomes an explicit operational gap. Never generate an optimistic production-ready badge from config presence.
8. If logs are supplied to AI/agents, wire the AI_LOG_ANALYSIS profile: structured correlation, redaction/minimization, raw-query provenance, untrusted-data delimiters and read-only/least-privilege discovery.
9. Generate/update the minimum vendor-specific adapter files needed by this harness. Adapters are NON-AUTHORITATIVE and point to canonical files/current project profile.
10. Keep always-on instructions concise. Do not copy ARCHITECTURE.md, all verification/production profiles, completed history, gaps, judgments or the whole Skill shelf into permanent context. Expose them lazily.
11. Preserve HIGH / MEDIUM / EVIDENCE_ONLY governance and DRAFT_TASK -> REVIEW_DRAFT -> freeze/authorization -> APPLY_TASK -> VERIFY_AND_REPORT -> required closure.
12. Material tasks classify engineering + operational flags, production impact and planned claim -> minimum receipt before APPLY.
13. Configure semantic roles from capabilities actually available: ORCHESTRATOR / CHEAP_READONLY / EXECUTION_TIER / JUDGMENT_TIER / INDEPENDENT_REVIEWER.
14. Reviewers remain read-only during review; evidence-only review cannot upgrade missing receipts.
15. Wire observable token/cost telemetry when available; unknown remains UNKNOWN. Enable TOKEN_WASTE_WARNING for material waste.
16. Expose deterministic repository validators such as verification/readiness linting when compatible.
17. Preserve hot-state/cold-history separation. Normal work may read current production profile + open-gap index when relevant, not every historical gap/incident/runbook.
18. If the harness lacks a feature, document the limitation/gap instead of pretending it exists.
19. Before writing, report adapter/bootstrap plan and conflicts.
20. After writing, verify a fresh session can discover without loading the whole framework:
   - source of truth/version;
   - surface/operational classification;
   - verification router + claim-receipt rules;
   - current production profile/tier + open gaps;
   - build/test/deploy/rollback commands or explicit gaps;
   - observability/data recovery/security/troubleshooting entrypoints;
   - workflow/supervisor/token-efficiency paths.
21. Return changed paths, created gaps and concise validation receipts. Do not start unrelated product work.
```