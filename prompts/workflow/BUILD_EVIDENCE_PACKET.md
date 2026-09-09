# Workflow prompt — BUILD EVIDENCE PACKET

**Version:** 1.1  
**Updated:** 2026-09-09T10:04:00Z

```text
Build the closure evidence packet for the current task. Do not decide closure yourself.

Read:
- the frozen task/amendment + change classification;
- schemas/CLAIM_RECEIPT.md;
- schemas/EVIDENCE_PACKET.md;
- schemas/STATUS_REPORT.md;
- selected verification profiles/annexes;
- all actual task receipts;
- current repository/diff/build/artifact/environment state.

Requirements:
- identify exact base/head refs, dirty state, changed/unexpected paths, artifact/build identity and environment where relevant;
- list each frozen/material claim separately;
- classify each statement OBSERVED/DERIVED/INFERRED/UNKNOWN/CONTRADICTED;
- record the minimum receipt rung frozen for each claim and the actual receipt(s);
- map every Definition-of-Done item to current evidence;
- include exact commands/sources/methods, bounded results, counts and method boundaries;
- bind behavioral evidence to the exact repository ref/artifact/environment and observation time;
- preserve PASS/FAIL/PARTIAL/SKIPPED/UNVERIFIED exactly;
- list important checks not executed and why;
- include known failures, baseline comparison, unexpected findings and disposition;
- include PATH_PROOF / integration / live / persistence / deployment / mutation receipts when required by the frozen claim/profile;
- if N required checks exist and M pass, report M/N plus failing/skipped/unverified items;
- narrow any global/negative claim unless a finite universe was exhaustively checked;
- if evidence is stale, missing or below the frozen minimum receipt, mark PARTIAL/UNVERIFIED rather than strengthening the narrative;
- do not substitute easier tests for frozen gates;
- do not use reviewer/model judgment as missing behavioral evidence;
- do not include chain-of-thought or full transcripts.

Return:
1. a packet conforming to schemas/EVIDENCE_PACKET.md;
2. a reality snapshot conforming to schemas/STATUS_REPORT.md (or ref to the separately generated report);
3. the requested supervisor disposition.

Mark task EVIDENCE_READY, not CLOSED.
```
