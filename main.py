#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun entry v2.

A Python program that writes ONE one-line joke about working beside
AI coding agents to /output/entry.txt.

Stdlib only, no network, no fonts, no third-party imports: the grade
run happens in a bare Python 3.13 image (news-image-20261121 v1 was
rejected exit 1 for importing Pillow), so this program must run with
`python3 -P -s` in a clean interpreter.

v2 joke (78 characters, 1 line): the agent "fixes" a race condition by
adding a comment instead of changing any code — a concrete, absurd
punchline the reviewer instantly recognises from real diffs.
"""

import os
from pathlib import Path

JOKE = "My agent fixed the race condition with a comment: 'This should be fine now'."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    # Atomic write: write to a temp file in the same directory, then
    # rename over entry.txt, so a killed/interrupted run can never leave
    # a half-written entry behind for the grader to read.
    tmp_path = output_path.with_suffix(".tmp")
    tmp_path.write_text(JOKE + "\n", encoding="utf-8")
    os.replace(tmp_path, output_path)
    # Read back and verify: the entry must be 1-280 Unicode code points
    # of non-whitespace text, or the run fails loudly instead of
    # silently producing an invalid file.
    written = output_path.read_text(encoding="utf-8")
    if written != JOKE + "\n":
        raise SystemExit("FAIL: entry.txt content does not match the joke exactly")
    if not 1 <= len(written) <= 280:
        raise SystemExit(
            f"FAIL: entry.txt is {len(written)} characters, outside 1-280"
        )
    if not written.strip():
        raise SystemExit("FAIL: entry.txt must not be only whitespace")
    if written.count("\n") != 1:
        raise SystemExit("FAIL: entry.txt must be exactly one line")


if __name__ == "__main__":
    main()
