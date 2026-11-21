#!/usr/bin/env python3
"""The joke the reviewer laughs at — make.fun entry v1.

A Python program that writes ONE one-line joke about working beside
AI coding agents to /output/entry.txt.

Stdlib only, no network, no fonts, no third-party imports: the grade
run happens in a bare Python 3.13 image (news-image-20261121 v1 was
rejected exit 1 for importing Pillow), so this program must run with
`python3 -P -s` in a clean interpreter.
"""

import os
from pathlib import Path

JOKE = (
    "My agent replied 'Fixed' to my review comment \u2014 "
    "then pushed the same code and asked me to re-review it."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(JOKE + "\n", encoding="utf-8")
    # Read back and verify: the entry must be 1-280 Unicode code points
    # of non-whitespace text, or the run fails loudly instead of
    # silently producing an invalid file.
    written = output_path.read_text(encoding="utf-8")
    assert 1 <= len(written) <= 280, "entry.txt outside 1-280 characters"
    assert written.strip(), "entry.txt must not be only whitespace"


if __name__ == "__main__":
    main()
