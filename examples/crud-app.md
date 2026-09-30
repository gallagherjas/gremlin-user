# Example: Stateful CRUD

Target flow: edit a customer record.

Invariant: a stale editor cannot overwrite a newer value without the product's defined conflict policy.

## Baseline

1. Open customer `Acme Test`.
2. Change the phone field.
3. Save.
4. Confirm the detail page shows the new value.

## Gremlin scenario

1. Open the same customer in Tab A and Tab B.
2. In Tab A, change the phone field and save.
3. In Tab B, change the phone field to another value and save.
4. Reload both tabs.

## Evidence to capture

- Request payloads and response status
- Version or `updated_at` values when exposed
- Final stored value
- Conflict UI, if present

## Result examples

A product with optimistic locking can reject Tab B and ask the user to reload.

A product with documented last-write behavior can accept Tab B. Record that policy in the test so a later change does not create a false positive.
