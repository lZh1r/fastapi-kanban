from fastapi import FastAPI

from crud.log import get_logs

from routers.board import board_router
from routers.column import column_router
from routers.task import task_router
from routers.user import user_router

app = FastAPI()
app.include_router(task_router, tags=["task"])
app.include_router(column_router, tags=["column"])
app.include_router(board_router, tags=["board"])
app.include_router(user_router, tags=["user"])

@app.get("/logs")
async def get_history():
    return get_logs()

