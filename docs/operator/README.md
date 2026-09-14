# Operator Documentation Index

**Operator-only index; coding agents should not preload this directory.**

Start here:

- `OPERATOR_GUIDE.en.md` — **single operator control-plane runbook**: Vibe/Product modes, Project Architect, Designer, Manager, Executor, Cold Reviewer, Independent Judge, task hierarchy, Swamp Guard, authority separation, evidence rules, production control and operator checkpoints.
- `OPERATOR_GUIDE.fa.md` — **Runbook کامل فارسی اپراتور** با همان مدل کنترل و Guardrailها.

Role/setup details:

- `DESIGNER_MANAGER_SETUP.md` — direct-Git role setup, permissions and review separation.
- `CONTEXT_PACKET.md` — bounded degraded-access alternative when a role cannot inspect Git directly.
- `PROMPT_TASK_AGENT_SETUP.en.md` / `.fa.md` — prompting, task-writing and agent-setup guidance.

Adoption / operation:

- `CLONE_AND_ADOPT.md` — clone-based adoption and `STRICT_PREVIEW` approval pattern.
- `INSTALLATION_PROMPTS.en.md` / `.fa.md` — copy-ready installation/adoption prompts.
- `USING_PYTHON_TOOLS.en.md` / `.fa.md` — deterministic helper usage.
- `CLAUDE_USAGE_NOTIFICATIONS.md` — Claude Code usage/quota telemetry integration.
- `RELEASE_CHECKLIST.en.md` / `.fa.md` — framework release checklist.
- `SCOPE_BOUNDARY.md` — operator/agent documentation-boundary note.

## Operator mental model

```text
Operator / Product Owner
→ Project Architect for greenfield/uncertain architecture
→ Designer for bounded task contract
→ Manager for freeze + authority + review
→ Executor for bounded implementation
→ Cold/Adversarial Review
→ Manager consolidated findings + bounded remediation
→ Independent Judge for HIGH-risk closure when required
→ Operator for production/business authority
```

Critical guardrails are summarized in the Operator Guide:

```text
VIBE_PROTOTYPE != PRODUCTION BASELINE
RECENCY IS NOT PRIORITY
SIDE_TASK cannot self-promote
SWAMP GUARD = CLEAR | WATCH | ALERT | STOP_REBASELINE
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
Human transports authority and priority
Repository transports engineering state
NO ROLLBACK / RECOVERY PLAN = no production mutation
```

Canonical policy remains `ARCHITECTURE.md` plus `schemas/`. Operator docs explain how to run that policy and should not be copied wholesale into permanent Executor context.

The Git repository is the recommended distribution source. Portable bundles may contain this directory for offline use, but coding agents should enter through `START_HERE.md` and load operator files only when needed.