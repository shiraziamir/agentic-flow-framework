# Bootstrap prompt — generic coding agent

**Version:** 1.1  
**Updated:** 2026-09-09

Use this after cloning Agentic Flow Framework into a project or making it available as a reference.

```text
You are bootstrapping this repository's agent operating layer.

1. Read, in order:
   - ARCHITECTURE.md
   - schemas/TASK_CONTRACT.md
   - schemas/AMENDMENT.md
   - schemas/EVIDENCE_PACKET.md
   - schemas/PROJECT_LAYOUT.md
   - skills/00_INDEX.md
2. Record the canonical architecture version you are generating from.
3. Inspect the target project's existing agent instructions, task/history stores, build/test mechanics, provider/harness telemetry, and model/subagent capabilities. Do not overwrite working project-specific rules blindly and do not create shadow stores when equivalents already exist.
4. Generate/update the minimum vendor-specific adapter files needed by this harness.
5. Adapters are NON-AUTHORITATIVE. They must point to canonical files and must not invent conflicting policy.
6. Keep always-on instructions concise. Do not copy ARCHITECTURE.md, completed-task history, judgment history, usage ledger, or every skill body into permanent context. Expose skills/tools/history lazily where supported.
7. Preserve risk-adaptive governance: HIGH / MEDIUM / EVIDENCE_ONLY.
8. Configure semantic roles using capabilities actually available: ORCHESTRATOR / CHEAP_READONLY / EXECUTION_TIER / JUDGMENT_TIER / INDEPENDENT_REVIEWER.
9. Where observable, wire provider/harness usage counters to the portable usage ledger; where unavailable, document telemetry as UNKNOWN rather than inventing it.
10. Enable/operator-document TOKEN_WASTE_WARNING behavior for long/cost-sensitive work. Cheap workers must remain read-only by default and cannot weaken acceptance quality.
11. Preserve hot-state/cold-history separation: ordinary runs discover current task/checkpoint/index without recursively reading completed tasks/judgments/stories.
12. If the harness lacks a feature, document the limitation and preserve the conceptual lifecycle with files/prompts instead of pretending the feature exists.
13. Before writing, report the adapter plan and conflicts with existing files.
14. After writing, verify that a fresh session can discover:
   - source of truth and canonical version;
   - governance classification/amendment path;
   - skill index;
   - supervisor workflow;
   - token-efficiency/usage path when applicable;
   - current project state without loading cold history;
   - build/test commands;
   without loading the entire framework into permanent context.
15. Return changed paths and a concise validation receipt. Do not start product work.
```
