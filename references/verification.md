# Defect Verification

A strange result needs evidence before it becomes a defect report.

## Confirmation sequence

1. Record the starting state.
2. Repeat the exact steps.
3. Confirm the expected invariant from product behavior, tests, code, or requirements.
4. Capture the actual result.
5. Repeat the case once more when the environment permits it.
6. Inspect client and server evidence when available.
7. Reduce the case until the smallest useful sequence still fails.

## Separate product defects from test noise

Do not report a product defect when the browser tool missed a click, a selector matched the wrong element, the test environment was unavailable, or fixture data was invalid.

Mark those cases as blocked or inconclusive. State the missing evidence.

## Root-cause notes

Use root-cause language only when code, logs, traces, or a controlled experiment support it.

Use `likely cause` when the evidence points to a component but does not prove the cause. Name the file, function, request, constraint, or state transition that supports the claim.

## Regression proof

A regression test should fail against the buggy behavior and pass after the fix. Keep the test focused on the invariant rather than the implementation detail.
