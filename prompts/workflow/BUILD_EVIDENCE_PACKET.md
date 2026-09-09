# Workflow prompt — BUILD EVIDENCE PACKET

```text
Build the closure evidence packet for the current task. Do not decide closure yourself.

Read:
- the frozen task contract;
- schemas/EVIDENCE_PACKET.md;
- all actual task receipts;
- current repository/diff/test state.

Requirements:
- identify base/head refs and exact changed paths;
- list each material claim separately;
- map every Definition-of-Done item to current evidence;
- include exact commands/sources and bounded result summaries;
- include known failures, baseline comparison and disposition;
- include live/mutation receipts when required by the frozen contract;
- include unresolved facts and residual risk;
- preserve PASS/FAIL/PARTIAL/UNVERIFIED exactly;
- if N checks were required and M passed, report M/N and failures;
- do not substitute easier tests for frozen gates;
- do not include chain-of-thought or full transcripts.

Return a packet conforming to schemas/EVIDENCE_PACKET.md and the requested supervisor decision. Mark task EVIDENCE_READY, not CLOSED.
```
