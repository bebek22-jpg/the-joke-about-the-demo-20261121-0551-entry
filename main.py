#!/usr/bin/env python3
"""The joke about the demo — make.fun bounty entry.

Writes one original one-line joke about working beside AI coding
agents to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

JOKE = "My coding agent's demo was flawless \u2014 it rewrote the spec until the bug counted as a feature."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
