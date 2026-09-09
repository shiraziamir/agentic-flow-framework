---
name: project-storytelling
description: Reconstruct the truthful story, architecture evolution, decisions, engineering advantages, incidents, and measurable outcomes of a project from cold durable artifacts only when explicitly requested.
---
# Project Storytelling and Self-Branding

**Class:** COMMON but ON-DEMAND ONLY  
**Updated:** 2026-09-09

## USE WHEN
The user explicitly asks for project history, architecture narrative, case study, portfolio/self-branding material, release story, lessons learned, or an engineering retrospective.

## DO NOT USE WHEN
Normal implementation/review work. Never preload project history merely because it exists.

## SOURCE ORDER
1. current architecture/project index;
2. completed task summaries;
3. supervisor decision index and selected judgment artifacts;
4. evidence summaries and release/change receipts;
5. usage/cost aggregates when relevant;
6. raw task/evidence artifacts only for claims that require deeper verification.

Do **not** begin by loading every historical task, transcript, or judgment.

## RULES
- Separate verified fact, inference, and unknown.
- Prefer concrete before/after evidence and dates.
- Preserve failed approaches and constraints when they materially explain the engineering achievement.
- Do not exaggerate causality, reliability, scale, savings, or model effectiveness.
- Usage/token/cost numbers must identify source and coverage; missing telemetry is not zero usage.
- Self-branding may emphasize difficulty, leverage, architecture, automation, risk reduction, and outcomes, but every factual claim must be traceable.
- Keep generated stories under `stories/` or another cold artifact location; they do not become standing agent context.

## OUTPUT MODES
- `PROJECT_HISTORY`
- `ARCHITECTURE_EVOLUTION`
- `ENGINEERING_CASE_STUDY`
- `PORTFOLIO_SELF_BRANDING`
- `INCIDENT_STORY`
- `RELEASE_NARRATIVE`

Each output includes `as_of`, source refs, validity boundary, and any telemetry coverage caveat.
