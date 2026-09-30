#!/usr/bin/env python3
"""Calculate a Gremlin Score from scenario counts."""

from __future__ import annotations

import argparse


def calculate_score(passed: int, failed: int) -> float | None:
    if passed < 0 or failed < 0:
        raise ValueError("counts must be non-negative")
    total = passed + failed
    if total == 0:
        return None
    return passed / total * 100


def main() -> int:
    parser = argparse.ArgumentParser(description="Calculate Gremlin Score")
    parser.add_argument("--passed", type=int, required=True)
    parser.add_argument("--failed", type=int, required=True)
    parser.add_argument("--blocked", type=int, default=0)
    args = parser.parse_args()

    if args.blocked < 0:
        parser.error("--blocked must be non-negative")

    try:
        score = calculate_score(args.passed, args.failed)
    except ValueError as exc:
        parser.error(str(exc))

    if score is None:
        print("Gremlin Score: N/A")
    else:
        print(f"Gremlin Score: {score:.0f}/100")

    print(f"Passed: {args.passed}")
    print(f"Failed: {args.failed}")
    print(f"Blocked or inconclusive: {args.blocked}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
