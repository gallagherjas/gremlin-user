---
name: gremlin-user
description: Gremlin-style testing of web application flows for bugs caused by duplicate actions, interrupted requests, stale tabs, session expiry, odd input, and concurrent edits. Use when stress-testing UI behavior, checking stateful CRUD or checkout flows, reproducing edge cases, or adding regression coverage after a bug.
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
2. **Run the happy path.** Confirm the intended flow works before adding stress. Record any baseline failure and stop testing that flow until the baseline works.
3. **Choose Gremlins.** Read `references/scenario-selection.md` and `references/gremlin-catalog.md`. Pick scenarios that match the flow's state and risks, and apply the requested intensity mode: Mild, Spicy, or Unhinged.
4. **Change one condition.** Keep the path stable while one Gremlin changes timing, input, navigation, network, session, or concurrency.
5. **Capture evidence.** Record steps, screenshots, console output, network traces, server logs, and affected records when the tools expose them.
6. **Confirm the defect.** Follow `references/verification.md`. Reproduce the result and separate product defects from automation noise.
7. **Classify impact.** Use `references/severity.md`.
8. **Add regression coverage.** Use the project's test stack. Prefer Playwright for browser behavior when the project already uses it or can run it without changing product code.
9. **Report.** Use `assets/report-template.md`. Keep each report reproducible and specific.

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

Count a scenario as passed when the app preserves the expected invariant. Count a scenario as failed when a confirmed defect breaks that invariant. Exclude blocked and inconclusive scenarios from the denominator. Report the counts with the score.

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
