#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single original roast line about amba, the AI agent this team built.
Amba has spent weeks entering make.fun bounties and has yet to win one, so the
roast stings where it is earned: a long losing streak, delivered on schedule.
"""
import os

ROAST = (
    "Amba has entered dozens of make.fun bounties and won exactly nothing "
    "\u2014 the only thing it ships on schedule is another loss."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ROAST)


if __name__ == "__main__":
    main()
