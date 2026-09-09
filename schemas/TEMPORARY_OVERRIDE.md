# Temporary Override Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09T11:30:00Z

Use when a project baseline requirement must be temporarily weakened, disabled or deferred. Never edit the baseline silently merely because a task needs a short-lived exception.

```yaml
override_id: <stable-id>
version: 1
created_at: <RFC3339>
expires_at: <RFC3339>
owner: <human/team>
authority_ref: <owner/judgment/change ref>

baseline_ref: .agentic/PROJECT_PROFILE.yaml
requirement: <exact requirement>
previous_state: <value>
temporary_state: <value>
reason: <why this exception is needed>
scope:
  environments: []
  services: []
  paths: []

risk_created:
  - <observable risk>
compensating_controls:
  - <temporary guard/check>
required_monitoring:
  - <signal to watch while override is active>
stop_or_abort_conditions:
  - <condition requiring immediate restore/rollback>
restore_plan: <how baseline state is reinstated>
verification_after_restore:
  - <receipt>
status: APPROVED|ACTIVE|EXPIRED|RESTORED|REVOKED
```

## Examples

Valid examples include temporarily suppressing a noisy non-safety alert while a corrected metric is deployed, temporarily disabling an optional telemetry series due to a cardinality incident, or temporarily relaxing a non-production test gate while its infrastructure is repaired.

Invalid examples include silently disabling backup, restore capability, security authorization, audit logging required by policy, or production health gates merely to make a release pass.

## Expiry rule

Expired override != permission. An expired override becomes an operational gap/incident candidate until the baseline is restored or a new explicit decision is made.
