# Clone-Based Adoption Prompt

Use when Agentic Flow is available as a cloned repository beside or inside the target project.

## Operator prompt

```text
Adopt Agentic Flow for this repository.

Framework source: <path-to-agentic-flow-framework>

Start by reading:
- <framework>/docs/agent/START_HERE.md
- <framework>/ARCHITECTURE.md

Inspect this project read-only first. Do not modify product files, configuration, infrastructure, data, or runtime state yet.

Use STRICT_PREVIEW mutation approval unless this project's existing .agentic/PROJECT_PROFILE.yaml explicitly defines another mode.

Before every mutation batch, report:
1. CURRENT STATE — what is true now;
2. PROPOSED STATE — what will be true after the change;
3. WHY — reason for the change;
4. WILL CHANGE — files/resources expected to mutate;
5. IMPACT — behavior/API/security/data/operations impact;
6. VERIFY — checks/tests you will run;
7. ROLLBACK/RECOVERY — when material;
8. OUT OF SCOPE — what you will not change.

Then stop and wait for explicit APPROVE/APPLY.
Approval is limited to the previewed batch. If implementation discovers a materially different change, stop, explain the new reality, present a revised preview, and request approval again.

If coding is already in progress, follow docs/agent/MIDSTREAM_ADOPTION.md first and preserve current valid edits.

Do not preload operator/reference/research documentation. Load detailed framework files only when triggered by the current task.
```

## Expected adoption result

The agent should return a concise read-only snapshot before requesting its first mutation:

```text
framework ref/version
project branch/HEAD/dirty paths
existing agent instruction files
current task/issue if any
build/test/deploy entrypoints discovered
project profile status
mutation approval mode
conflicts/gaps
next proposed mutation batch: none until requested/approved
```
