#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The name is a single joke that implies a whole story: he proposed,
and her answer was to change the Wi-Fi password instead of saying yes.

The entry is checked twice — once before it is written, once after —
so what lands in /output/entry.txt is exactly the name below.
"""

import os

ENTRY = "HeProposed_IChangedTheWiFi"

MAX_LENGTH = 32


def main() -> None:
    """Validate the entry and write it to /output/entry.txt."""
    if not ENTRY or ENTRY.isspace():
        raise ValueError("entry must not be empty")
    if len(ENTRY) > MAX_LENGTH:
        raise ValueError(f"entry is {len(ENTRY)} chars, over the {MAX_LENGTH} limit")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read the file back and confirm it holds exactly the validated entry.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        raise ValueError("read-back mismatch: /output/entry.txt differs from ENTRY")


if __name__ == "__main__":
    main()
