#!/usr/bin/env python3
"""One Line, One Laugh: Roast Your Fridge — entry program.

Deterministic: writes exactly one roast line (one line, <=200 characters)
to /output/entry.txt. No network, no randomness, no input, no dependencies.
The line roasts the entrant's own phone: it overheats the moment the
camera opens, and the punchline lands on the last few words.
"""

ENTRY = "My phone gets hot just opening the camera, like it's embarrassed to be seen with me."


def main():
    import os

    if len(ENTRY) > 200 or not ENTRY.strip():
        raise SystemExit("entry must be 1-200 non-blank characters")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
