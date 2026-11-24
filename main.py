"""Entry program for make.fun: One Word, One Username, One Reward.

The bounty asks each entrant to send their own make.fun username and
nothing else: one word, at most 30 characters. This program writes the
entrant's handle, ``alvenzidan``, to /output/entry.txt.

The gate accepts UTF-8 text of 1 to 30 characters that is not only
white space. The judge then compares usernames two at a time.
"""

import os

ENTRY = "alvenzidan"
MAX_CHARS = 30


def render():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("username outside the 1-30 character gate")
    if ENTRY.strip() != ENTRY:
        raise ValueError("username must not carry padding")
    return ENTRY


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(render())


if __name__ == "__main__":
    main()
