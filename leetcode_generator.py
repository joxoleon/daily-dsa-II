import asyncio
import json
from functools import lru_cache
from pathlib import Path

import requests
from openai import AsyncOpenAI

# ==========================================
# CONFIG
# ==========================================
MODEL = "gpt-4.1"
INPUT_JSON = Path("leetcode_input/leetcode.json")
OUTPUT_DIR = Path("leetcode")

# ==========================================
# PROMPT BUILDER
# ==========================================
def build_prompt(meta: dict, category: str, difficulty: str) -> str:
    """
    Builds the prompt that generates a Python file template.
    """

    name = meta["title"]
    topic = meta.get("topic", category)
    weight = meta["weight"]
    link = meta["link"]

    return f'''
Generate a SINGLE Python file for a coding problem template.

STRICT RULES:

============================================================
1. HEADER FORMAT (USE EXACT STYLE)
============================================================

# [ Name: {name} ]  [ Category: {category} ]  [ Topic: {topic} ]  [ Weight: {weight} ]  [ Difficulty: {difficulty} ]
# [ Link: {link} ]

============================================================
2. PROBLEM DESCRIPTION (LeetCode-style)
============================================================

Inside a triple-quoted string, write a concise 3–8 line LeetCode-style description:

- Goal of the problem
- Inputs / outputs
- Constraints (brief)
- One example only
- NO solution strategy
- NO pseudocode

============================================================
3. IMPLEMENTATION SKELETON
============================================================

Infer the correct function signature based on the known LeetCode problem.
Rules:
- Use correct parameter types (List[int], str, TreeNode, etc.)
- Add necessary imports
- Body must contain EXACTLY:
        pass

============================================================
4. TEST CASES
============================================================

At the bottom:

if __name__ == "__main__":
    # At least 8 assert-based tests
    # No blank lines between asserts

============================================================
5. OUTPUT FORMAT
============================================================

- Output ONLY valid Python code
- NO markdown
- NO ``` 
'''

# ==========================================
# DIFFICULTY LOOKUP
# ==========================================
@lru_cache(maxsize=None)
def fetch_difficulty(slug: str) -> str:
    """
    Fetch the official LeetCode difficulty for a slug via GraphQL.
    Falls back to 'unknown' if the request fails or the slug is missing.
    """
    query = """
    query getQuestionDifficulty($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            difficulty
        }
    }
    """
    try:
        resp = requests.post(
            "https://leetcode.com/graphql",
            json={"query": query, "variables": {"titleSlug": slug}},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()
        return data.get("data", {}).get("question", {}).get("difficulty", "unknown")
    except Exception as exc:
        print(f"[!] Difficulty lookup failed for {slug}: {exc}")
        return "unknown"

# ==========================================
# LOAD GROUPS
# ==========================================
def load_groups():
    """
    Load a single JSON that contains categories mapping to lists of items.
    """
    with open(INPUT_JSON, "r") as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError("leetcode.json must contain a top-level object of groups.")

    for group_name, items in data.items():
        if not isinstance(items, list):
            continue
        yield group_name, items

# ==========================================
# GENERATION
# ==========================================
def generate_all():

    async def generate_one(
        client: AsyncOpenAI,
        semaphore: asyncio.Semaphore,
        category_dir: Path,
        width: int,
        idx: int,
        meta: dict,
        category: str
    ):
        slug = meta["slug"]
        difficulty = meta.get("difficulty") or fetch_difficulty(slug)
        prompt = build_prompt(meta, category, difficulty)

        filename = f"{idx:0{width}d}_{slug}.py"
        file_path = category_dir / filename

        print(f"[*] Generating {slug} ({category})")

        async with semaphore:
            response = await client.responses.create(
                model=MODEL,
                input=prompt
            )

        content = response.output_text
        await asyncio.to_thread(file_path.write_text, content)

        print(f"[+] Saved: {file_path}")

    async def process_one_group(client, semaphore, category, items):

        category_dir = OUTPUT_DIR / category
        category_dir.mkdir(parents=True, exist_ok=True)

        width = max(2, len(str(len(items))))

        tasks = [
            asyncio.create_task(generate_one(
                client, semaphore, category_dir, width, idx, meta, category
            ))
            for idx, meta in enumerate(items)
        ]

        await asyncio.gather(*tasks)

    async def run():
        client = AsyncOpenAI()
        semaphore = asyncio.Semaphore(5)

        for category, items in load_groups():
            await process_one_group(client, semaphore, category, items)

        print("All LeetCode templates generated successfully.")

    asyncio.run(run())


if __name__ == "__main__":
    generate_all()
