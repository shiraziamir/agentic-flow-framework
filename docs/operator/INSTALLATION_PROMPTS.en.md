# Practical Installation Prompts

**Operator-facing; do not preload into normal agent context.**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

## Fresh project or idle repository

```text
Agentic Flow has been extracted to `.agentic-flow/`.
Read `.agentic-flow/docs/agent/START_HERE.md` and adopt the framework for this repository.
Do not start product work yet.
Inspect existing project instructions, build/test/deploy structure, and project profile requirements first.
Generate only the minimum vendor adapter and return an adoption receipt.
```

## Mid-task adoption

```text
Agentic Flow has been introduced while coding is already in progress.
Read `.agentic-flow/docs/agent/MIDSTREAM_ADOPTION.md`.
Do not discard, reset, amend, or continue current product changes until you have captured the adoption snapshot.
Do not retroactively claim framework review or authorization for existing work.
Reconcile the remaining work, profile/gaps, and verification requirements; return the next authorization required.
```

## Existing mature project

```text
Adopt Agentic Flow as an operating/control layer, not as a replacement technology stack.
Preserve working CI/CD, observability, security, task tracking and architecture mechanisms when they already satisfy the framework semantics.
Map them to the framework instead of creating shadow systems.
List conflicts and real gaps separately from already-satisfied requirements.
```

## Production-bound project

```text
After adoption, assess the existing production profile using the smallest applicable profile set.
Do not say `production ready` unless the named tier/environment requirements have current receipts.
Create explicit operational gaps for missing or unverified backup/restore, observability, security, delivery, troubleshooting or resilience requirements.
Do not implement every gap automatically; prioritize and request authorization according to risk.
```
