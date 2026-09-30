# Example: Checkout Retry

Use a test gateway or payment sandbox.

Invariant: one purchase intent creates one successful test charge and one order.

## Baseline

1. Build a cart with fixture products.
2. Enter test payment details.
3. Submit the order.
4. Confirm one order and one test charge.

## Gremlin scenario

1. Use a fresh fixture cart, separate from the baseline, and record its purchase intent.
2. Submit the order through a test mechanism that lets the server commit while withholding the success response from the browser.
3. Confirm the first order and test charge committed, and the client did not receive success. If this cannot be verified, mark the attempt inconclusive; if the tool cannot produce it, mark it blocked.
4. Restore the connection and retry the same purchase intent from the state the UI presents.
5. Wait for relevant requests and gateway processing to complete, then count final orders and successful test charges for that intent.
6. Reproduce from equivalent fresh state. Restore test-created interception and fixture state even after failure; report any cleanup failure.

## Evidence to capture

- Client request IDs
- Idempotency key, if the system uses one
- Gateway test transaction IDs
- Created order IDs
- UI copy shown after the uncertain outcome
- Evidence of the first commit, withheld response, and processing completion

## Defect condition

Report a defect if the same purchase intent creates duplicate test charges or duplicate orders, or if the UI tells the user that nothing happened after the server committed the order.
