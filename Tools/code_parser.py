import ast

def extract_routes(code: str):
    tree = ast.parse(code)
    routes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                if isinstance(decorator, ast.Call):
                    if hasattr(decorator.func, 'attr'):
                        route_type = decorator.func.attr
                        if decorator.args:
                            path = decorator.args[0].value
                            routes.append({
                                "function": node.name,
                                "method": route_type.upper(),
                                "path": path
                            })
    return routes

