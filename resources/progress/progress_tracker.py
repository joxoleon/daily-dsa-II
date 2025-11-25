import json
import os
from datetime import datetime

PROGRESS_FILE = "progress.json"

def normalize(path: str) -> str:
    """
    Always store filenames as RELATIVE paths from repo root.
    """
    return os.path.relpath(path)

def load_progress():
    if not os.path.exists(PROGRESS_FILE):
        return {"solved": {}}

    with open(PROGRESS_FILE, "r") as f:
        data = json.load(f)

    # normalize keys (in case old absolute paths exist)
    fixed = {}
    for k, v in data.get("solved", {}).items():
        fixed[normalize(k)] = v

    return {"solved": fixed}

def save_progress(progress):
    # always save normalized keys
    fixed = { normalize(k): v for k, v in progress["solved"].items() }

    with open(PROGRESS_FILE, "w") as f:
        json.dump({"solved": fixed}, f, indent=4)

def mark_solved(filename: str):
    filename = normalize(filename)
    progress = load_progress()
    progress["solved"][filename] = {
        "solved": True,
        "timestamp": datetime.utcnow().isoformat()
    }
    save_progress(progress)

def is_solved(filename: str) -> bool:
    filename = normalize(filename)
    progress = load_progress()
    return filename in progress["solved"]
