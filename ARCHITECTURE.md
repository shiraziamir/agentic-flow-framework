# Agentic Flow Architecture

**Status:** CANONICAL SOURCE OF TRUTH  
**Version:** 1.9  
**Updated:** 2026-09-13

Agentic Flow is a repository-first, vendor-neutral operating architecture for coding agents. This file is intentionally a **small canonical map + invariant set**. Detailed contracts live in lower layers and are loaded only when the active task triggers them.

## 1. Source-of-truth hierarchy

When sources disagree, use this order:

1. `ARCHITECTURE.md` — authority, lifecycle and invariants.
2. `schemas/` — durable task/evidence/project/approval contracts.
3. `verification/` — claim-aware verification profiles.
4. `production/` — environment/production-readiness profiles.
5. `skills/` — triggered reusable procedures.
6. approved current project/task/amendment/profile state.
7. receipts, gaps, overrides and reviewer decisions.
8. generated vendor adapters.
9. conversation memory.

Reader docs, research, historical reports and generated exports are explanatory/cold layers, not higher authority.

## 2. Core invariants

> Durable project memory; disposable working context.

> Human transports authority; repository transports engineering state.

> A claim may be no broader than the current receipt that directly establishes it.

> Mock-only evidence cannot silently inherit integration, deployment or production semantics.

> Multi-model agreement is review coverage, not independent behavioral evidence.

> Quality requirements stay fixed; process ceremony adapts to risk.

> An Executor that can edit a behavior but cannot exercise the real changed path is not execution-ready for that claim.

> Remediation autonomy is not scope autonomy.

> Unknown/unowned dirty work is protected state.

> Task authority, mutation authority, environment authority and external-side-effect authority are separate.

> Production readiness is evidenced capability plus explicit gaps—not a badge.

> Every production mutation requires rollback or explicit forward-recovery readiness before execution.

Agent/model/provider sessions are replaceable. Project state must survive reset or handoff without replaying full chat history.

## 3. Progressive disclosure

Humans should not read the whole repository to begin. The normal human route is:

```text
README.md
→ docs/GETTING_STARTED.md
→ docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md
→ docs/GUIDE.fa.md when Persian guidance is preferred
```

The normal Executor route is:

```text
docs/agent/START_HERE.md
→ current project profile + current task
→ only triggered schemas/profiles/skills
```

Do not preload research, operator manuals, historical tasks, all production profiles or the full schema shelf.

## 4. Adoption modes

- **NEW / IDLE:** discover project reality, establish/map the project profile, validate build/test/environment entrypoints, then stop before product mutation unless authorized.
- **EXISTING MATURE:** reuse valid CI/CD, observability, security and architecture; do not create shadow systems.
- **MIDSTREAM:** snapshot branch/HEAD/dirty state/current task/tests/environment first; preserve existing work; never fabricate retroactive approval.

The framework can be cloned directly or distributed as a generated portable bundle. Distribution does not change authority semantics.

## 5. Project baseline

A target project should normally maintain:

```text
.agentic/PROJECT_PROFILE.yaml
```

Use `schemas/PROJECT_PROFILE_CONFIG.md` and `templates/PROJECT_PROFILE.example.yaml`.

The profile defines intended testing, execution readiness, mutation modes, environment permissions, review policy, role access, model routing, workspace safety, external effects and production expectations. It is not proof that those expectations are satisfied.

Temporary exceptions use `schemas/TEMPORARY_OVERRIDE.md`; they are explicit, owned, expiring and do not silently rewrite the baseline.

## 6. Risk and work kind are separate

New task contracts should represent two dimensions:

```text
risk.level = LOW | MEDIUM | HIGH
work_kind  = IMPLEMENTATION | REMEDIATION | EVIDENCE_ONLY
```

Legacy `governance: HIGH|MEDIUM|EVIDENCE_ONLY` remains readable during migration, but `EVIDENCE_ONLY` is a work kind, not a risk level.

Default workflow:

