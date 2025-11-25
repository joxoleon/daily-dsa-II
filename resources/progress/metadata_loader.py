import os
import re

def load_all_problems():
    root = "00_structured"
    problems = []
    
    meta_re = re.compile(r"\[\s*Name:\s*(.*?)\s*\]\s*\[\s*Category:\s*(.*?)\s*\]\s*\[\s*Topic:\s*(.*?)\s*\]\s*\[\s*Weight:\s*(.*?)\s*\]")

    for base, _, files in os.walk(root):
        for f in files:
            if not f.endswith(".py"):
                continue

            full_path = os.path.join(base, f)
            rel = os.path.relpath(full_path)

            source = "fundamentals" if "fundamentals" in rel else "leetcode"

            with open(full_path, "r") as fp:
                head = fp.read(512)

            m = meta_re.search(head)
            if not m:
                continue

            name, category, topic, weight = m.groups()

            problems.append({
                "filename": rel,
                "name": name.strip(),
                "category": category.strip(),
                "topic": topic.strip(),
                "weight": int(weight.strip()),
                "source": source,
                "difficulty": extract_difficulty_from_filename(rel) if source=="leetcode" else None
            })

    return problems

def extract_difficulty_from_filename(path: str):
    # Very rough: filenames contain e.g. easy, medium, hard
    l = path.lower()
    if "easy" in l: return "easy"
    if "medium" in l: return "medium"
    if "hard" in l: return "hard"
    return "unknown"
