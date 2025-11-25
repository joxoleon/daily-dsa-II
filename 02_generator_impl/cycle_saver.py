from __future__ import annotations

import re
from pathlib import Path
from typing import Iterable, List, Sequence

from daily_cycle_generators import ProblemContainer


def _sanitize_filename(name: str) -> str:
    """Create a filesystem-friendly filename stem."""
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")
    return safe.lower() or "problem"


def _write_problems(target_dir: Path, problems: Iterable[ProblemContainer]) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    for idx, problem in enumerate(problems, start=1):
        stem = _sanitize_filename(problem.metadata.name)
        filename = f"{stem}.py"

        # Avoid overwriting if two problems sanitize to the same stem.
        counter = 1
        path = target_dir / filename
        while path.exists():
            path = target_dir / f"{stem}_{counter}.py"
            counter += 1

        path.write_text(problem.source_code, encoding="utf-8")


def save_cycles(
    fundamentals_cycles: Sequence[Sequence[ProblemContainer]],
    leetcode_cycles: Sequence[Sequence[ProblemContainer]],
    output_root: Path | str,
) -> None:
    """
    Persist generated cycles to disk in a day-based folder hierarchy:

    <output_root>/
        001_day/
            fundamentals/<problem>.py
            leetcode/<problem>.py
        002_day/
            ...
    """
    root = Path(output_root)
    root.mkdir(parents=True, exist_ok=True)

    num_days = max(len(fundamentals_cycles), len(leetcode_cycles))
    for day_index in range(num_days):
        day_dir = root / f"{day_index + 1:03d}_day"
        day_dir.mkdir(parents=True, exist_ok=True)

        if day_index < len(fundamentals_cycles):
            _write_problems(day_dir / "fundamentals", fundamentals_cycles[day_index])

        if day_index < len(leetcode_cycles):
            _write_problems(day_dir / "leetcode", leetcode_cycles[day_index])
