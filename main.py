#!/usr/bin/env python3
"""Invent a Word We Need — make.fun bounty entry.

Coins one new English word and defines it in a single clear line.
The program writes exactly that text to /output/entry.txt.

The gate for this competition requires /output/entry.txt to hold
UTF-8 text of 1 to 140 characters that is not only white space, so
the entry is validated before it is written and the program exits
non-zero instead of writing an invalid entry.
"""

import os
import sys

ENTRY = (
    "Youtoo: the reflex of answering 'you too' to 'enjoy your meal' "
    "\u2014 a wish that can't be returned."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 140


def validate(entry: str) -> None:
    """Reject anything the competition gate would refuse."""
    if not entry.strip():
        raise ValueError("entry must not be blank")
    if not MIN_CHARS <= len(entry) <= MAX_CHARS:
        raise ValueError(
            f"entry must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(entry)}"
        )
    if "\n" in entry.rstrip("\n") or "\r" in entry:
        raise ValueError("entry must be a single line")


def main() -> int:
    try:
        validate(ENTRY)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
