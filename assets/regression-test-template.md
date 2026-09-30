# Regression Test Checklist

Use the project's existing test conventions.

## Browser regression test

- Use an independent fixture or restore equivalent starting state for each attempt, separate from the baseline.
- Reproduce the user action that triggered the defect.
- Verify the intended timing, network, session, or concurrency condition actually occurred.
- Assert the user-visible result.
- Wait for relevant requests and background processing to complete using the project's existing completion signal, then assert the durable state for this attempt's business intent. A transient count is not a final-state assertion.
- Avoid sleeps when a state-based wait exists.
- Keep one invariant per test when practical.
- Name the test after the behavior, not the implementation.
- Restore test-created fixture state, interception, and session settings even after failure.
- Report execution results; identify failures caused by an unfixed defect and use the project's expected-failure convention when available.

## Duplicate-action example shape

```text
Start with a fresh cart and a distinct purchase intent.
Attempt duplicate submission and record which requests actually occur.
Check the success UI or the pending-state protection.
Wait for all relevant requests and background work to complete.
Assert exactly one durable order for this purchase intent.
Clean up only this test's state, even if an assertion fails.
```

Adapt selectors, fixtures, helpers, and assertions to the project. Do not introduce a new test stack when the repository already has one that can cover the case.

If the intended condition or final state cannot be verified, record the evidence gap instead of claiming the scenario passed.
