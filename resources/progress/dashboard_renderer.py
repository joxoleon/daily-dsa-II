import os
from datetime import datetime
from metadata_loader import load_all_problems
from progress_tracker import load_progress, is_solved

DASHBOARD_FILE = "PROGRESS_DASHBOARD.md"

def pct(x, total):
    if total == 0:
        return 0
    return round((x / total) * 100, 1)

def bar(done, total, width=20):
    if total == 0:
        return "[no items]"
    ratio = done / total
    filled = int(ratio * width)
    return "[" + "#" * filled + "-" * (width - filled) + f"] {pct(done, total)}%"

def render_dashboard():
    problems = load_all_problems()
    progress = load_progress()["solved"]

    fundamentals = [p for p in problems if p["source"] == "fundamentals"]
    leetcode = [p for p in problems if p["source"] == "leetcode"]

    # difficulty split
    lc_easy = [p for p in leetcode if (p["difficulty"] or "").lower() == "easy"]
    lc_medium = [p for p in leetcode if (p["difficulty"] or "").lower() == "medium"]
    lc_hard = [p for p in leetcode if (p["difficulty"] or "").lower() == "hard"]

    solved_global = sum(is_solved(p["filename"]) for p in problems)
    solved_f = sum(is_solved(p["filename"]) for p in fundamentals)
    solved_l = sum(is_solved(p["filename"]) for p in leetcode)

    solved_e = sum(is_solved(p["filename"]) for p in lc_easy)
    solved_m = sum(is_solved(p["filename"]) for p in lc_medium)
    solved_h = sum(is_solved(p["filename"]) for p in lc_hard)

    # category split
    def split_by_cat(items):
        out = {}
        for p in items:
            out.setdefault(p["category"], []).append(p)
        return out

    f_cat = split_by_cat(fundamentals)
    lc_cat = split_by_cat(leetcode)

    # recent solved list (sorted by timestamp)
    recent = []
    for fname, info in progress.items():
        ts = info.get("timestamp")
        if ts:
            recent.append((fname, ts))
    recent = sorted(recent, key=lambda x: x[1], reverse=True)[:10]

    out = []
    out.append("# DSA Progress Dashboard\n")

    # overall
    out.append("## Overall Completion")
    out.append(bar(solved_global, len(problems)))
    out.append(f"Solved {solved_global} / {len(problems)}")
    out.append("")
    out.append(f"- Fundamentals: {solved_f} / {len(fundamentals)}")
    out.append(f"- LeetCode: {solved_l} / {len(leetcode)}")
    out.append("")
    out.append(f"- Easy: {solved_e}/{len(lc_easy)}")
    out.append(f"- Medium: {solved_m}/{len(lc_medium)}")
    out.append(f"- Hard: {solved_h}/{len(lc_hard)}")
    out.append("\n")

    # fundamentals compact section
    out.append("## Fundamentals")
    for cat, items in sorted(f_cat.items()):
        solved = sum(is_solved(p["filename"]) for p in items)
        out.append(f"{cat}: {bar(solved, len(items), width=15)}  {solved}/{len(items)}")
    out.append("")

    # leetcode compact section
    out.append("## LeetCode Categories")
    for cat, items in sorted(lc_cat.items()):
        solved = sum(is_solved(p["filename"]) for p in items)
        out.append(f"{cat}: {bar(solved, len(items), width=15)}  {solved}/{len(items)}")
    out.append("")

    # recently solved
    out.append("## Recently Solved")
    if not recent:
        out.append("No problems solved yet.")
    else:
        for fname, ts in recent:
            out.append(f"- {fname}  ({ts})")
    out.append("")

    with open(DASHBOARD_FILE, "w") as f:
        f.write("\n".join(out))

    print("Wrote:", DASHBOARD_FILE)

if __name__ == "__main__":
    render_dashboard()
