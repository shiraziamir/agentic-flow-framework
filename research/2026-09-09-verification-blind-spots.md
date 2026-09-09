# Research note — verification blind spots, receipts and engineering surfaces

**Date:** 2026-09-09  
**Framework target:** v1.5  
**Status:** research/evidence, not policy authority

This note records the evidence behind v1.5. Canonical policy lives in `ARCHITECTURE.md`.

## 1. Repository reports need executable feedback loops, not agent confidence

OpenAI's Harness Engineering report describes an agent-first repository where UI behavior, logs and metrics are made directly legible to Codex so the agent can reproduce bugs and validate fixes. It also describes mechanically enforced architectural dependency directions, custom linters and structural tests. The implication for this framework is that deterministic and runtime-observable facts should be checked with tools/receipts rather than delegated to narrative model confidence.

Source:
- https://openai.com/index/harness-engineering/

## 2. Low-risk friction and high-risk review should be separated

OpenAI's Codex safety deployment states the principle explicitly: everyday low-risk actions should be productive/frictionless, while higher-risk actions stop for review. It also emphasizes sandbox boundaries and agent-native telemetry/audit trails. This supports risk-adaptive governance plus explicit mutation/environment identity rather than identical ceremony for every edit.

Source:
- https://openai.com/index/running-codex-safely/

## 3. Define success/verification before implementation or grading

Anthropic's evaluation guidance recommends specific, measurable success criteria and task-specific evals including edge cases, and prefers automated/code grading where it is reliable. Its Managed Agents outcome grader uses a separate context window from the implementation session. These support freezing observable DoD/claim rubrics before APPLY and using cold review to reduce implementation-context anchoring.

Sources:
- https://platform.claude.com/docs/en/test-and-evaluate/develop-tests
- https://platform.claude.com/docs/en/managed-agents/define-outcomes

## 4. Skills themselves require trigger/non-trigger/coexistence evaluation

Anthropic's enterprise Skills guidance warns that Skills can degrade performance through incorrect triggers, conflicts or poor instructions, and recommends evaluation of triggering accuracy, isolation, coexistence, instruction following and output quality, with separation of duties between authors and reviewers.

Source:
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise

Framework implication: usage count alone cannot validate a skill; trigger denominators and controlled/non-trigger fixtures remain necessary.

## 5. Frontend verification should observe user-visible behavior

Playwright's official best practices recommend testing user-visible behavior instead of implementation details, using isolated tests and user-facing/resilient locators. A component test or screenshot may be useful evidence but cannot automatically establish an end-user interaction flow.

Source:
- https://playwright.dev/docs/best-practices

## 6. Shared/API contract tests must exercise the real boundary

Pact's documentation stresses that contract tests should exercise the actual consumer API client rather than hand-constructing HTTP requests, because otherwise the contract may pass while the consumer code still fails. It also distinguishes contract compatibility from provider functional correctness and warns about permissive providers silently ignoring incorrect inputs.

Source:
- https://docs.pact.io/consumer

Framework implication: `SHARED/PUBLIC_CONTRACT` verification must consider producer + affected consumers and distinguish type/schema compatibility from runtime client/provider behavior.

## 7. Security claims need a named verification scope/version

OWASP ASVS provides a basis for testing web-application technical security controls and explicitly versions its requirements. ASVS 5.0.0 is the current stable release identified on the project page. Security reports should reference relevant versioned requirements when standards coverage is claimed and should avoid unbounded claims like `secure` merely because functional tests pass.

Source:
- https://owasp.org/www-project-application-security-verification-standard/

## 8. Green CI is not proof every check executed

GitHub protected-branch documentation states required status checks can be `successful`, `skipped`, or `neutral` and still satisfy the merge gate. Therefore a green PR/check surface is not, by itself, proof that a particular test/job ran. Verification reports should preserve executed/skipped/not-run status where that distinction matters.

Source:
- https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches

## 9. Logical project boundaries improve affected verification

TypeScript Project References structure programs into smaller pieces, improve build performance and enforce logical separation. Similar project/dependency graphs in build systems can mechanically identify affected consumers and reduce whole-repository guessing.

Source:
- https://www.typescriptlang.org/docs/handbook/project-references

## 10. Audit findings in v1.4 before the update

The v1.4 framework already had strong source-of-truth, risk-adaptive governance, STOP/amendment discipline, evidence packets and independent review. The audit found these remaining blind spots:

1. `receipt exists` was not tied formally to **receipt strength vs claim strength**.
2. task contracts did not classify engineering surface, so verification could remain generic.
3. reports lacked a universal `OBSERVED/DERIVED/INFERRED/UNKNOWN/CONTRADICTED` truth model.
4. evidence did not consistently bind behavior to exact repository/artifact/environment identity and freshness.
5. negative/global claims lacked an explicit finite-universe/exhaustive-method rule.
6. draft review was not a first-class prompt for verification-design review before APPLY.
7. frontend/backend/shared/data/infra blind spots were not routed by surface profile.
8. `CI green`, screenshot, HTTP success, mock success and reviewer approval could be over-interpreted without a formal prohibition.
9. independent review did not explicitly recommend inspecting raw diff/receipts before executor narrative to reduce anchoring.
10. deterministic artifact contradictions had no portable linter.

v1.5 addresses these with `schemas/CHANGE_CLASSIFICATION.md`, `schemas/CLAIM_RECEIPT.md`, `schemas/STATUS_REPORT.md`, `verification/`, `change-classification`, `surface-verification`, `blind-spot-audit`, a formal draft-review prompt and `scripts/verification_lint.py`.

## 11. Design rule

The framework now uses this invariant:

> A claim may be no broader than the identified, current receipt that directly establishes it.

A stronger model or reviewer can improve judgment about evidence; it cannot manufacture missing evidence.
