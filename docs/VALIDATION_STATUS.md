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
| newcomer documentation topology/required policy language | VERIFIED mechanically after this change | `scripts/test_docs_onboarding.py` |
| GitHub Actions execution for the current PR head | PENDING until remote CI runs | workflow status required |
| effectiveness on real project outcomes | UNPROVEN | no controlled comparative study |
| reduction in false-complete rate | UNPROVEN | no measured baseline/control |
| portability across all vendors/harnesses | PARTIAL / UNPROVEN | vendor-neutral documents and selected adapters; no exhaustive matrix |
| production readiness of an adopting project | NOT INFERABLE | requires that project’s profile, gaps and current receipts |

## What local PASS means

A local PASS shows that the checked deterministic invariant held for the identified checkout and fixtures. It does not prove agent compliance, behavior in another repository, successful deployment, security, performance or organizational effectiveness.
It validates repository mechanics, not the effectiveness of the framework in real projects.

## Known limitations

- Markdown schemas are contracts, not machine-enforced schemas everywhere.
- Role separation is procedural unless separate identities, permissions, branch protection and CI enforce it.
- A context packet can be incomplete or stale.
- The quality of claim-to-receipt mapping still requires judgment.
- “Production-like” is property-specific; no lower environment reproduces all production conditions.
- Primary sources support component practices, not the framework’s total effectiveness.
- Vendor-specific adapter and quota behavior can change.

## Evidence needed to strengthen the claim

A credible validation program would publish:

- a defined task corpus and project mix;
- baseline and Agentic Flow treatment protocols;
- false-complete, escaped-defect, review-rework, lead-time and cost measures;
- blinded or independent grading;
- environment and model/harness identity;
- failures, negative results and confidence/variance;
- reproducible artifacts that do not expose private code or data.

Until then, describe Agentic Flow as an evidence-oriented framework under active validation—not as proven best practice or universally production-ready.
