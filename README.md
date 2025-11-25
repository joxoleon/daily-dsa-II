# DSA-Every-Day

A fully structured, weighted, difficulty-balanced daily practice engine for FAANG-tier interviews, implemented entirely in Python. Inside you’ll find:
- A curated library of fundamental algorithm patterns and implementations.
- A large collection of LeetCode-style problems grouped by topic and difficulty.
- A cycle generation engine that produces a 100-day training plan with deterministic difficulty rotation, weighted category balancing, and starvation-free scheduling.

This system is designed to keep you interview-ready while steadily reinforcing the most important problem-solving techniques.

## Repository Structure

```
.
├── 00_structured
│ ├── fundamentals # Handpicked core patterns with minimal implementations
│ └── leetcode # LeetCode problems grouped by category and difficulty
│
├── 01_daily_cycles # Generated 100-day plan
│ ├── 001_day
│ ├── 002_day
│ ├── ...
│ ├── 100_day
│ ├── daily_cycles_report.txt
│ └── not_included # Problems not scheduled in the 100-day plan
│
├── 02_generator_impl # Cycle generation engine
│ ├── resource_loader.py
│ ├── daily_cycle_generators.py
│ ├── cycle_saver.py
│ └── generate.py
│
├── resources
│ ├── daily_rotation
│ ├── generator_scripts
│ └── inputs
│
├── Makefile
├── requirements.txt
└── README.md
```

## Overview

This is a complete training discipline built around repetition, difficulty control, and category-weighted reinforcement. It combines:
1) Fundamental problem patterns (short, 2–5 minute drills).  
2) Full LeetCode-style interview problems (Easy, Medium, Hard).  
3) A scheduling engine that rotates categories and difficulties intelligently.

The result is a pipeline that re-surfaces what matters most while ensuring broad coverage of the interview landscape.

## Using This Repository

### Step 1: Learn the Fundamentals
Start with `00_structured/fundamentals`. These short, pure-pattern Python problems teach the canonical templates for:
- Two pointers, sliding window, binary search
- Graph BFS/DFS, tree traversals and LCA
- Dynamic programming fundamentals
- Monotonic stacks, heaps, greedy, intervals
- Union-Find, grids, backtracking, linked lists

### Step 2: Generate Your 100-Day Plan
Once you’ve built the base, run the cycle generator to produce 100 daily folders.

Setup:
```bash
make venv
source .venv/bin/activate
pip install -r requirements.txt
```

Generate the cycles:
```bash
python 02_generator_impl/generate.py
```

This creates:
- `01_daily_cycles/NNN_day/` folders with fundamentals and LeetCode problems.
- `daily_report.txt` with a per-day breakdown (names, category, topic, weight, difficulty, link).
- `not_included/` listing unscheduled problems.

Delete `01_daily_cycles` and rerun any time to rebuild with the same or tweaked weights.

## Daily Cycle Structure

Each day contains:
- **Fundamentals**: Balanced by category weight, size, and aging (how long since last seen).
- **LeetCode**: Selected by difficulty rotation (e.g., pure easy, pure medium, easy + hard) defined in `LC_MODES` and `LC_ROTATION`, with no duplicates in the same day.

## How the Cycle Engine Works

- **Category weighting**: Emphasizes high-frequency interview topics (arrays, sliding window, two pointers, binary search, etc.).
- **Progressive aging**: Problems not selected get older faster (`age += 1 + (age // 3)`) to avoid starvation.
- **Difficulty bucketing**: Easy/Medium/Hard buckets use the same weighted, aging-based selection per category.
- **Non-duplicate guarantee**: The same problem never appears twice within a single day.

## Internals

- `resource_loader.py`: Scans fundamentals/leetcode directories, parses metadata headers, builds `FileRecord`s.
- `daily_cycle_generators.py`: Implements the engines (ProblemContainer, CategoryContainer, CycleGenerator, LeetCodeCycleGenerator).
- `cycle_saver.py`: Writes cycles to disk and handles safe filenames.
- `generate.py`: Main entrypoint—loads everything, applies weights and rotations, writes 100 days, report, and not-included sets. Config knobs (weights, rotations, day count) live here.

## Recommended Training Strategy

- **Daily**: Do fundamentals first (fast pattern refresh), then LeetCode for deeper reasoning; flag tough problems to revisit.
- **Weekly**: Re-run weak fundamentals sections; do timed mediums/hards or a mock interview.
- **Monthly**: Rebalance weak categories (graphs, DP, backtracking, etc.); regenerate the plan with updated weights/rotation.

After a single 100-day cycle you’ll have hit essentially all core concepts required for FAANG-style interviews.

## Contributing

Contributions are welcome:
- Add new fundamental templates or LeetCode problems.
- Improve category weights or difficulty rotations.
- Add reporting/visualization or CLI flags in `generate.py`.
- Build a small UI or dashboard over the daily cycles.

Fork, branch, and open a PR.

# License

This project is open source under the MIT License.

---

# Notes

- The virtual environment is ignored by git; every contributor should run `make venv`
- If adding new dependencies, update `requirements.txt`
- You may delete and regenerate `01_daily_cycles` at any time

---

# Final Words

DSA-Every-Day is designed as a strict, structured, repeatable training system. It removes randomness and burnout from interview prep while reinforcing the patterns that matter most. If you follow the fundamentals and daily cycles consistently, you will reach interview-ready performance significantly faster than with unstructured LeetCode grinding.

Good luck, and stay consistent.
