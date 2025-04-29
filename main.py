from fastapi import FastAPI

from crud.log import get_logs

from routers.crud.board import board_router
from routers.crud.column import column_router
from routers.crud.task import task_router
from routers.crud.user import user_router

app = FastAPI()
app.include_router(task_router)
app.include_router(column_router)
app.include_router(board_router)
app.include_router(user_router)

@app.get("/logs")
async def get_history():
    return get_logs()

