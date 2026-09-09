---
name: receipts-not-claims
description: Require factual engineering claims to carry observable receipts or an explicit unverified label.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# receipts-not-claims

Use whenever status, diagnosis, implementation, test, deployment, performance, or closure claims matter.

For each material claim attach one of:
- file/diff/config receipt;
- test command/result;
- live/runtime observation;
- mutation proof;
- external primary source;
- explicit `UNVERIFIED` label.

Do not infer implementation from plans, deployment from code presence, or correctness from model confidence.

## Mutation authority
None.

## Output
Claim → receipt mapping, with unverified claims called out explicitly.
