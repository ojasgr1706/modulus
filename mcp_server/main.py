from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/context")
def get_context():
    return JSONResponse({
        "name": "Simple Web Tool Agent",
        "description": "Uses calculator or search tool to answer user queries.",
        "capabilities": ["calculator", "web-search"]
    })

@app.get("/task")
def get_task():
    return JSONResponse({
        "task_id": "task-001",
        "objective": "Answer: What is the capital of France plus 3*7?"
    })
