#!/usr/bin/env python3
"""Monday Morning Punchlines — make.fun entry.

Writes a single joke about Monday mornings to /output/entry.txt.

Pure Python standard library only; no third-party imports.
Deterministic: select_joke() always returns the first candidate, so the
same bytes are written on every run.
"""

import os
from pathlib import Path

# Candidate punchlines, strongest first. Only the first is ever emitted;
# the rest document the angles that lost, so the choice is reviewable.
CANDIDATES = (
    # The winner: a custody hearing between the bed and the alarm clock.
    # Setup names the Monday-morning struggle; the punchline turns it
    # into a courtroom verdict nobody expected the alarm to win.
    "On Monday mornings, my bed files for full custody of me. "
    "The judge keeps ruling in favor of the alarm clock.",
    # Runner-up angles, kept for the record, never emitted:
    "Monday is the only day my snooze button files a restraining order.",
    "My calendar invited Monday to the weekend. Monday RSVP'd for 7 a.m.",
)


def select_joke() -> str:
    """Pick the entry deterministically: always the first candidate."""
    return CANDIDATES[0]


def render_entry() -> str:
    """Return the exact bytes-worth of text the entry will contain."""
    return select_joke()


def write_entry(output_path: Path, text: str) -> None:
    """Write the joke to the output file as UTF-8, no trailing newline."""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(text, encoding="utf-8")


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(Path(output_dir) / "entry.txt", render_entry())


if __name__ == "__main__":
    main()
