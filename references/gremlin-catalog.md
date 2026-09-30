# Gremlin Catalog

Choose Gremlins that match the flow. A good scenario targets one invariant and changes one condition.

## Click Gremlin

Targets duplicate actions and weak pending-state controls.

Scenarios:

- Double-click a submit action.
- Press Enter and click submit for the same form.
- Click the primary action again while its request is in flight.
- Trigger two conflicting actions with little delay, such as Save and Delete.
- Reopen a dialog and submit the same operation again after a slow response.

Check:

- One user intent creates one durable mutation.
- Buttons reflect pending state.
- Server-side idempotency protects irreversible or costly operations.

## Form Gremlin

Targets validation, normalization, length limits, and state drift.

Scenarios:

- Submit empty input and whitespace-only input.
- Paste a value that exceeds the expected length.
- Use Unicode, emoji, line breaks, and mixed scripts.
- Enter zero, negative, high, low, and high-precision numeric values where the domain permits numbers.
- Change a validated field before submit without blurring it.
- Remove a required value after another field triggers validation.
- Paste content instead of typing it.

Check:

- Client and server rules agree.
- Invalid data does not create partial records.
- Error messages point to the field and preserve entered data when safe.

## Navigation Gremlin

Targets stale UI state and interrupted transitions.

Scenarios:

- Refresh during save.
- Leave the page during save, then return.
- Use Back and Forward after a mutation.
- Open a stateful page in a second tab.
- Revisit a stale deep link after the underlying record changes.
- Close and reopen a modal around a pending request.

Check:

- Navigation does not duplicate mutations.
- Stale pages detect changed or missing records.
- Unsaved input has a defined recovery path.

## Network Gremlin

Targets retries, timeouts, offline recovery, and uncertain server state.

Scenarios:

- Drop the network after submit but before the response reaches the browser.
- Restore the network after a timeout.
- Delay a response past the UI's normal loading window.
- Return a controlled 4xx or 5xx response from a test stub.
- Return malformed or incomplete test data from a stub.
- Retry an action after the browser reports failure while the server may have committed it.

Check:

- The UI distinguishes failure from unknown outcome.
- A retry cannot duplicate an operation.
- Recovery preserves enough context for the user to continue.

## Session Gremlin

Targets auth expiry, permission changes, and cross-tab session state.

Scenarios:

- Expire the session before submit.
- Expire the session while a form contains unsaved work.
- Log out in another tab.
- Change the test user's role in another session, then retry a privileged action.
- Return to a stale tab after login state changes.

Check:

- Unauthorized mutations fail on the server.
- Reauthentication has a defined path.
- The app does not lose user input without warning when recovery is possible.

## Concurrency Gremlin

Targets lost updates, stale writes, duplicate work, and cross-user races.

Scenarios:

- Open the same record in two tabs, edit both, save A, then save B.
- Let user A delete a test record while user B edits it.
- Let two users claim the same limited resource in the test environment.
- Submit the same operation from two sessions with the same business intent.
- Update a parent record while another session changes a dependent record.

Check:

- The app detects stale writes or defines last-write behavior.
- The server protects unique and limited resources.
- Conflict messages give the user a recovery path.

## Data Gremlin

Targets boundary values and assumptions hidden in types or schemas.

Scenarios:

- Use `0`, `-1`, high values, and high-precision decimals where valid input is numeric.
- Use dates at day, month, year, and timezone boundaries.
- Use duplicate identifiers in import or batch flows.
- Use long filenames and unusual file extensions in upload tests with safe fixture files.
- Use strings with leading and trailing spaces.
- Use records that reference deleted or archived test entities.

Check:

- Storage and display preserve valid precision.
- Boundary dates keep their intended day and timezone meaning.
- Imports reject or report bad rows without corrupting good rows.
