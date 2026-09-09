---
name: sibling-sweep
description: After a fix, search for siblings, symmetric boundaries, and regressions in the same defect class.
metadata:
  class: COMMON
  authority: portable-agentic-flow
---

# sibling-sweep

Use when the first found instance may represent a broader class.

1. Define the defect class from evidence.
2. Mechanically search sibling sites.
3. Test symmetric/boundary cases.
4. Fix only the approved class.
5. Re-run baseline and adversarial checks.

## Mutation authority
Only within the frozen defect class/scope.

## Output
Class definition, sweep results, repaired instances, residual out-of-scope cases.
