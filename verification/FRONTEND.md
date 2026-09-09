# Verification Profile — FRONTEND

**Version:** 1.0  
**Updated:** 2026-09-09T10:04:00Z

Use when rendered UI, client state, browser navigation, frontend API client behavior, or user interaction changes.

## Core checks

Choose the checks required by the claim:

1. typecheck/lint/build for the affected frontend;
2. focused unit/component tests for logic/state where useful;
3. browser-level check for user-visible behavior changes using the real rendered surface;
4. exercise the actual interaction path: navigation, form action, keyboard/mouse interaction, state transition, or route;
5. inspect relevant browser console errors and failed/unexpected network requests;
6. verify applicable loading, empty, error, permission/auth and retry states;
7. verify consumer/API client contract when request/response shape or error handling changed;
8. verify responsive/visual/accessibility semantics when the task makes such claims;
9. run affected frontend baseline/regression checks frozen by the task.

## Receipt rules

- A screenshot proves a visual state, not that the interaction flow works.
- A component/unit test proves the tested component/logic, not the full browser flow.
- A successful HTTP response alone does not prove the UI interpreted/rendered it correctly.
- Prefer user-facing roles/text/contracts over fragile implementation selectors in browser tests.
- When browser behavior changed, report the browser/runtime/environment used.

## Frontend blind spots

- hidden console/runtime error while UI appears correct;
- stale service worker/cache/build serving old code;
- happy path only; error/loading/empty/permission state omitted;
- mocked API differs from real client/provider contract;
- route/feature flag/auth state makes the changed code unreachable;
- optimistic UI looks successful while backend mutation failed;
- hydration/SSR/client-only mismatch where applicable;
- visual claim checked at one viewport/theme only when broader claim was made;
- accessibility/keyboard behavior broken by interaction change;
- browser test asserts DOM implementation detail rather than user-visible behavior.

## Preferred evidence for a user-flow claim

```text
identified frontend build/ref
+ browser/runtime identity
+ exact user actions
+ observed rendered/result state
+ relevant console/network status
+ artifact ref (trace/screenshot/video only when useful)
```

Playwright’s own best practices recommend testing user-visible behavior rather than implementation details and using resilient user-facing locators.
