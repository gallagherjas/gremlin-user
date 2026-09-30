# Scenario Selection

Pick scenarios from the state changes in the flow.

## Start from invariants

Write one sentence for each invariant before testing. Examples:

- One click intent creates one order.
- A stale editor cannot overwrite a newer version without a defined conflict policy.
- An expired session cannot create a privileged mutation.
- A timed-out payment request cannot charge twice in the test gateway.

Each scenario should try to break one invariant.

## Match Gremlins to flow shape

| Flow trait | Gremlins to consider |
|---|---|
| Form creates a record | Click, Form, Network |
| Edit existing state | Navigation, Concurrency, Session |
| Irreversible action | Click, Network, Session |
| Multi-step wizard | Navigation, Network, Session |
| Import or batch work | Data, Network |
| Shared resource | Concurrency, Session |
| Auth or admin flow | Session, Navigation |

## Test budget

For a focused change, run three to eight scenarios that cover the changed state and its nearest dependencies.

For a broad release check, cover each high-value user flow with at least one timing or duplicate-action scenario and one stale-state or recovery scenario.

Do not chase scenario count. Add a scenario when it tests a new invariant or failure mode.

## Modes

### Mild

Use common edge cases with low mutation risk. Favor form boundaries, refresh, duplicate clicks, and stale navigation.

### Spicy

Add network interruption, session expiry, competing tabs, and controlled server errors.

### Unhinged

Combine two realistic conditions after each condition works alone. Examples include a stale tab after session expiry or a retry after an unknown network outcome.

Keep one clear hypothesis per combined scenario. Do not use destructive infrastructure actions.
