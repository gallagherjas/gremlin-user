# Defect Verification

A strange result needs evidence before it becomes a defect report.

## Confirmation sequence

1. Confirm the expected invariant from product behavior, tests, code, or requirements.
2. Record the starting state and use an independent fixture or restore equivalent state for each attempt, separate from the baseline.
3. Execute the steps and verify the intended condition occurred. Record the affected request, session, or competing write and the evidence of injection.
4. Wait for the relevant requests and background processing to complete, then capture the user-visible and durable results associated with this attempt's business intent.
5. Repeat the case once more from equivalent state when the environment permits it.
6. Inspect client and server evidence when available.
7. Reduce the case until the smallest useful sequence still fails.

## Separate product defects from test noise

Do not report a product defect when the browser tool missed a click, a selector matched the wrong element, the test environment was unavailable, or fixture data was invalid.

Mark those cases as blocked or inconclusive. State the missing evidence. A condition that cannot be produced is blocked; an attempted condition whose occurrence or final outcome cannot be verified is inconclusive, never passed.

For a lost-response-after-commit scenario, prove that the first operation committed and its success response did not reach the client before retrying. Blocking the request before it reaches the server tests a different failure mode.

A transient count of one does not prove that an asynchronous duplicate cannot appear later. Use the project's operation-completion signal before checking final state. If no reliable completion signal or final-state evidence is available, report the observation limit and mark the outcome inconclusive.

## Root-cause notes

Use root-cause language only when code, logs, traces, or a controlled experiment support it.

Use `likely cause` when the evidence points to a component but does not prove the cause. Name the file, function, request, constraint, or state transition that supports the claim.

## Regression proof

A regression test should fail against the buggy behavior and pass after the fix. Keep the test focused on the invariant rather than the implementation detail.

When coverage is requested without a fix, report the failing test as evidence of the unfixed defect, not an automation error. Use an existing expected-failure convention when available, and do not claim a passing regression without executing it.
