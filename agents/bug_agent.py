import ast

def analyze_code(code: str):
    issues = []

    try:
        tree = ast.parse(code)
    except SyntaxError as e:
        issues.append(f"Syntax Error: {e}") 
        return issues

    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            continue
        if isinstance(node, ast.FunctionDef):
            if len(node.body) > 10:
                issues.append(f"Function '{node.name}' is too long")

    if not issues:
        issues.append("No major bugs found")

    return issues

