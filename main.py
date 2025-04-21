from fastapi import FastAPI

from db import get_all_tasks, get_all_columns, get_all_boards

app = FastAPI()


@app.get("/tasks")
async def root():
    return get_all_tasks()

@app.get("/columns")
async def root():
    return get_all_columns()

@app.get("/boards")
async def root():
    return get_all_boards()
