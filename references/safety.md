# Safety Boundary

Stress application behavior inside an authorized test boundary.

## Default boundary

Use local, preview, staging, sandbox, or dedicated test environments for mutation.

Use test accounts, fixture data, test payment methods, and stubbed integrations when the project provides them.

## Stop before these actions without an authorized test path

- Real payment or financial transfer
- Real email, SMS, push, or webhook spam
- Deletion of non-test records
- Account lockout for real users
- Permission changes for real users
- Bulk mutation outside fixture data
- Calls that can affect a real vendor, customer, shipment, booking, or inventory position
- Infrastructure stress, denial-of-service behavior, or load generation

## Production access

If the only reachable environment is production, use read-only inspection and produce an executable test plan. Do not mutate production state unless the user has authorized a specific safe action and the system exposes a test mechanism for it.

## Credentials and secrets

Do not print secrets into reports. Redact tokens, cookies, API keys, passwords, personal data, and payment details from captured evidence.
