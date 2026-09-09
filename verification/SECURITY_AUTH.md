# Verification Annex — SECURITY / AUTH

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use when authentication, authorization, tenant/ownership boundaries, secrets, untrusted input, security controls or trust semantics are touched.

## Core checks

1. identify the security boundary/threat relevant to this change;
2. verify positive path and at least the relevant negative/unauthorized path;
3. verify tenant/ownership/object-level authorization when applicable;
4. verify untrusted input validation/encoding/query construction at the real boundary;
5. verify secrets/credentials are not exposed in source, logs or receipts;
6. verify privilege/permission changes use the minimum intended authority;
7. verify security-sensitive fallback/error behavior does not fail open;
8. for a claimed vulnerability fix, reproduce the exploit/failure before the fix when safe/feasible and demonstrate the relevant path no longer succeeds after the fix;
9. reference versioned external verification requirements (for web apps, e.g. relevant OWASP ASVS version/requirement) when the task calls for standards coverage.

## Receipt rules

- Functional success is not authorization proof.
- `401/403 exists somewhere` is not proof the changed resource/tenant boundary is protected.
- Static scanner/reviewer findings are useful but do not automatically establish exploitability or remediation; validate the relevant path where practical.
- `secure` or `no vulnerabilities` is normally an invalid global claim unless a defined verification scope/standard justifies it.

## Blind spots

- authenticated but wrong tenant/owner can access object;
- client-side check exists but server enforcement is missing;
- default/fallback role becomes over-privileged;
- secret appears only in error/log/debug path;
- indirect injection/path traversal/command execution via transformed input;
- authorization checked on read but not mutation/export/bulk path;
- cache or pre-signed artifact bypasses current authorization;
- security test covers synthetic helper instead of real route;
- standards requirement cited without version or without actually testing it.

OWASP ASVS is a versioned verification standard; when referencing a requirement, include the ASVS version so the claim remains stable as the standard evolves.
