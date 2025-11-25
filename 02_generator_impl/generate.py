from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import List

from cycle_saver import save_cycles
from daily_cycle_generators import (
    CycleGenerator,
    LeetCodeCycleGenerator,
)
from resource_loader import ResourceLoader

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

NUM_DAYS = 100
OUTPUT_ROOT = Path(__file__).resolve().parents[1] / "01_daily_cycles"

# Fundamentals generation knobs
FUNDAMENTALS_PROBLEMS_PER_CATEGORY = 2
FUNDAMENTALS_CATEGORIES_PER_DAY = 2
FUNDAMENTALS_WEIGHT_GROUPS = {
    10: {"arrays", "strings", "binary_search"},
    9: {"dp", "trees"},
    8: {"graphs", "intervals", "greedy", "heaps"},
    7: {"backtracking", "linked_list", "stacks_and_queues"},
    6: {"grids"},
    3: {"union_find"},
}
FUNDAMENTALS_WEIGHTS = {
    category: weight for weight, cats in FUNDAMENTALS_WEIGHT_GROUPS.items() for category in cats
}

# LeetCode generation knobs
LEETCODE_WEIGHT_GROUPS = {
    10: {"arrays", "sliding_window", "two_pointers", "binary_search"},
    9: {"dp", "trees", "graphs"},
    8: {"greedy", "intervals", "hashing", "strings"},
    7: {"heap", "backtracking", "stack", "linked_list"},
    6: {"bit_manipulation", "math"},
    5: {"tries", "design"},
    4: {"extra_20_must_know"},
}
LEETCODE_WEIGHTS = {
    category: weight for weight, cats in LEETCODE_WEIGHT_GROUPS.items() for category in cats
}

# Difficulty distributions for LC days
LC_MODES = {
    "pure_easy": ["easy", "easy", "easy"],
    "pure_medium": ["medium", "medium"],
    "easy_and_hard": ["easy", "hard"],
    "balanced": ["easy", "medium"],
    "pure_hard": ["hard"],
}

# Rotation of LC mode per day
LC_ROTATION = ["balanced", "pure_hard", "balanced", "pure_easy", "pure_medium", "balanced", "easy_and_hard", "balanced"]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def flatten(cycles: List[List]) -> List:
    return [item for cycle in cycles for item in cycle]


def summarize_leetcode(cycles: List[List]) -> str:
    flat = flatten(cycles)
    total = len(flat)
    unique = len({p.metadata.name for p in flat})
    difficulties = Counter(
        (p.metadata.difficulty or "unknown").lower() for p in flat
    )
    lines = [
        f"LeetCode problems -> total: {total}, unique: {unique}",
        f"  difficulties: {dict(sorted(difficulties.items()))}",
    ]
    return "\n".join(lines)


def summarize_fundamentals(cycles: List[List]) -> str:
    flat = flatten(cycles)
    total = len(flat)
    unique = len({p.metadata.name for p in flat})
    return f"Fundamentals problems -> total: {total}, unique: {unique}"

def compute_not_included(all_records, cycles: List[List]) -> List:
    """Return records that never appeared in any cycle."""
    used_names = {p.metadata.name for p in flatten(cycles)}
    return [r for r in all_records if r.metadata.name not in used_names]

def _sanitize_filename(name: str) -> str:
    import re
    safe = re.sub(r"[^A-Za-z0-9._-]+", "_", name).strip("_")
    return safe.lower() or "problem"

def write_not_included(root: Path, fundamentals_missing, leetcode_missing) -> None:
    ni_root = root / "not_included"
    ni_root.mkdir(parents=True, exist_ok=True)

    def _write(target: Path, records) -> None:
        target.mkdir(parents=True, exist_ok=True)
        for rec in records:
            stem = _sanitize_filename(rec.metadata.name)
            filename = f"{stem}.py"
            path = target / filename
            counter = 1
            while path.exists():
                path = target / f"{stem}_{counter}.py"
                counter += 1
            path.write_text(rec.content, encoding="utf-8")

    _write(ni_root / "fundamentals", fundamentals_missing)
    _write(ni_root / "leetcode", leetcode_missing)


# ---------------------------------------------------------------------------
# Generation entrypoint
# ---------------------------------------------------------------------------

def main() -> None:
    loader = ResourceLoader()

    # Fundamentals cycles
    fundamentals_gen = CycleGenerator(loader.fundamentals, FUNDAMENTALS_WEIGHTS)
    fundamentals_cycles = fundamentals_gen.generate_cycles(
        num_cycles=NUM_DAYS,
        num_problems_per_category=FUNDAMENTALS_PROBLEMS_PER_CATEGORY,
        num_categories=FUNDAMENTALS_CATEGORIES_PER_DAY,
    )

    # LeetCode cycles
    lc_gen = LeetCodeCycleGenerator(loader.leetcode, LEETCODE_WEIGHTS)
    leetcode_cycles = lc_gen.generate_cycles(
        num_cycles=NUM_DAYS,
        rotation=LC_ROTATION,
        modes=LC_MODES,
    )

    save_cycles(fundamentals_cycles, leetcode_cycles, OUTPUT_ROOT)

    # Compute and persist not-included problems
    missing_fundamentals = compute_not_included(loader.fundamentals, fundamentals_cycles)
    missing_leetcode = compute_not_included(loader.leetcode, leetcode_cycles)
    write_not_included(OUTPUT_ROOT, missing_fundamentals, missing_leetcode)

    print(f"Wrote {NUM_DAYS} days to: {OUTPUT_ROOT}")
    print(summarize_fundamentals(fundamentals_cycles))
    print(summarize_leetcode(leetcode_cycles))
    print(f"LeetCode coverage vs pool: {len({p.metadata.name for p in flatten(leetcode_cycles)})}/{len(loader.leetcode)} unique")
    print(f"Not included -> fundamentals: {len(missing_fundamentals)}, leetcode: {len(missing_leetcode)}")


if __name__ == "__main__":
    main()
