---
name: gremlin-user
description: Test web application flows for defects caused by duplicate actions, interrupted requests, stale tabs, session expiry, odd input, and concurrent edits. Use for targeted misuse testing, reproducing these edge cases, or adding regression coverage for these failure modes.
license: MIT
---

# Gremlin User

Test the app through user behavior that breaks happy-path assumptions.

## Goal

Find defects caused by impatience, interruption, stale state, duplicate actions, odd input, and competing sessions. Confirm each defect before reporting it.

## Safety boundary

Read `references/safety.md` before any test that can mutate data, send messages, charge money, delete records, or call external services.

Use local, preview, staging, or dedicated test environments for mutation. Use test accounts and test data. Stop before an action that can create a real external side effect unless the user has authorized that action and the environment provides a safe test path.

## Workflow

1. **Map the flow.** Identify the user goal, entry point, state changes, external side effects, and success signal.
2. **Check the baseline.** Run the happy path. Record and verify any baseline failure; pause only scenarios that depend on it. Continue requested reproduction and independent scenarios.
3. **Choose Gremlins.** Read `references/scenario-selection.md` and `references/gremlin-catalog.md`. Pick scenarios that match the flow's state and risks. Default to Mild unless the user selects Spicy or Unhinged; intensity does not expand permissions.
4. **Apply the condition.** Use independent fixtures or restore equivalent starting state for the baseline, each scenario, and each reproduction. Keep the path stable while the selected Gremlin changes it, and verify the intended condition actually occurred.
5. **Capture evidence.** Record steps, screenshots, console output, network traces, server logs, and affected records when the tools expose them.
6. **Confirm the defect.** Follow `references/verification.md`. Reproduce the result and separate product defects from automation noise.
7. **Classify impact.** Use `references/severity.md`.
8. **Add regression coverage when in scope.** Follow `assets/regression-test-template.md` and the project's test conventions. Report test execution results and identify tests that still fail because the defect is unfixed; use the project's expected-failure convention when available.
9. **Restore and report.** Restore test-created network interception, session settings, and fixture state, including on failure. Use `assets/report-template.md`; deliver the requested report, plan, or tests without expanding scope.

## Testing rules

- Prefer plausible misuse over random clicking.
- Tie each scenario to a concrete failure hypothesis.
- Keep destructive actions inside test data.
- Do not hide a product defect behind retries or catch-all error handling.
- Do not change production code unless the user asks for a fix.
- Do not label a result a bug until you can state the expected behavior and reproduce the mismatch.
- Preserve the project's test conventions when you add coverage.

## Browser access

If browser automation is available, execute the scenarios and collect evidence. Match each condition to the tool's capability map in `references/gremlin-catalog.md`. When a click-only tool cannot produce a condition such as a dropped response or an expired session, execute the scenario with a scripted browser session instead of skipping it or reporting it as run.

If browser automation is unavailable, produce a Gremlin test plan from the code and identify the exact flows, selectors or routes, state transitions, and assertions a browser test should cover. Do not claim that unexecuted scenarios passed or failed.

## Gremlin Score

Calculate the score from executed scenario outcomes:

`score = passed / (passed + failed) * 100`

Count a scenario as passed only when the intended condition occurred and the app preserved the expected invariant after relevant processing completed. Count a scenario as failed when a confirmed defect breaks that invariant. Exclude blocked and inconclusive scenarios from the denominator. Count each distinct scenario once; reproduction attempts do not add outcomes. Report passed, failed, blocked, and inconclusive counts before the score. If passed + failed is zero, report N/A.

Treat the score as a summary of the tested scenarios, not a measure of overall product quality.

## Reference map

- `references/gremlin-catalog.md`: scenario library
- `references/scenario-selection.md`: scenario selection rules
- `references/verification.md`: defect confirmation
- `references/severity.md`: impact levels
- `references/safety.md`: side-effect limits
- `assets/report-template.md`: final report format
- `assets/regression-test-template.md`: test-writing checklist
- `examples/crud-app.md`: stateful CRUD example
- `examples/checkout.md`: duplicate-action and recovery example
