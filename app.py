from fastapi import FastAPI
from pydantic import BaseModel

from agents.bug_agent import analyze_code
from agents.doc_agent import generate_docs
from agents.memory_agent import save_result

app = FastAPI()

class CodeInput(BaseModel):
    code: str

@app.post("/analyze")
def analyze(input_data: CodeInput):
    try:
        bugs = analyze_code(input_data.code)
        docs = generate_docs(input_data.code)

        result = {
            "bugs": bugs,
            "docs": docs
        }

        save_result(result)   # 👈 add this back

        return result

    except Exception as e:
        return {"error": str(e)}

    except Exception as e:
        return {"error": str(e)}

    result = {
        "bugs": bugs,
        "docs": docs
    }

    save_result(result)

    return result