```text
LOW
execute → focused test → compact self-review → report

MEDIUM
short preflight → execute → cold review → one bounded remediation → Manager review

HIGH
frozen contract
→ failure-surface preflight
→ separate initial apply authority
→ bounded execution
→ adversarial review
→ Manager consolidated review
→ one controlled remediation round by default
→ read-only Independent Judge when required
→ Operator production/business decision
```

HIGH risk means stronger boundaries/evidence, not human approval for every tiny correction.

A second remediation iteration is exceptional rather than routine: it requires a new material finding, must remain inside the configured maximum and cannot silently expand scope.

## 7. Independent closure

A different model name is not enough to establish independence. Independent review should separate as many of these dimensions as the risk requires:

```text
IMPLEMENTATION INDEPENDENCE
reviewer/judge did not materially implement the change

CONTEXT INDEPENDENCE
review starts from task + source/diff + receipts, not only the Executor narrative

AUTHORITY INDEPENDENCE
Executor cannot approve/merge/close its own material work

EVIDENCE INDEPENDENCE
reviewer/judge inspects raw receipts/runtime evidence rather than repeating another model's conclusion
```

Model/provider diversity is useful defense-in-depth, especially for HIGH-risk judgment, but it is **not** an evidence-class upgrade by itself.

```text
Sonnet PASS + Opus PASS + another model PASS
!=
real integration / deployment / production proof
```

The Independent Judge is read-only by default. It may inspect source, exact diff, CI/receipts and authorized production telemetry, but it must not mutate product code, rewrite the task to manufacture a pass, or mutate production. Production mutation remains separately authorized by the Operator/project policy.

## 8. Artifact-driven handoff and session reset

Humans should not act as permanent message buses between agents.

Durable handoff state should be recoverable from repository artifacts such as:

```text
current task / contract
repository + base/head identity
review findings
active remediation window
receipts / gaps
closure state
next required authority decision
```

A fresh agent session should be able to inspect those artifacts and continue without replaying the previous conversation.

```text
checkpoint durable state
→ session may be cleared/replaced
→ new session re-reads current repo/task state
```

Session-reset commands are vendor-specific and belong in adapters/guides, not in canonical policy.

## 9. Capability/cost routing

The framework does not prescribe model brands. Projects may route roles by capability and cost, for example:

```text
Executor          → task-adequate, cost-efficient model/harness
Manager           → stronger reasoning/review capability when justified
Independent Judge → high-reasoning, separate context; model diversity preferred where useful
```

Cost routing must never lower the evidence or acceptance bar. If the cheaper role cannot establish the required claim, escalate capability or leave the claim unverified.

## 10. Production mutation invariant

Production mutation is a separate authority boundary. Enabling production mode does not mean the Executor may improvise recovery after something goes wrong.

Before **every production change**, the active task/change record must identify:

```text
target environment
exact artifact/config/change identity
expected success + health signals
abort condition
rollback OR explicit forward-recovery path
stateful/data rollback constraints
recovery authority/owner
post-change verification
```

If rollback is technically possible, it must be documented and executable before mutation. If rollback is unsafe or impossible, the change must instead define an explicit forward-recovery path, backup/checkpoint strategy, blast-radius controls and STOP conditions.

```text
missing rollback/recovery readiness
→ NOT EXECUTION_READY_FOR_PRODUCTION_MUTATION
```

A successful deployment command does not erase the recovery requirement. See `production/DELIVERY.md`.

## 11. Canonical practical routes

- Task lifecycle: `docs/agent/TASK_WORKFLOW_DRAFT_REVIEW_APPLY_VERIFY.md`
- Mutation/remediation authority: `schemas/MUTATION_APPROVAL_POLICY.md`
- Project operating baseline: `schemas/PROJECT_PROFILE_CONFIG.md`
- Role setup and permissions: `docs/operator/DESIGNER_MANAGER_SETUP.md`
- Independent Judge prompt: `prompts/operator/INDEPENDENT_JUDGE.md`
- Test environments: `production/AGENT_ENVIRONMENTS.md`
- Delivery/rollback: `production/DELIVERY.md`
- Verification semantics: `verification/00_INDEX.md`
- Production profiles: `production/00_INDEX.md`

Detailed rules belong in those triggered layers rather than being duplicated here.
