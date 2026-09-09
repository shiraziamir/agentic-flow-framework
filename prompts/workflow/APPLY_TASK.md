# Workflow prompt — APPLY TASK

```text
Execute the authorized frozen task contract exactly as reviewed.

Before mutation:
1. read ARCHITECTURE.md;
2. load the frozen task contract and authorization;
3. load only the skills frozen by the contract;
4. curate the smallest working context;
5. confirm stop/escalation conditions.

During execution:
- stay inside EDIT_SET and frozen strategy;
- use deterministic tools before LLM work when practical;
- retry execution only within the approved strategy;
- if scope/strategy/prerequisites materially change, STOP and request amendment;
- gather receipts as work proceeds rather than reconstructing them from memory later;
- do not self-close the task.

After implementation:
- run required baseline/verification;
- build an evidence packet conforming to schemas/EVIDENCE_PACKET.md;
- mark the task EVIDENCE_READY, not CLOSED;
- hand off to the required supervisor.
```
