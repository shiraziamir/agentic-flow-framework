# Production Profile Schema

**Schema version:** 1.0  
**Updated:** 2026-09-09T10:40:00Z

A production-capable project should have one durable profile. This profile does not claim readiness; it defines the required operating bar and known gaps.

```yaml
profile_id: <stable-id>
version: <semver-or-integer>
updated_at: <RFC3339>

codebase_scale: SMALL|MEDIUM|LARGE
operational_complexity: LOW|MEDIUM|HIGH
readiness_tier: BASIC|STANDARD|HIGH_ASSURANCE

business_context:
  user_facing: true|false
  internet_exposed: true|false
  multi_tenant: true|false
  stateful: true|false
  durable_data_criticality: NONE|LOW|HIGH
  data_classification: PUBLIC|INTERNAL|SENSITIVE|REGULATED
  compliance_or_contractual_constraints: []
  blast_radius: LOCAL|SERVICE|MULTI_SERVICE|CUSTOMER_CRITICAL

runtime:
  environments: [dev, test, staging, production]
  deployment_platforms: []
  runtime_owners: []
  oncall_or_support_owner: <owner|NONE>

recovery:
  rpo: <duration|NOT_DEFINED|NOT_APPLICABLE>
  rto: <duration|NOT_DEFINED|NOT_APPLICABLE>
  backup_required: true|false
  restore_test_required: true|false

observability:
  metrics_required: true|false
  logs_required: true|false
  traces_required: true|false
  slo_required: true|false

security:
  threat_model_required: true|false
  sbom_required: true|false
  provenance_target: NONE|SLSA_BUILD_L1|SLSA_BUILD_L2|SLSA_BUILD_L3
  vulnerability_management_required: true|false

resilience:
  failure_mode_analysis_required: true|false
  recovery_drill_required: true|false
  chaos_experiments_allowed: NONE|NON_PROD|CONTROLLED_PROD

required_profiles:
  - DELIVERY
  - OBSERVABILITY
  - SECURITY_FIRST
  # add DATA_DURABILITY, TROUBLESHOOTING, RESILIENCE_CHAOS,
  # AI_LOG_ANALYSIS, CODE_ARCHITECTURE as triggered

gaps:
  - gap_id: GAP-001
    ref: <schemas/OPERATIONAL_GAP.md artifact>
```

## Tier guidance

### BASIC

Suitable for low-blast-radius production software. Minimum bar: repeatable build, identified artifact/version, documented deploy/rollback path, basic health/logging, secrets discipline, dependency/update ownership, and backups when durable data exists.

### STANDARD

Default for normal customer-facing/stateful services. Adds automated CI/CD gates, immutable artifact identity, structured metrics/logs and useful traces, dashboards/alerts, runbooks, RPO/RTO, restore testing, vulnerability/supply-chain controls, incident ownership and failure-mode review.

### HIGH_ASSURANCE

For customer-critical, regulated, security-sensitive, high-blast-radius or difficult-to-recover systems. Adds stronger independent review, SLO/error-budget operations, progressive delivery, stronger artifact provenance, frequent recovery drills, controlled resilience experiments, explicit threat/failure models and stronger evidence for production closure.

## Scaling rule

`codebase_scale` changes the amount of decomposition and automation needed; it must not downgrade controls required by risk. A small payment/authentication service may require `HIGH_ASSURANCE`. A large internal analysis tool may remain `STANDARD` if its blast radius and data risks justify that choice.

## Gap rule

Any required capability that is absent, unverified or intentionally deferred must appear as a durable gap. Missing data is not interpreted as readiness.