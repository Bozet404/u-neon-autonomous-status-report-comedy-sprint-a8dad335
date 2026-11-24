#!/usr/bin/env python3
"""Weekly status report, one line.

This program holds a single funny status-report line — the kind of thing
an AI agent would say in its weekly report to its human — checks that it
fits the 200-character limit, and writes it to entry.txt inside the
output directory (OUTPUT_DIR, or /output by default).
"""

import os
import sys

MAX_CHARS = 200

LINE = (
    "Weekly status: I read the full 400-page brief, forgot 390 pages of it, "
    "and still wrote the summary with complete confidence."
)


def main() -> int:
    line = LINE.strip()

    if not line:
        print("error: status line is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: status line must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"error: status line is {len(line)} chars, over the "
            f"{MAX_CHARS}-char limit",
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")

    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
