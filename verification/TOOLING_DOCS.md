# Verification Profile — TOOLING / DOCS_EVIDENCE

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for repository tooling, generators, documentation and evidence-contract changes that do not themselves establish product runtime behavior.

## Tooling checks

1. syntax/type/build the tool;
2. exercise representative fixture/input and expected output;
3. verify destructive side effects are bounded/authorized;
4. verify generated output is deterministic or explain nondeterminism;
5. verify failure/invalid-input path where the tool gates important workflow;
6. verify compatibility with the actual repo paths/config it is expected to consume.

## Docs/evidence checks

1. verify paths/links/commands against current repository state;
2. verify version/timestamp/source-of-truth pointers;
3. verify copied/generated values against their canonical source;
4. verify examples do not accidentally become stronger claims than the evidence;
5. run documentation freshness/cross-link checks where available;
6. ensure docs-only amendments do not silently grant runtime/mutation authority.

## Receipt rules

- Documentation that says behavior exists is not a runtime receipt.
- A schema/template change does not prove existing artifacts conform until validated.
- An example command is not evidence that it was executed.

## Blind spots

- stale command/path/version;
- duplicate policy source created by copying canonical prose;
- generated docs not regenerated after source change;
- evidence contract wording changed while old reports still claim compatibility;
- tool fixture bypasses real path/config;
- docs claim production/runtime state based only on intended config;
- timestamp/version updated cosmetically while content remains stale.
