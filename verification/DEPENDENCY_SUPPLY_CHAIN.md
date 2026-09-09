# Verification Annex — DEPENDENCY / SUPPLY CHAIN

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use for dependency manifest/lockfile changes, package/runtime upgrades, GitHub Action/reusable-workflow dependencies, container/base-image changes, or dependency updates with security/license/runtime implications.

## Core checks

1. identify direct **and transitive** dependency changes between base/head where tooling supports it;
2. inspect manifest and lockfile diff rather than assuming a requested direct version is the only change;
3. run ecosystem/package build, tests and affected consumer verification;
4. check known vulnerability/advisory information with the repository's approved tooling when available;
5. check license/policy constraints when they are part of project governance;
6. inspect relevant upstream release/migration notes for breaking/runtime/config changes when the update is material;
7. verify runtime/engine/platform compatibility (language/runtime, OS/arch, database/client/protocol) when applicable;
8. verify generated lock/resolution state is reproducible and source/lock are synchronized;
9. for GitHub Actions/reusable workflows/container/base images, identify the exact version/ref/digest policy used rather than assuming a mutable tag means immutable code;
10. record dependency-security tooling coverage/limitations; absence of a finding is bounded by the database/ecosystem/tool coverage.

## Receipt rules

- A one-line manifest change can produce many transitive lockfile changes.
- `build passes` does not prove the dependency introduced no known vulnerability or policy/license issue.
- `dependency review passed` is bounded to dependencies/ecosystems/data the tool can parse and assess; also inspect source/manifest diff where relevant.
- A vulnerability scanner finding is evidence of a known advisory match, not automatic proof of exploitability in this project.
- A scanner with no findings is not an unbounded `secure` receipt.

## Blind spots

- unexpected transitive upgrade/downgrade;
- package name confusion/wrong dependency;
- runtime or peer-dependency incompatibility;
- lockfile not regenerated or regenerated with unexpected package-manager version;
- package/build scripts or code generation introduce side effects;
- known vulnerability/license issue introduced;
- removed transitive dependency changes runtime behavior unexpectedly;
- mutable action/image tag resolves to different code/artifact later;
- platform-specific native binary fails only on target OS/architecture;
- upstream breaking change not represented by compile/type checks.

GitHub's official dependency review can show added/removed/updated direct and indirect dependencies, vulnerability information and available license metadata; use it when available, but do not treat it as coverage for ecosystems or changes it cannot parse.
