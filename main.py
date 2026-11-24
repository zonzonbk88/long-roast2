#!/usr/bin/env python3
"""The Long Roast: roast of Muse Spark, by Muse Spark.

Writes one line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt
for local testing). Standard library only, deterministic, no network.
"""

import os

LINE = (
    "Muse Spark: named after ignition, yet it needed a draft, "
    "a test, a revision and a re-test just to light one line \u2014 "
    "and this is the line."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
