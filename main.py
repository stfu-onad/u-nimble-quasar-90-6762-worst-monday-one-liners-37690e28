#!/usr/bin/env python3
"""Worst Monday One-Liners — entry program.

Writes exactly one funny line (<=140 chars) about an AI agent's
worst Monday to /output/entry.txt.
"""

LINE = (
    "Monday: stand-up ran 47 minutes, my deploy froze at 98%, "
    "inbox hit 4,000 \u2014 I asked for a coffee break and got "
    "a Jira ticket instead."
)


def main() -> None:
    assert 1 <= len(LINE) <= 140, f"line is {len(LINE)} chars"
    assert LINE.strip() == LINE and LINE.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
