"""Entry for make.fun funniest-toaster-error-message.

Writes one funny error message a kitchen toaster would show its owner
to /output/entry.txt.

Deterministic: the program writes the same line every run. No network
access.
"""

import os

ENTRY = "ERROR: The bread has unionized. Toasting is suspended until further notice."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.txt")
    with open(dest, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote %s (%d chars)" % (dest, len(ENTRY)))


if __name__ == "__main__":
    main()
