# Adoption Receipt — Agent Output Contract

**Agent-facing**  
**Version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

After drop-in or midstream adoption, return a compact receipt such as:

```yaml
framework_version: <VERSION>
adoption_mode: NEW|EXISTING_IDLE|MIDSTREAM
framework_root: <path>
repository_ref: <HEAD>
branch: <branch>
dirty_paths: []
existing_instruction_files: []
adapters_changed: []
project_profile:
  path: <path|PROPOSED>
  status: EXISTING|CREATED|PROPOSED
operational_gaps: []
conflicts: []
current_task_reconciliation: <ref|NONE>
validation:
  source_of_truth_discoverable: PASS|FAIL
  build_test_commands_discoverable: PASS|FAIL|UNVERIFIED
  verification_router_discoverable: PASS|FAIL
  production_router_discoverable: PASS|FAIL
  cold_operator_docs_not_preloaded: PASS|FAIL
next_authorization_required: <text|NONE>
```

Do not report PASS for checks that were not actually performed.
