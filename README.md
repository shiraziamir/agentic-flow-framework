# Agentic Flow Framework

A repository-first, tool-agnostic operating framework for engineering with coding agents.

**This GitHub repository is the authoritative home for the framework.** The earlier Google Drive folder is an archived snapshot only. All updates after 2026-09-09 belong here.

Current framework revision: **v1.1.1**.

## Start here

- [`agentic-flow-framework.en.md`](agentic-flow-framework.en.md) — canonical English Markdown reference.
- [`agentic-flow-framework.en.html`](agentic-flow-framework.en.html) — standalone English HTML (LTR).
- [`agentic-flow-framework.fa.html`](agentic-flow-framework.fa.html) — standalone Persian HTML (RTL, with LTR code/identifiers).
- [`research/2026-09-09-context-model-routing.md`](research/2026-09-09-context-model-routing.md) — primary-source research behind the context/model-routing guidance.
- [`templates/MODEL_TIER_MAP.example.yaml`](templates/MODEL_TIER_MAP.example.yaml) — vendor-neutral routing template.
- [`templates/MODULE_CONTEXT_CONTRACT.example.yaml`](templates/MODULE_CONTEXT_CONTRACT.example.yaml) — bounded context contract for modular repositories.

## Core idea

> Durable project memory; disposable, high-quality working context.

Keep always-on policy small, make tasks explicit, load reusable procedures on demand, route low-risk work to cheaper tiers, escalate on evidence, verify with receipts, and reset context at durable semantic boundaries.

## Source policy

Recommendations in this project should prefer primary/current sources: official agent/model documentation, vendor engineering reports describing real production workflows, and primary build-system/compiler documentation. Community heuristics may be noted as hypotheses but should not silently become framework rules.

Version-specific product behavior (default models, CLI behavior, context sizes, pricing) is not a permanent framework invariant and must be re-checked against current official vendor documentation when it materially affects a decision.
