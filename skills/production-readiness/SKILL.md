---
name: production-readiness
description: Assess and maintain a project's DevOps, security, observability, data recovery and operational readiness at a risk-appropriate maturity tier, reporting every material gap explicitly.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# Production Readiness

## USE WHEN

- a project/service is intended for production;
- user asks whether a project is DevOps-friendly, secure, observable or operable;
- architecture/release changes affect deployment, monitoring, recovery or security posture;
- a new repository is bootstrapped for ongoing engineering;
- production readiness/launch review is requested.

## DO NOT USE WHEN

A tiny docs/evidence-only change cannot affect project operational posture.

## PROCEDURE

1. Read `schemas/PRODUCTION_PROFILE.md` and existing project profile/gaps.
2. Determine `codebase_scale` separately from `readiness_tier`; risk overrides size.
3. Load `production/00_INDEX.md` and only triggered profiles.
4. Discover existing CI/CD, runtime, observability, data stores, security tooling and operational docs mechanically before proposing new systems.
5. For each required capability classify `VERIFIED`, `PARTIAL`, `UNVERIFIED`, `NOT_IMPLEMENTED` or `NOT_APPLICABLE` with receipts.
6. Create/update durable `schemas/OPERATIONAL_GAP.md` artifacts for non-ready requirements.
7. Prefer existing project/platform conventions over parallel shadow tooling.
8. Make the smallest high-value readiness improvement; do not enterprise-architect a low-risk small project.
9. For production-bound changes, map closure to artifact/environment/runtime evidence.
10. Update profile/version/docs when verified capabilities change.

## FAIL CLOSED

- `tool configured` is not `capability proven`;
- `backup enabled` is not `restore proven`;
- `metrics exported` is not `useful monitoring/alerting proven`;
- `CI green` is not `deployed artifact proven`;
- `security scanner green` is not `system secure`;
- missing evidence remains a gap.

## OUTPUT

Updated production profile, gap list, evidence refs, prioritized improvements and exact validity boundary.