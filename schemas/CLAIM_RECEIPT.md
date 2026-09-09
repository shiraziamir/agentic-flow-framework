# Claim–Receipt Contract

**Schema version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

A report may say only what its receipts support. Model confidence, reviewer approval, code presence, or a passing unrelated test do not upgrade a claim.

```yaml
claim_id: C1
statement: <exact bounded statement>
claim_kind: STATIC_EXISTENCE|BUILDABILITY|LOCAL_BEHAVIOR|INTEGRATION_CONTRACT|USER_VISIBLE|PERSISTENCE|DEPLOYMENT|PERFORMANCE|SECURITY_CONTROL|NEGATIVE_GLOBAL
truth_class: OBSERVED|DERIVED|INFERRED|UNKNOWN|CONTRADICTED
verification_status: VERIFIED|PARTIAL|UNVERIFIED|CONTRADICTED
minimum_receipt: <required strength>
receipt_refs: [E1]
valid_for:
  repository_ref: <commit/hash>
  artifact_ref: <image/build/hash or NONE>
  environment: <local/testenv/staging/prod/identity or NONE>
  observed_at: <RFC3339>
method_boundary: <what was actually checked>
```

## Truth classes

- `OBSERVED` — directly visible in Git/tool/test/live output at an identified ref/environment.
- `DERIVED` — deterministic calculation from observed inputs; name the inputs/method.
- `INFERRED` — reasoned conclusion not directly established by the receipts.
- `UNKNOWN` — required information is missing/unobservable.
- `CONTRADICTED` — current receipt conflicts with the claim.

Do not use subjective confidence as a replacement for these classes.

## Verification ladder

From weaker/narrower to stronger/broader evidence:

1. `IDENTITY` — commit/ref, diff, artifact/environment identity.
2. `STATIC` — source/config/schema inspection.
3. `BUILD` — exact lint/typecheck/compile/build at the identified ref.
4. `FOCUSED_TEST` — targeted deterministic test exercising the intended unit/component.
5. `PATH_PROOF` — evidence the changed path/test assertion can actually influence the result (coverage/instrumentation/mutation/adversarial failure where justified).
6. `INTEGRATION_CONTRACT` — real boundary/client/handler/repository interaction or contract verification.
7. `LIVE_BEHAVIOR` — browser/runtime/test-environment observation of the relevant behavior.
8. `DEPLOYED_ARTIFACT` — target environment identity plus exact artifact/image/config identity and live check.
9. `EXHAUSTIVE_BOUNDED_NEGATIVE` — a negative/global claim over a named finite universe with an exhaustive method.
10. `JUDGMENT` — independent interpretation of the above. Judgment does not substitute for missing behavioral evidence.

Not every claim needs the highest rung. Use the lowest rung that directly establishes the claim.

## Minimum receipt examples

| Claim | Minimum adequate receipt |
|---|---|
| `file/config contains X` | IDENTITY + STATIC |
| `project builds` | IDENTITY + exact BUILD result |
| `function behavior changed as intended` | FOCUSED_TEST; PATH_PROOF when the test itself is load-bearing/suspect |
| `frontend user flow works` | LIVE_BEHAVIOR through user-visible interaction; build/unit tests alone are insufficient |
| `frontend/provider contract is compatible` | INTEGRATION_CONTRACT using the actual consumer boundary/client where practical |
| `API endpoint behaves correctly` | handler/service integration receipt appropriate to the claim, including relevant error/auth paths |
| `data persists` | write/read or equivalent persistence receipt against the named storage boundary; HTTP 200 alone is insufficient |
| `deployed to environment X` | DEPLOYED_ARTIFACT with environment + artifact identity; repository commit alone is insufficient |
| `performance improved` | comparable repeated benchmark/load method with baseline, environment and variance/summary |
| `security control fixed` | relevant security verification including negative/adversarial path; reviewer opinion alone is insufficient |
| `no regressions` | normally forbidden as an unbounded claim; report the exact suites/surfaces checked |
| `no other files changed` | bounded/exhaustive Git diff over the named base/head |

## Negative/global claim rule

Claims using words such as `all`, `none`, `no regression`, `no security issue`, `only`, `every`, or `nothing else` require either:

- a named finite universe plus exhaustive check; or
- narrower wording that states the method boundary.

Prefer:

`128/128 required tests passed at <ref>; frontend browser smoke for flows A/B passed; security was not exhaustively assessed.`

not:

`Everything is good and there are no regressions.`

## Freshness rule

Evidence is valid only for the ref/artifact/environment it identifies. Any material mutation after evidence collection makes prior behavioral evidence stale unless the verifier establishes that the mutation cannot affect the claim.
