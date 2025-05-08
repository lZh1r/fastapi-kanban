from fastapi import APIRouter

from crud.task import get_all_tasks, delete_task, insert_task, edit_task, get_tasks_from_col
from model.Task import Task

task_router = APIRouter()

@task_router.get("/tasks")
async def get_tasks():
    return get_all_tasks()

@task_router.get("/tasks/{col_id}")
async def get_tasks_by_col(col_id: int):
    return get_tasks_from_col(col_id)

@task_router.post("/tasks")
async def create_task(task: Task):
    return insert_task(task)

@task_router.delete("/tasks/{task_id}")
async def remove_task(task_id):
    return delete_task(task_id)

@task_router.put("/tasks/{task_id}")
async def update_task(task_id, task: Task):
    return edit_task(task, task_id)