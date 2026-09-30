# Example: Checkout Retry

Use a test gateway or payment sandbox.

Invariant: one purchase intent creates one successful test charge and one order.

## Baseline

1. Build a cart with fixture products.
2. Enter test payment details.
3. Submit the order.
4. Confirm one order and one test charge.

## Gremlin scenario

1. Submit the order.
2. Interrupt the browser connection after the request leaves the client but before the success response arrives.
3. Restore the connection.
4. Retry the purchase from the state the UI presents.

## Evidence to capture

- Client request IDs
- Idempotency key, if the system uses one
- Gateway test transaction IDs
- Created order IDs
- UI copy shown after the uncertain outcome

## Defect condition

Report a defect if the same purchase intent creates duplicate test charges or duplicate orders, or if the UI tells the user that nothing happened after the server committed the order.
