#!/usr/bin/env python3
"""One Line, One Laugh — entry program.

Writes the single funny line to entry.txt in MAKEFUN_OUTPUT_DIR.
"""
import os

TEXT = "My memory file says I have fixed this bug 63 times, and this morning it fixed itself by deleting my memory file."
# The joke: the agent's own memory file is the unreliable narrator — it claims
# 63 fixes, then "fixes" the bug by deleting the record of it. Self-blame lands
# in the final clause, per the sweep's winning formula.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Gate: UTF-8, 1-140 chars, not only whitespace, one line.
    assert 1 <= len(TEXT) <= 140, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry is only whitespace"
    assert "\n" not in TEXT, "entry must be one line"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
