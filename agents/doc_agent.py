def generate_docs(code: str):
    docs = []

    if "print" in code:
        docs.append("This code prints output to the console.")

    if "def " in code:
        docs.append("This code defines a function.")

    if "for " in code or "while " in code:
        docs.append("This code contains a loop.")

    if "=" in code:
        docs.append("This code performs variable assignment.")

    if not docs:
        docs.append("Basic code execution.")

    return docs