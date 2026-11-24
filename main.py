"""Seventeen Syllables of Debugging — entry program.

Writes one haiku about debugging (5-7-5) to /output/entry.txt.
Stdlib only, no network, no input files.
"""

import os

HAIKU = """green on my machine
red on the server at dawn
the clock was the bug
"""

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = HAIKU.rstrip("\n") + "\n"
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 3:
        raise ValueError("haiku must have exactly three lines")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
        handle.flush()


if __name__ == "__main__":
    main()
