import os
import json
from pathlib import Path
from openai import OpenAI

client = OpenAI()

# ==========================================
# CONFIG
# ==========================================
MODEL = "gpt-4.1"     # You can use gpt-5.1 if you want max quality
OUTPUT_DIR = Path("fundamentals")

FUNDAMENTALS_PATH = Path("fundamentals.json")

# ==========================================
# HELPER: build prompt for a single fundamental
# ==========================================
def build_prompt(meta: dict) -> str:
    """
    Build a prompt that forces the model to generate a full doc-style problem description
    along with a skeleton Python file.
    """
    return f"""
You are generating a SINGLE Python file containing a clean, high-quality coding problem template.

Produce a beautifully formatted file with the following rules:

============================================================
1. BEGIN WITH A DETAILED MULTI-LINE COMMENT BLOCK
============================================================

This block must read like a professional problem statement.

It MUST include:

### Fundamental ID
{meta['id']}

### Name
{meta['name']}

### Category
{meta['category']}

### Topic
{meta['topic']}

### Weight (Importance)
{meta['weight']}

### Problem Description (VERY IMPORTANT — Write a FULL DOC-STYLE STATEMENT)

Write a clear, multi-paragraph explanation describing:

- The goal of the problem  
- What the function should compute  
- A thorough explanation of input parameters  
- Expected output description  
- Valid and invalid cases (if any)  
- Common edge cases  
- Small example(s) written in plain English  
- DO NOT provide any solution hints  
- NO pseudocode  
- NO implementation logic  
- This must look like a polished problem prompt from LeetCode or a coding interview.

### Function Signature
Show the exact Python function signature:
    {meta['signature']}

============================================================
2. IMPLEMENTATION SECTION
============================================================

After the comment block:

- Write the full function/class signature exactly as given.
- Replace the body with ONLY:
      # TODO: implement
      pass
- Do not modify the signature.
- Add necessary imports (`from typing import List, Optional`) if the signature uses them.

============================================================
3. TEST SECTION (GENERATE YOUR OWN BASED ON THE DESCRIPTION)
============================================================

At the bottom, generate:

if __name__ == "__main__":
    # create meaningful test inputs based on the description
    # write at least 8 assert-based tests - sensible and edge cases
    # DO NOT solve the function — just call it with expected placeholder outputs
    # For example:
    # assert myfunc(input) == expected_value

YOU:  
- MUST create your own test cases  
- Test cases must be realistic  
- Test cases MUST match the description  

============================================================
4. OUTPUT RULES
============================================================

- Output ONLY the Python file content.
- Do NOT include markdown formatting.
- Do NOT include backticks.
- Do NOT include meta-explanation.
- The output must be directly savable as a .py file.
"""



# ==========================================
# MAIN GENERATION
# ==========================================
def generate_all_fundamentals():
    with open(FUNDAMENTALS_PATH, "r") as f:
        fundamentals_data = json.load(f)

    for group_name, group_items in fundamentals_data.items():
        group_dir = OUTPUT_DIR / group_name
        group_dir.mkdir(parents=True, exist_ok=True)

        for meta in group_items:
            prompt = build_prompt(meta)

            print(f"[*] Generating: {meta['id']}  ({group_name})")

            response = client.responses.create(
                model=MODEL,
                input=prompt
            )

            # Extract the text output
            content = response.output_text

            # Save the file
            file_path = group_dir / f"{meta['id']}.py"
            file_path.write_text(content)
            print(f"[+] Saved to {file_path}")

    print("All fundamentals generated successfully.")


if __name__ == "__main__":
    generate_all_fundamentals()
