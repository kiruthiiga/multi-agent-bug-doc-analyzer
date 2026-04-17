import json
import os

MEMORY_FILE = "memory/history.json"

def save_result(result):
    history = []

    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            history = json.load(f)

    history.append(result)

    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

