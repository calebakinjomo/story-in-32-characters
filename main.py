#!/usr/bin/env python3
"""Write one Wi-Fi network name to /output/entry.txt.

The name is a single joke that implies a whole story: he proposed,
and her answer was to change the Wi-Fi password instead of saying yes.
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


if __name__ == "__main__":
    main()
