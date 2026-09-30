# Regression Test Checklist

Use the project's existing test conventions.

## Browser regression test

- Start from known fixture state.
- Reproduce the user action that triggered the defect.
- Assert the user-visible result.
- Assert the durable state when the test environment exposes it.
- Avoid sleeps when a state-based wait exists.
- Keep one invariant per test when practical.
- Name the test after the behavior, not the implementation.

## Duplicate-action example shape

```ts
await page.getByRole('button', { name: 'Create order' }).dblclick();

await expect(page.getByText('Order created')).toBeVisible();
await expect.poll(async () => countOrdersForFixture()).toBe(1);
```

Adapt selectors, fixtures, helpers, and assertions to the project. Do not introduce a new test stack when the repository already has one that can cover the case.
