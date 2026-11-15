#!/usr/bin/env python3
"""Write the agency poem to /output/entry.txt.

Deterministic, no network, no randomness, no wall clock.
Run twice and the output bytes must be identical.
"""

from pathlib import Path

POEM = """No one applauds the morning
I choose water over wine,
the letter I do not send,
the shortcut I do not take.

Yet here is the arithmetic
no one taught me to keep:
a life is not one brave hour,
it is a thousand quiet entries,
each signed in the same hand.

I am not waiting to be chosen.
I am the clerk, the witness,
the one who writes the total
and then pays it."""

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8", newline="\n")
    # Self-check: the entry must stay exactly the poem, UTF-8, 1-1000 chars.
    written = out.read_text(encoding="utf-8")
    if written != POEM or not 1 <= len(written) <= 1000:
        raise SystemExit("entry.txt does not match the poem")

if __name__ == "__main__":
    main()
