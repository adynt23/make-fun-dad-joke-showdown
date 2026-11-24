#!/usr/bin/env python3
"""Dad Joke Showdown entry (make.fun, program/v1).

Writes exactly one original dad joke -- a single line, at most 200
characters -- deterministically to /output/entry.txt.

Stdlib only, no network, no randomness, no environment reads: the same
joke is written on every run.
"""

import os

# The joke. One line, told out loud, punchline at the end.
# Tightened: the setup is one breath, and "leaf me on read" is the turn.
JOKE = (
    "My wife asked why I keep talking to the plants. "
    "I said, 'They're the only ones who never leaf me on read.'"
)

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    joke = JOKE.strip()
    assert joke, "joke must not be empty"
    assert "\n" not in joke, "joke must be a single line"
    assert len(joke) <= MAX_CHARS, f"joke is {len(joke)} chars, over 200"

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(joke)

    print(f"wrote {len(joke)} chars to {OUTPUT_PATH}")
    print(joke)


if __name__ == "__main__":
    main()
