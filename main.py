"""Funniest toaster error message entry for the make.fun bounty.

This program writes a single funny error message — the line a kitchen
toaster would show its owner — to the entry output file.
"""

import os

ENTRY_LINE = "ERROR: The bread has unionized. Toasting is suspended until further notice."


def main():
    """Write the entry line to the output file."""
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_LINE)
    # Validate the output: read it back and check it is exactly one
    # UTF-8 line of 1 to 120 characters matching the entry line.
    with open(entry_path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != ENTRY_LINE or not 1 <= len(written) <= 120 or "\n" in written:
        raise SystemExit("error: output validation failed")
    print(f"Wrote entry ({len(ENTRY_LINE)} characters) to {entry_path}")


if __name__ == "__main__":
    main()
