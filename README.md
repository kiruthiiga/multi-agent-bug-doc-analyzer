# Multi-Agent Bug & API Documentation Analyzer

## Overview

The **Multi-Agent Bug & API Documentation Analyzer** is a backend automation project built using **FastAPI** that combines multiple intelligent agents to analyze backend code, detect potential issues, and automatically generate API documentation.

This project demonstrates a **multi-agent pipeline** architecture where each agent performs a dedicated task in the workflow. It also maintains memory of previous analyses and exposes the workflow through an API endpoint.

---

## Features

### Bug Analyzer Agent
- Scans backend Python code for:
  - Syntax errors
  - Long functions
  - Risky coding patterns
- Returns bug analysis reports

### API Documentation Generator Agent
- Parses API routes from source code
- Generates endpoint documentation including:
  - Route path
  - HTTP method
  - Description

### Memory Agent
- Stores analysis history
- Maintains previous bug reports and generated docs

### API Endpoint
- Provides a FastAPI endpoint to:
  - Submit code
  - Receive bug analysis
  - Get API documentation

---

## Architecture

```text
User submits backend code
        ↓
Coordinator
        ↓
 ┌──────────────┬──────────────┬──────────────┐
 │ Bug Agent    │ Doc Agent    │ Memory Agent │
 └──────────────┴──────────────┴──────────────┘
        ↓
Returns analysis + generated docs



Tech Stack
Python
FastAPI
Uvicorn
AST (Abstract Syntax Tree)
JSON Memory Storage
Project Structure
multi-agent-bug-doc-analyzer/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│
├── agents/
│   │── bug_agent.py
│   │── doc_agent.py
│   │── memory_agent.py
│
├── tools/
│   │── code_parser.py
│
├── memory/
│   │── history.json
│
├── tests/
│   │── test_app.py
Workflow
User submits Python backend code via API
Bug Agent analyzes the code for possible issues
Doc Agent extracts API routes and generates documentation
Memory Agent stores the analysis results
API returns:
Bug analysis
Generated API documentation
Installation
Clone the repository
git clone https://github.com/YOUR_USERNAME/multi-agent-bug-doc-analyzer.git
cd multi-agent-bug-doc-analyzer
Install dependencies
pip install -r requirements.txt
Run the Application

Start the FastAPI server:

uvicorn app:app --reload

Open the API docs:

http://127.0.0.1:8000/docs
API Endpoint
POST /analyze

Submit Python backend code for analysis.

Request Body
{
  "code": "from fastapi import FastAPI\napp = FastAPI()\n@app.get('/users')\ndef get_users(): return []"
}
Sample Response
{
  "bugs": [
    "No major bugs found"
  ],
  "docs": [
    {
      "endpoint": "/users",
      "method": "GET",
      "description": "get_users endpoint"
    }
  ]
}
Future Enhancements
Integrate LangGraph for advanced agent orchestration
Add LLM-based bug analysis
Support Swagger/OpenAPI schema generation
Add database memory storage
Add frontend dashboard for reports
Learning Outcomes

This project demonstrates:

Multi-agent backend workflow design
Tool-calling architecture
Persistent memory handling
API development using FastAPI
Automated bug analysis and documentation generation
Author
