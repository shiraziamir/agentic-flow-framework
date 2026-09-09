---
name: project-storytelling
description: Turn evidence-bounded project history into architecture narratives, case studies, lessons and self-branding material when explicitly requested; consume a project-retrospective first when audit-grade reconstruction exists or is required.
---
# Project Storytelling and Self-Branding

**Class:** COMMON but ON-DEMAND ONLY  
**Version:** 1.1  
**Updated:** 2026-09-09T08:22:00Z

## USE WHEN
The user explicitly asks for project history narrative, architecture story, case study, portfolio/self-branding material, release story, lessons learned, or an engineering narrative.

## DO NOT USE WHEN
Normal implementation/review work. Never preload project history merely because it exists. Do not use this skill as the primary audit/counting mechanism when exact retrospective metrics are requested.

## RELATION TO `project-retrospective`

- `project-retrospective` owns audit-grade work reconstruction, timeline/metrics/truth classes and governance-overhead analysis.
- `project-storytelling` owns reader-facing narrative and self-branding.
- When a trustworthy retrospective exists, use it plus its source refs as the bounded evidence base instead of rereading all raw history.
- When exact historical counts are requested but no retrospective exists, run/prepare `project-retrospective` first.

## SOURCE ORDER
1. current architecture/project index;
2. latest applicable retrospective/index if present;
3. completed task summaries;
4. supervisor decision index and selected judgment artifacts;
5. evidence summaries and release/change receipts;
6. usage/cost aggregates when relevant;
7. raw task/evidence artifacts only for claims that require deeper verification.

Do **not** begin by loading every historical task, transcript, or judgment.

## RULES
- Separate verified/proven fact, reconstructed/inferred fact, and unknown.
- Prefer concrete before/after evidence and dates.
- Preserve failed approaches and constraints when they materially explain the engineering achievement.
- Do not exaggerate causality, reliability, scale, savings, or model effectiveness.
- Usage/token/cost numbers must identify source and coverage; missing telemetry is not zero usage.
- Self-branding may emphasize difficulty, leverage, architecture, automation, risk reduction, governance and outcomes, but every factual claim must be traceable.
- Keep generated stories under `stories/` or another cold artifact location; they do not become standing agent context.

## OUTPUT MODES
- `PROJECT_HISTORY`
- `ARCHITECTURE_EVOLUTION`
- `ENGINEERING_CASE_STUDY`
- `PORTFOLIO_SELF_BRANDING`
- `INCIDENT_STORY`
- `RELEASE_NARRATIVE`

Each output includes `version`, `generated_at`, `as_of`, source refs, validity boundary, and any telemetry/reconstruction coverage caveat.
