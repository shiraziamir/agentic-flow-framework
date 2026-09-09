---
name: durable-context
description: Keep session recovery state durable and reset context only at safe semantic boundaries.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# durable-context

Use for long sessions, handoffs, provider/model changes, compaction/reset, or when facts risk living only in chat.

Before reset:
- current task state durable;
- contract/evidence/supervisor decision current;
- repo status/diff inspectable;
- no required result exists only in conversation;
- next exact action recorded.

## Mutation authority
Documentation/checkpoint updates only as authorized.

## Output
`RESET_READY` or `NOT_READY` with missing durable state, plus resume pointer.

## Fail closed
Never reset mid-task while decisive evidence exists only in transient context.
