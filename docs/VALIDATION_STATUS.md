# Validation Status

**Updated:** 2026-09-13  
**Scope:** this repository and its portable bundle, not adopter projects.

## Current status

The framework is usable as a documented operating method and its deterministic helpers are self-tested. It is **not yet empirically validated as superior** to ordinary coding-agent workflows.

| Area | Status | Current receipt |
|---|---|---|
| Python helper syntax/importability | VERIFIED in repository checks | Python compilation and helper self-tests |
| verification-lint invariants | VERIFIED for included fixtures | `scripts/test_verification_lint.py` |
| production-readiness-lint invariants | VERIFIED for included fixtures | `scripts/test_production_readiness_lint.py` |
| quota snapshot normalization | VERIFIED for included fixtures | `scripts/test_claude_usage_snapshot.py` |
| portable bundle selection/manifest/hash behavior | VERIFIED for included fixtures and clean-checkout CI | bundle builder tests and workflow |
| newcomer documentation / role-policy wiring | VERIFIED mechanically for required strings/files | `scripts/test_docs_onboarding.py` |
| Independent Judge prompt included in portable bundle | VERIFIED mechanically | bundle builder self-test |
| effectiveness on real project outcomes | UNPROVEN | no controlled comparative study |
| reduction in false-complete rate | UNPROVEN | no measured baseline/control |
| benefit of multi-model review vs same-model review | UNPROVEN / PROJECT-DEPENDENT | no controlled model-independence study in this repository |
| portability across all vendors/harnesses | PARTIAL / UNPROVEN | vendor-neutral documents and selected adapters; no exhaustive matrix |
| production readiness of an adopting project | NOT INFERABLE | requires that project’s profile, gaps and current receipts |

## What local PASS means

A local PASS shows that the checked deterministic invariant held for the identified checkout and fixtures. It does not prove agent compliance, behavior in another repository, successful deployment, security, performance or organizational effectiveness.

It validates repository mechanics and policy wiring, not the effectiveness of the framework in real projects.

## Multi-model limitation

Multiple models agreeing is **not** treated as independent behavioral evidence. Models can share assumptions, training patterns, weak test oracles or the same incomplete context.

```text
model A PASS + model B PASS + model C PASS
!=
integration / deployment / production proof
```

Model diversity may improve review coverage, but the evidence class is still determined by the underlying receipts and observed runtime boundaries.

Independent closure therefore emphasizes implementation, context, authority and evidence separation rather than model-name voting.

## Known limitations

- Markdown schemas are contracts, not machine-enforced schemas everywhere.
- Role separation is procedural unless separate identities, permissions, branch protection and CI enforce it.
- A context packet can be incomplete or stale.
- Model diversity does not guarantee statistical or cognitive independence.
- The quality of claim-to-receipt mapping still requires judgment.
- “Production-like” is property-specific; no lower environment reproduces all production conditions.
- Primary sources support component practices, not the framework’s total effectiveness.
- Vendor-specific adapter and quota behavior can change.
- Artifact-driven handoff reduces chat dependence but still requires adopters to maintain accurate durable task/review state.

## Evidence needed to strengthen the claim

A credible validation program would publish:

- a defined task corpus and project mix;
- baseline and Agentic Flow treatment protocols;
- false-complete, escaped-defect, review-rework, lead-time and cost measures;
- blinded or independent grading;
- comparison of same-model vs cross-model review where relevant;
- environment and model/harness identity;
- failures, negative results and confidence/variance;
- reproducible artifacts that do not expose private code or data.

Until then, describe Agentic Flow as an evidence-oriented framework under active validation—not as proven best practice or universally production-ready.
