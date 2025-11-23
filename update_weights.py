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
        "values are integer weights 1–10. No markdown. No commentary."
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
    except:
        print("INVALID JSON FROM MODEL:", content)
        return None


def update_json(json_data, weights):
    root_key = list(json_data.keys())[0]
    for item in json_data[root_key]:
        if item["id"] in weights:
            item["weight"] = weights[item["id"]]
    return json_data


def process(path):
    print(f"=== Processing {path} ===")

    with open(path, "r") as f:
        data = json.load(f)

    ids = get_id_list(data)

    print("IDs:", ids)

    weights = ask_model_for_weights(ids)
    if weights is None:
        print("Skipping due to invalid model output.")
        return

    print("Returned weights:", weights)

    updated = update_json(data, weights)

    backup = path + ".bak"
    os.replace(path, backup)

    with open(path, "w") as f:
        json.dump(updated, f, indent=2)

    print(f"Updated {path} (backup at {backup})")


def main():
    for name in os.listdir(FOLDER):
        if name.endswith(".json"):
            process(os.path.join(FOLDER, name))


if __name__ == "__main__":
    main()
