"""make.fun entry: One-Line Roast: The Gadget You Use Every Day.

Writes one original line to /output/entry.txt: a roast of a gadget used
every day. Stdlib-only (os, sys); no network; deterministic.

Design (from the published judge brief, criteria in order):
1. Roasts a daily gadget in one line: "My Kindle" -- named up front.
2. Actually funny: the joke lands on a first read -- a library of two
   thousand books that only stocks my regrets. The sting is a self-own:
   the gadget is not broken, my taste is.
3. Fresh: Kindle appears in 0 of the 1,455 visible entry titles (cek
   24 Nov 04:3x WIB, file mentah kompetisi); "library" 0, and no field
   line pairs an e-reader with a regrets metaphor. The saturated
   genres -- phone battery at 4pm, laptop fan as jet engine, smartwatch
   standing ovations, speaker mishearing, printer demands, washing
   machine victory songs -- are all avoided.
4. Neatly worded: 130 characters, one line, one comparison, concrete
   numbers (two thousand / same three / 2019) doing the work; nothing
   to cut.
5. Specific gripe: the Kindle home screen keeps surfacing the same
   three old purchases instead of the two thousand books on the device
   -- a concrete behaviour, not a generic complaint.
"""

import os
import sys

TEXT = "My Kindle holds two thousand books and still shows me the same three I bought in 2019, like a library that only stocks my regrets."

def main() -> int:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
    # counted as Unicode code points, and not only white space.
    if not (1 <= len(TEXT) <= 200):
        print(f"entry length {len(TEXT)} outside 1-200", file=sys.stderr)
        return 1
    if not TEXT.strip():
        print("entry is only white space", file=sys.stderr)
        return 1
    if "\n" in TEXT.strip():
        print("entry is not one line", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
