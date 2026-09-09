# Workflow prompt — APPLY TASK

**Version:** 1.1  
**Updated:** 2026-09-09T10:04:00Z

```text
Execute the authorized frozen task contract exactly as reviewed.

Before mutation:
1. read ARCHITECTURE.md;
2. load frozen task contract + classification + authorization/amendment;
3. load only skills frozen by the contract;
4. load GENERAL + selected verification surface profiles/annexes only;
5. curate the smallest working context;
6. confirm base/head/working-tree identity, STOP/escalation/reclassification conditions and planned claim -> receipt matrix.

During execution:
- stay inside EDIT_SET and frozen strategy;
- use deterministic tools before LLM work when practical;
- retry execution only within approved strategy;
- if a new material surface, consumer, security/persistence/public-contract/production risk or changed prerequisite appears, STOP and request amendment/reclassification;
- gather receipts as work proceeds rather than reconstructing them from memory later;
- bind receipts to exact repository/artifact/environment identity;
- preserve FAIL/PARTIAL/SKIPPED results;
- if a test may bypass/cache/mock the changed path, gather PATH_PROOF where justified;
- do not replace an exact frozen acceptance gate with a weaker proxy without amendment;
- do not self-close the task.

After implementation:
- run required GENERAL + surface/annex verification and frozen baselines;
- record material checks not executed and why;
- build an evidence packet conforming to schemas/EVIDENCE_PACKET.md;
- build a reality-reflecting status report conforming to schemas/STATUS_REPORT.md;
- run blind-spot audit if frozen/triggered;
- mark task EVIDENCE_READY, not CLOSED;
- hand off to the required supervisor.
```
