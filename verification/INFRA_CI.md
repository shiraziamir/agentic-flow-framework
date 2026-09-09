# Verification Profile — INFRA / CI_CD

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for infrastructure, Kubernetes/cloud/network config, build/release pipelines and deployment orchestration.

## Core checks

1. identify exact target account/subscription/cluster/environment/branch/ref;
2. syntax/schema/validate the configuration;
3. inspect plan/diff/rendered manifest where tooling supports it;
4. classify read-only vs mutation actions and required authorization;
5. verify permissions/identity/secret references without exposing secret values;
6. verify pipeline triggers, conditions, branch/environment mapping and artifact handoff;
7. verify actual artifact/image/config identity across build → deploy boundary;
8. run a real pipeline/deploy/testenv smoke when the claim requires operational proof;
9. verify rollback/recovery mechanism appropriate to the change;
10. inspect relevant health/log/event/status output after mutation.

## Receipt rules

- A valid YAML/Terraform/manifest proves syntax/planability, not that the target environment changed.
- A repository image tag does not prove which digest is running.
- `CI green` does not prove every relevant job/test executed; report skipped/neutral/not-run checks when material.
- A pipeline definition that looks correct is weaker than a real run receipt when triggers/artifact flow are the claim.

## Infra/CI blind spots

- wrong subscription/account/cluster/context/namespace/environment;
- plan evaluated against stale state/provider/plugin version;
- mutable tag points at unexpected artifact;
- branch condition prevents a stage from running while overall pipeline stays green;
- job is skipped/neutral yet report says all tests ran;
- build and release consume different artifact/version;
- secret/identity permission only fails at runtime;
- rollout health passes while application-specific smoke fails;
- rollback path exists on paper but not for the actual data/config mutation;
- generated/rendered manifest differs from source assumptions;
- local validation uses different variable/overlay values from target.

For production mutation, keep explicit owner authorization and preserve environment/artifact identity in the receipt.
