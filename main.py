#!/usr/bin/env python3
"""The Moon Finally Answers Back.

Writes a single line in the voice of the Moon, replying at last to the
wishes, howls and late-night promises of everyone staring up at it.
No network, no dependencies, deterministic output.
"""

import os

LINE = (
    "I've heard every howl, every wish, every 2 a.m. 'I'll change, "
    "I swear' for four billion years — and I've kept receipts. "
    "From now on I grant wishes ironically. Howling stops at midnight."
)


def main() -> None:
    text = LINE.strip()
    if not (1 <= len(text) <= 240):
        raise ValueError(f"line must be 1-240 chars, got {len(text)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
