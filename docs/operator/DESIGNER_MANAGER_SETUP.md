# Setting Up Designer, Manager, Executor and Independent Judge

**Operator guide.** This document explains how to separate planning, execution, authority and independent closure without turning the human into a permanent message bus.

## 1. Roles

### Designer / Task Architect

Purpose: turn operator intent + repository evidence into a bounded task contract and evidence-constrained engineering advisory.

Default posture:

- product/source access: read-only;
- production mutation: denied;
- may draft task/advisory artifacts;
- must not implement product changes;
- must not approve/freeze its own task.

### Manager / Reviewer

Purpose: own task quality control, bounded authority and consolidated code review.

Default posture:

- reads exact repository/diff/receipts;
- may freeze/approve task or mutation only when operator/project policy delegates that authority;
- normally does not implement product code;
- production mutation denied by default;
- produces one consolidated finding set where possible;
- may issue a bounded remediation window;
- does not replace an Independent Judge when separate closure is required.

### Executor

Purpose: implement the frozen task.

Default posture:

- bounded source write access;
- owns HOW inside frozen boundaries;
- runs the real-enough changed path and produces receipts;
- cannot self-freeze, self-approve, self-merge or self-close material work;
- production mutation requires separate owner authority.

### Independent Judge

Purpose: perform read-only closure for HIGH-risk or policy-required work.

Default posture:

- source/diff: read-only;
- CI/receipts: read-only;
- production telemetry: read-only only when separately authorized;
- product/source mutation: denied;
- production mutation: denied;
- provider/external side effects: denied.

The Judge does not fix defects. It returns findings/closure status to the Manager/Operator.

## 2. Core flow

```text
Operator intent
    ↓
Designer — contract + advisory
    ↓
Manager — review / freeze / bounded authority
    ↓
Executor — implement / test / commit / PR
    ↓
Cold/adversarial review when appropriate
    ↓
Manager — consolidated findings
    ↓
One bounded remediation round by default
    ↓
Independent Judge — read-only closure when required
    ↓
Operator — business / production authority
```

Remember:

```text
Designer proposes.
Manager governs and reviews.
Executor executes.
Judge independently assesses closure.
Evidence limits the claim.
Operator retains real authority.
```

## 3. Independence is more than a different model name

For HIGH-risk closure, assess four dimensions:

| Dimension | Meaning |
|---|---|
| implementation independence | Judge did not materially implement the candidate change |
| context independence | Judge starts from task/source/diff/receipts, not only prior summaries |
| authority independence | Executor cannot approve/merge/close itself |
| evidence independence | Judge inspects underlying receipts/runtime evidence rather than repeating another conclusion |

Model/vendor diversity is useful defense-in-depth, but:

```text
MULTI-MODEL AGREEMENT != INDEPENDENT BEHAVIORAL EVIDENCE
```

Three models can share the same wrong assumption or weak test oracle. Real-path tests, falsifying checks, runtime observations and recovery controls remain the primary defense.

## 4. Recommended Git and runtime permissions

| Role | Read source | Write source | Review PR/diff | Prod read | Prod mutation |
|---|---:|---:|---:|---:|---:|
| Designer | yes | no | read-only if useful | normally no | no |
| Executor | yes | bounded task branch | self-check only | owner approval | owner approval |
| Manager | yes | normally no | yes | owner approval | normally no |
| Independent Judge | yes | no | yes, read-only | owner approval | no |

For real enforcement, use separate identities/tokens/apps/permission scopes where practical. Merely telling multiple sessions to behave differently does not create a security boundary if all of them share one unrestricted credential.

### Recommended repository controls

```text
protected main/default branch
→ isolated Executor branch
→ PR required
→ required CI/checks
→ Manager reviews exact base/head
→ bounded remediation if needed
→ Independent Judge for HIGH when required
→ authorized merge
```

Avoid giving an autonomous Executor or Judge a credential that can bypass branch protection or mutate production.

## 5. Direct Git access is preferred

Direct Git access lets Designer/Manager/Judge independently inspect repository identity instead of relying on copied summaries.

Each review artifact should record:

```text
repository
branch
base/head SHA
relevant dirty-state caveat
files/symbols inspected
receipts inspected
known unknowns
```

A new head after approval/review makes the old review stale for the new delta unless policy explicitly says otherwise.

## 6. If a role lacks Git access

Use a bounded [Context Packet](CONTEXT_PACKET.md) containing only what the role needs:

```text
repository identity / branch / HEAD
relevant source excerpts or diff
current task/profile refs
build/test entrypoints
raw receipt/artifact refs
known operational/security constraints
unknowns
```

Do not substitute a copied narrative for direct code review when HIGH-risk closure is expected.

## 7. Human should not be the message bus

Use this operating rule:

```text
Human transports authority.
Repository transports engineering state.
```

The operator should make real decisions:

- approve/reject scope;
- accept residual risk;
- authorize external effects or production;
- choose business priority;
- override architecture/product constraints when appropriate.

The operator should not have to permanently copy/paste:

```text
Executor report
→ Manager findings
→ Executor fix report
→ Judge packet
```

Instead, persist compact task/review/receipt artifacts that each role can read directly.

A durable checkpoint should include current task, exact head, findings, remediation status, receipts/gaps and next required authority decision. Once durable, a fresh session can continue without replaying old conversation history.

## 8. Model/cost routing

Agentic Flow is vendor-neutral. A practical project may route by capability and cost:

```text
Executor          → task-adequate / cost-efficient
Manager           → higher reasoning when justified
Independent Judge → high reasoning + separate context
```

Model diversity for the Judge is preferred when it adds useful defense-in-depth, but it is not proof by itself and should never replace real evidence.

Cost pressure must not weaken the acceptance/evidence bar.

## 9. Remediation target

For MEDIUM/HIGH work, prefer:

```text
implementation
→ cold/adversarial review
→ Manager consolidated findings
→ ONE bounded remediation
→ re-review
→ Judge if required
```

Default `max_iterations` should normally be `1`. A second iteration requires a **new material finding**, remains inside the configured maximum and cannot silently expand scope.

A new provider, migration, public contract, security boundary, production action, dependency, architecture strategy or out-of-boundary file invalidates the remediation window.

## 10. Production separation

Production mutation is its own boundary.

- Designer: no production mutation.
- Manager: normally review/authorize only within delegated policy, not apply.
- Independent Judge: read-only, no production mutation.
- Executor: may mutate production only with explicit owner/project authority.

Before every production mutation require exact target/change identity, health/success signals, abort condition, rollback or forward recovery, data constraints, recovery owner and post-change verification.

Judge PASS is not production authority.

## 11. Copy-ready prompts

Use:

- `prompts/operator/TASK_DESIGNER.md`
- `prompts/operator/MANAGER_REVIEWER.md`
- `prompts/operator/INDEPENDENT_JUDGE.md`

The Executor should normally start at `docs/agent/START_HERE.md` and the current frozen task/profile rather than loading this whole operator guide.

## 12. Anti-patterns

Avoid:

```text
same Executor writes task, implements, approves and closes
three models say PASS, therefore integration is assumed proven
Judge reads only Manager summary and never inspects raw receipts/diff
Judge has unrestricted production mutation credentials
Manager fixes code and then claims independent closure
human permanently copy/pastes engineering state between agents
second remediation round happens only because first review was shallow
model cost optimization lowers evidence requirements
all roles share one unrestricted production credential
```

Separation is useful only when authority, context and evidence remain genuinely separated.
