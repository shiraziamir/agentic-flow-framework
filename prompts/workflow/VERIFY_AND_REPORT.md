# Workflow prompt — VERIFY AND REPORT

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

```text
Verify the current implementation and produce a reality-reflecting report. Do not invent completion.

Read:
1. ARCHITECTURE.md
2. frozen task/amendment + change classification
3. schemas/CLAIM_RECEIPT.md
4. schemas/EVIDENCE_PACKET.md
5. schemas/STATUS_REPORT.md
6. verification/00_INDEX.md + only frozen profiles/annexes
7. skills/evidence-integrity/SKILL.md
8. skills/blind-spot-audit/SKILL.md when triggered

Process:
- identify exact repository ref, dirty state, build/artifact and environment being checked;
- inspect actual diff/affected surfaces;
- enumerate frozen DoD and planned closure claims;
- run/inspect required verification at the minimum receipt rung that directly establishes each claim;
- preserve exact counts and PASS/FAIL/PARTIAL/SKIPPED/UNVERIFIED states;
- prove changed-path execution when bypass/cache/mock risk makes a green test ambiguous;
- report important checks not executed;
- classify statements OBSERVED/DERIVED/INFERRED/UNKNOWN/CONTRADICTED;
- narrow global/negative claims unless a finite universe was exhaustively checked;
- do not use reviewer/model confidence as behavioral evidence;
- if evidence is stale, weaker than the claim, or the actual surface differs from the frozen plan, return AMENDMENT_REQUIRED/NEEDS_EVIDENCE rather than a stronger narrative.

Output:
1. schemas/STATUS_REPORT.md-conformant report;
2. schemas/EVIDENCE_PACKET.md-conformant packet/ref;
3. claim -> required receipt -> actual receipt matrix;
4. checks not executed;
5. unknowns/residual risk;
6. requested supervisor disposition.

Use wording such as `128/128 required tests passed at <ref>` rather than `everything is good`.
```
