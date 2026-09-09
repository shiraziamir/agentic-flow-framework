# Why and How to Use Agentic Flow Framework

**Architecture reader**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z  
**Canonical authority:** `ARCHITECTURE.md`

## Why this system exists

Coding agents can produce useful code quickly, but the difficult failures are rarely syntax errors. They are false-complete states, scope drift, stale context, weak tests, unverified deployment claims, hidden operational gaps, expensive models doing mechanical work, and long conversations becoming the only project memory.

Agentic Flow makes these failure modes explicit by separating:

```text
WHAT SHOULD BE TRUE      project/task/profile requirements
WHAT WAS DONE            implementation/diff/artifact
WHAT WAS OBSERVED        receipts
WHAT IS STILL UNKNOWN    gaps/unverified claims
WHO DECIDES              owner/supervisor authority
WHAT FUTURE AGENTS READ  hot state vs cold history
```

The system is repository-first because a chat session, model, provider, or human reviewer can change. Durable engineering state should survive all of them.

## Core architecture

```text
PROJECT BASELINE
  PROJECT_PROFILE.yaml
        ↓
REQUEST
        ↓
DRAFT TASK + CHANGE CLASSIFICATION
        ↓
DRAFT REVIEW
        ↓
AUTHORIZED APPLY
        ↓
IMPLEMENTATION
        ↓
CLAIM-AWARE VERIFICATION
        ↓
REALITY REPORT / EVIDENCE
        ↓
INDEPENDENT JUDGMENT WHEN REQUIRED
        ↓
CHECKPOINT / COLD HISTORY
```

In parallel, production-bound projects maintain a production profile and explicit operational gaps across delivery, security, observability, data durability, troubleshooting, resilience and architecture.

## Why claim → receipt matters

A plan is not implementation. A unit test is not a browser flow. HTTP 200 is not persistence. A successful backup job is not recoverability. A reviewer saying “looks good” is not runtime evidence.

The framework therefore restricts report language to what current, identified receipts establish. Unsupported statements remain `INFERRED`, `UNKNOWN`, `PARTIAL`, or `UNVERIFIED`.

## Why project profile and temporary override are separate

The project profile defines the intended steady-state engineering bar. Temporary operational exceptions must not silently rewrite that baseline. A temporary override records reason, owner, expiry, added risk, compensating controls and restoration verification. Expired exceptions become visible gaps.

## Why tests are designed before implementation but strict TDD is not universal

Material tasks define observable DoD, planned closure claims and required tests before APPLY. This prevents implementation from redefining success after the fact. Strict test-first coding is recommended where behavior is precise and important, but exploratory/spike/generated work may need a different sequence. Load-bearing tests should be proven capable of detecting the defect through mutation/path proof when risk warrants it.

## Why agents need environments

Many claims cannot be proven from static code. The environment ladder is:

```text
LOCAL/HERMETIC
→ EPHEMERAL TEST
→ SHARED TEST
→ STAGING/PRODUCTION-LIKE
→ CONTROLLED CANARY/PRODUCTION READ
→ PRODUCTION MUTATION
```

Use the lowest environment capable of establishing the claim. Production authority is never created by the agent itself.

## Why patterns are proposals, not commandments

Adapters, Anti-Corruption Layers, repositories, strategies, circuit breakers, sagas and similar patterns solve particular volatility/failure/changeability problems and add complexity. Small/local/reversible pattern use can be an implementation decision. Cross-module/public/architectural pattern adoption should be proposed with the problem, simpler alternative, benefits, costs and verification impact and reviewed according to risk.

## Why context is split

Agent context is working memory, not archive storage. Ordinary sessions need the current task/profile, relevant source, selected profiles and triggered skills. Operator guides, research, completed tasks, historical judgments, retrospectives and stories remain cold until explicitly needed.

## Adoption modes

### New project

Place/extract the Agent Bundle into the project, open `docs/agent/START_HERE.md`, generate the minimal vendor adapter, create the project profile, and validate build/test/environment discovery before product work.

### Existing project

Bootstrap from existing architecture/build/test/deploy reality. Do not replace established mechanisms merely because the framework has examples.

### Mid-task adoption

Use `docs/agent/MIDSTREAM_ADOPTION.md`. Snapshot the current branch/dirty state/work/tests, distinguish pre-adoption work from remaining work, then reconcile without fabricating earlier authorization or discarding valid edits.

## What this framework is not

It is not a mandatory technology stack, not a requirement to run Kubernetes/Prometheus/Chaos Monkey, not strict TDD for every edit, not a replacement for operator authorization, not a security certification, and not permission to create enterprise-scale abstractions in small projects.

The operating principle is: **use the smallest process, model, test surface and architecture that preserves the required quality and risk bar, while making every important gap visible.**
