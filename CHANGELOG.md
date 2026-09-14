# Changelog

## 1.11 — 2026-09-14

Productization and coherence release. Consolidates recent Task Hierarchy, Operator Control Plane and Dual-Lens work into a simpler operating model rather than adding another governance layer.

Key changes:

- adds `VIBE_FAST | PRODUCT_STANDARD | HIGH_ASSURANCE` operating presets so adopters can start from sane defaults and override only real project differences;
- separates project phase (`VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE`) from assurance/ceremony preset;
- formalizes `PRIMARY_TASK | SIDE_TASK | INTERRUPT` attention control and explicit side-task promotion;
- adds the project-level System Truth / Data Authority Map and a directly usable `templates/SYSTEM_TRUTH_MAP.example.yaml`;
- makes Dual-Lens risk-adaptive: LOW/local work uses a compact system-impact summary, while MEDIUM/HIGH and sensitive boundaries record explicit relevant dimensions;
- makes cross-system audit event/risk-first, with the 5–8 material-task interval retained only as a fallback reminder;
- keeps mutation/path proof for load-bearing tests while explicitly protecting operator workspace from destructive Git restore/reset/clean behavior;
- synchronizes Agent entrypoint, architecture and profile semantics around presets, System Truth, Swamp Guard and production recovery;
- fixes bundle-vs-agent-context wording: operator/reference docs may be present in the portable ZIP but remain cold/default-excluded from coding-agent context;
- adds the Dual-Lens/productization self-test to CI so a green release check actually validates the new wiring;
- keeps the framework itself under Swamp Guard: prefer simplification, validation and real-project measurement over adding new governance concepts.

Production mutation remains separately authorized and requires rollback or explicit forward-recovery readiness before execution. Independent Judge remains read-only by default. Multi-model agreement remains review coverage, not behavioral evidence.

## 1.10 — 2026-09-13

Project-inception and architecture-safety release: adds explicit `VIBE_PROTOTYPE | PRODUCT_BUILD | MAINTENANCE` project modes; a canonical Product Inception / Architecture Discovery lifecycle; a copy-ready Project Architect prompt; quality/eval-contract-first guidance for AI/RAG systems; minimal architecture option comparison; walking-skeleton and architecture-checkpoint gates; hard-to-change-invariant vs easy-experiment-variable separation; and a continuous Swamp Guard with `CLEAR | WATCH | ALERT | STOP_REBASELINE` states. Vibe prototypes are explicitly sacrificial/non-production by default and require re-baselining before product promotion.

## 1.9 — 2026-09-13

Risk-adaptive execution and coherence release: adds controlled remediation windows, consolidated review, triggered failure-surface preflight, pre-Manager adversarial review, compact receipt/raw-evidence separation, workspace dirty-state protection, explicit external-provider-call authority, flow-friction metrics and a clean separation between risk level and work kind. Simplifies the newcomer route to four human-facing files and two agent entrypoints, and refreshes the standalone Persian guide around the same workflow.

Independent-closure hardening: formalizes that multi-model agreement is review coverage rather than behavioral evidence; defines implementation/context/authority/evidence independence; adds a read-only Independent Judge role and prompt; makes one remediation iteration the default with a second allowed only for a new material finding; adds role-specific access defaults, vendor-neutral capability/cost routing and repository-driven handoff/session-reset semantics. Production mutation remains separately owner-authorized with rollback or explicit forward-recovery readiness.

## 1.8 — 2026-09-13

Newcomer/onboarding release: makes README a WHY-first landing page; adds getting-started, comparison, validation-status and end-to-end example guides; adds a standalone comprehensive RTL Persian guide; formalizes Designer/Manager/Executor separation, direct-Git branch/PR review and bounded context packets; adds evidence-constrained advisory tags; and makes real changed-path execution readiness, environment ladders and mock-only claim limits explicit in canonical policy, profiles, prompts and deterministic documentation checks.

## Unreleased

Evidence-recovery hardening: adds a canonical recovery/measurement-qualification schema; separates designed/implemented/tested/qualified/live/deployed/production-proven capability states; formalizes stale/wrong-runtime evidence as preservable but potentially `VOID_FOR_CLAIM`; records single-use authorization consumption and rerun re-authorization; adds pre-live runtime/environment/writable-path qualification and explicit side-effect accounting.

Usage-aware operator reporting: adds optional per-material-task quota snapshots, a normalized quota schema, Claude Code session/weekly usage extraction with status-line telemetry preferred over the implementation-dependent `~/.claude.json` cache, Telegram/notification guidance, and CI/self-tests for the helper. Quota is explicitly an operator/routing signal and never engineering evidence or permission to lower verification quality.

## 1.7 — 2026-09-09

Portable adoption release: separates agent/operator/reference docs; adds drop-in and midstream adoption guides/prompts; adds consolidated primary-source index; adds English/Persian prompting/task/agent-setup guides; adds deterministic Agent Bundle builder with manifest hashing and self-test; formalizes portable bundle/documentation boundaries.

## 1.6 — 2026-09-09

Production engineering profiles, project profile/operational gaps, DevOps/security/observability/data durability/troubleshooting/AI-log/chaos/evolvable architecture and readiness checks.

## 1.5 — 2026-09-09

Claim/receipt contract, truth-aware reporting, engineering-surface verification and blind-spot audit.

## 1.4 — 2026-09-09

Execution retrospective ledger and audit/storytelling separation.

## 1.3 — 2026-09-09

Adaptive governance/token efficiency and project history controls.
