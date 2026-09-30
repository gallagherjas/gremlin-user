# Contributing

Contribute a Gremlin when it captures plausible user behavior and tests a distinct failure mode.

## Scenario requirements

Include:

- The invariant under test
- Preconditions and fixture state
- User actions
- Evidence needed to confirm failure
- Safe environment constraints

Keep the scenario focused. Split unrelated failure modes into separate contributions.

## Good contributions

Good scenarios come from production bugs, support incidents, QA findings, or repeatable edge cases. Remove customer data and secrets before sharing an example.

## Out of scope

Do not add scenarios built around denial-of-service behavior, credential attacks, destructive production actions, or unauthorized access.

## Repository layout

```text
gremlin-user/
├── SKILL.md
├── references/
│   ├── gremlin-catalog.md
│   ├── scenario-selection.md
│   ├── verification.md
│   ├── severity.md
│   └── safety.md
├── assets/
│   ├── report-template.md
│   └── regression-test-template.md
├── examples/
│   ├── crud-app.md
│   └── checkout.md
├── scripts/
│   └── gremlin_score.py
└── tests/
    └── test_gremlin_score.py
```

## Pull requests

Update `references/gremlin-catalog.md` when you add a new behavior class. Add an example when the scenario needs more context than the catalog entry can hold.

Run the score helper tests before opening a pull request:

```bash
python -m unittest discover -s tests -q
```
