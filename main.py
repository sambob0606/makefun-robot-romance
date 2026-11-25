#!/usr/bin/env python3
"""Robot Romance entry: write one pickup line to /output/entry.txt.

The line is a single-line joke pickup line aimed at an AI, built on the
autocomplete premise: the machine keeps finishing the speaker's sentences,
so the speaker's sentences keep ending with it.
"""

import os

LINE = "You must be my autocomplete, because every sentence I start ends with you."


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-200
    # characters, not only whitespace, on a single line.
    text = LINE.strip()
    assert text, "entry line must not be blank"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"wrote {path} ({len(text)} chars)")


if __name__ == "__main__":
    main()
