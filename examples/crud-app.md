# Example: Stateful CRUD

Target flow: edit a customer record.

Invariant: a stale editor cannot overwrite a newer value without the product's defined conflict policy.

## Baseline

1. Open customer `Acme Test`.
2. Change the phone field.
3. Save.
4. Confirm the detail page shows the new value.

## Gremlin scenario

1. Use a fresh fixture customer, separate from the baseline. Open it in Tab A and Tab B and confirm both loaded the same initial version or values.
2. In Tab A, change the phone field and save.
3. In Tab B, change the phone field to another value and save.
4. Wait for both saves and relevant background processing to complete, then reload both tabs and inspect the final stored value.
5. Reproduce from equivalent fresh state and restore test-created fixture state even after failure; report any cleanup failure.

## Evidence to capture

- Request payloads and response status
- Version or `updated_at` values when exposed
- Final stored value
- Conflict UI, if present
- Evidence of both editors' starting state and save completion

## Result examples

A product with optimistic locking can reject Tab B and ask the user to reload.

A product with documented last-write behavior can accept Tab B. Record that policy in the test so a later change does not create a false positive.
