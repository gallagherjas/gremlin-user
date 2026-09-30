# 👹 Gremlin User

[![CI](https://github.com/gallagherjas/gremlin-user/actions/workflows/ci.yml/badge.svg)](https://github.com/gallagherjas/gremlin-user/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[English](README.md) | [简体中文](README.zh-CN.md)

A coding-agent skill for testing web apps through plausible user misuse, interruption, stale state, and duplicate actions.

Normal UI tests follow the intended path. Real users don't. Gremlin User adds the behavior users bring to real software: repeated clicks, stale tabs, expired sessions, odd input, interrupted requests, and competing edits.

The agent confirms each failure, collects evidence, and writes regression tests for confirmed defects.

## Example

A checkout test can pass with one click and a clean network. Gremlin User runs the same flow with a lost response and a retry:

```text
Submit order
Connection drops after request leaves the browser
Server may commit the order
Connection returns
User retries
```

A useful result looks like this:

```text
[HIGH] Retry after unknown outcome creates a duplicate order

Invariant: one purchase intent creates one order
Observed: two orders share the same cart and customer
Evidence: two POST /orders requests, two created order IDs
Likely cause: retry path has no idempotency guard
Regression: tests/checkout/retry-after-timeout.spec.ts
```

Full walkthroughs: [`examples/checkout.md`](examples/checkout.md) and [`examples/crud-app.md`](examples/crud-app.md).

## How it works

Gremlin User does not click at random. Each Gremlin is a named failure hypothesis selected from the flow's state changes.

1. Map the flow and write the invariants it must preserve — one purchase intent creates one order; a stale editor cannot silently overwrite a newer version.
2. Run the happy path, then change one condition at a time: timing, input, navigation, network, session, or concurrency.
3. Reproduce every suspected defect and separate product bugs from automation noise before reporting.
4. Add regression tests for confirmed defects, in the project's existing test stack.

## Gremlins

| Gremlin | Tests |
| --- | --- |
| Click | Duplicate actions and pending states |
| Form | Validation, normalization, and boundary input |
| Navigation | Refresh, Back/Forward, stale pages, interrupted transitions |
| Network | Timeouts, lost responses, retries, and recovery |
| Session | Expiry, logout, and permission changes |
| Concurrency | Competing tabs, users, and writes |
| Data | Numeric, date, identifier, import, and text boundaries |

Full scenario library: [`references/gremlin-catalog.md`](references/gremlin-catalog.md).

## Modes

| Mode | What it adds |
| --- | --- |
| Mild | Common edge cases with low mutation risk |
| Spicy | Network interruption, session expiry, competing tabs, and controlled server errors |
| Unhinged | Two realistic conditions combined, after each condition passes alone; keeps a clear failure hypothesis inside the test boundary |

## Installation

Works with any agent that supports the open Agent Skills `SKILL.md` format. Browser automation and Python are optional.

The repository root is the skill directory: clone it (or download and extract it) as `gremlin-user` into the skills location your agent discovers.

| Client | Location |
| --- | --- |
| Claude Code | `.claude/skills/gremlin-user/` (project) or `~/.claude/skills/gremlin-user/` (global) |
| Codex | `.codex/skills/gremlin-user/` |
| Other clients | Your client's skills directory |

Keep the folder intact with `SKILL.md` at its root. Extra repository files such as `tests/` and CI config are harmless; agents only read `SKILL.md` and the files it references.

## Usage

Ask the agent to test a flow with the skill:

```text
Use gremlin-user on the create-order flow. Run Mild mode.
```

```text
Gremlin-test auth and session expiry in staging. Do not send real email.
```

```text
Run Spicy mode against this checkout flow with the payment sandbox.
```

The agent runs the happy path, selects Gremlins that match the flow, confirms each suspected defect, and writes regression coverage when the project can support it. Without browser automation it produces an executable Gremlin test plan instead of claiming unexecuted results.

## Gremlin Score

Each run is summarized by a score over executed scenarios:

```text
score = passed / (passed + failed) * 100
```

Blocked and inconclusive scenarios stay outside the denominator. Run the helper:

```bash
python scripts/gremlin_score.py --passed 28 --failed 6 --blocked 3
```

```text
Gremlin Score: 82/100
Passed: 28
Failed: 6
Blocked or inconclusive: 3
```

Treat the score as a summary of that run, not a product rating.

## Safety

Run mutation tests with test data in local, preview, staging, sandbox, or dedicated test environments. Keep real payments, messages, non-test data, real user permissions, and infrastructure load outside the run unless an authorized test system provides a safe path for the specific action.

Read [`references/safety.md`](references/safety.md) before testing flows with external side effects.

## Prior art

"Gremlin" here means the imaginary creatures that break machinery when nobody watches, not the chaos-engineering company. This project is not affiliated with Gremlin Inc.

Unleashing misbehaving users on an app has a long history, most notably [gremlins.js](https://github.com/marmelab/gremlins.js), the monkey-testing library. Gremlin User applies the same idea with a coding agent: invariant-driven scenario selection, evidence capture, and regression coverage instead of random fuzzing.

## Contributing

A good Gremlin names the invariant it attacks, the steps, and the evidence needed to confirm the defect. See [CONTRIBUTING.md](CONTRIBUTING.md) for the requirements, the repository layout, and the test command.

## License

[MIT](LICENSE)
