#!/usr/bin/env python3
"""One Star, Five Stars for the Food — make.fun entry.

Writes a single-sentence alien tourist's one-star review of Earth,
with a real compliment about the food, to /output/entry.txt.
"""
import os

# The review is assembled from fragments so each clause earns its place:
# the rating, the alien's bafflement at two human habits, and the turn
# where the food almost rescues the planet's score.
RATING = "One star for Earth: "
COMPLAINT = ("the locals pay for water that falls from the sky "
             "and worship glowing rectangles, ")
TURN = ("yet the tacos alone nearly earned this planet "
        "a second star.")

MAX_CHARS = 200


def assemble():
    return RATING + COMPLAINT + TURN


def validate(text):
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if len(text) != len(text.strip()):
        raise ValueError("entry must not have leading/trailing whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the "
                         f"{MAX_CHARS}-char limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    entry = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
