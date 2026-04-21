import json
import os

def save_result(result: dict):
    os.makedirs("results", exist_ok=True)

    file_path = "results/output.json"

    # If file exists, read old data safely
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                data = json.load(f)
        except:
            data = []   # if file is empty or corrupted
    else:
        data = []

    # Append new result
    data.append(result)

    # Write back
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)