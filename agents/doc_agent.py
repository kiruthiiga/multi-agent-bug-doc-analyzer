from tools.code_parser import extract_routes

def generate_docs(code: str):
    routes = extract_routes(code)

    docs = []
    for route in routes:
        docs.append({
            "endpoint": route["path"],
            "method": route["method"],
            "description": f"{route['function']} endpoint"
        })

    return docs

