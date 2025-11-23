import json
import os
from openai import OpenAI

client = OpenAI()

MODEL = "gpt-4.1-mini"
FOLDER = "fundamentals_input"


def get_id_list(json_data):
    root_key = list(json_data.keys())[0]
    return [item["id"] for item in json_data[root_key]]


def ask_model_for_weights(ids):
    system_prompt = (
        "You output ONLY a flat JSON object where keys are problem IDs and "
        "values are integer weights 1–10. No markdown. No commentary. No text."
    )

    user_prompt = "IDs:\n" + "\n".join(ids)

    resp = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    content = resp.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print("INVALID JSON FROM MODEL:", content)
        return None


def update_json(json_data, weights):
    root_key = list(json_data.keys())[0]
    for item in json_data[root_key]:
        item_id = item["id"]
        if item_id in weights:
            item["weight"] = weights[item_id]
    return json_data


def process(path):
    print(f"=== Processing {path} ===")

    # Load file
    try:
        with open(path, "r") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        print("!!! FILE IS EMPTY OR INVALID JSON — SKIPPING")
        return

    ids = get_id_list(data)
    if not ids:
        print("No IDs found, skipping.")
        return

    print("IDs:", ids)

    weights = ask_model_for_weights(ids)
    if weights is None:
        print("Skipping due to invalid model output.")
        return

    print("Returned weights:", weights)

    updated = update_json(data, weights)

    # Write updated file (NO BACKUPS)
    with open(path, "w") as f:
        json.dump(updated, f, indent=2)

    print(f"✓ Updated {path} successfully\n")


def main():
    for name in os.listdir(FOLDER):
        if name.endswith(".json"):
            process(os.path.join(FOLDER, name))


if __name__ == "__main__":
    main()
