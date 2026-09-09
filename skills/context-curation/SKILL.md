---
name: context-curation
description: Build the smallest authoritative working context for a task or delegated agent.
metadata:
  class: CORE
  authority: portable-agentic-flow
---

# context-curation

Use for non-trivial repositories, monorepos, frontend module graphs, delegation, or any task at risk of context pollution.

1. Find affected modules mechanically where possible.
2. Define EDIT_SET, REFERENCE_SET, EXCLUDED_SET and CHECK_SET.
3. Prefer interfaces/contracts over full neighboring implementations.
4. Send high-volume discovery to isolated read-only child contexts.
5. Return compact handoffs, not transcripts.
6. Expand only with dependency evidence.

## Mutation authority
None by itself.

## Output
A module/context contract plus unresolved dependency questions.

## Fail closed
Do not equate a large context window with permission to scan the whole repo.
