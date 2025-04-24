from fastapi import FastAPI

from db import get_all_tasks, get_all_columns, get_all_boards, delete_task, insert_task, insert_column, delete_column, \
    insert_board, delete_board, edit_column, edit_task, edit_board, get_tasks_from_col, get_logs, register_user, \
    add_user_to_project, remove_user_to_project
from model.ProjectMember import ProjectMember

from model.Task import Task
from model.Column import Column
from model.Board import Board
from model.User import User

app = FastAPI()


@app.get("/tasks")
async def get_tasks():
    return get_all_tasks()

@app.get("/tasks/{col_id}")
async def get_tasks_by_col(col_id: int):
    return get_tasks_from_col(col_id)

@app.post("/tasks")
async def create_task(task: Task):
    return insert_task(task)

@app.delete("/tasks/{task_id}")
async def remove_task(task_id):
    return delete_task(task_id)

@app.put("/tasks/{task_id}")
async def update_task(task_id, task: Task):
    return edit_task(task, task_id)


@app.get("/columns")
async def get_columns():
    return get_all_columns()

@app.post("/columns")
async def create_column(col: Column):
    return insert_column(col)

@app.delete("/columns/{col_id}")
async def remove_column(col_id):
    return delete_column(col_id)

@app.put("/columns/{col_id}")
async def update_column(col: Column, col_id: int):
    return edit_column(col, col_id)


@app.get("/boards")
async def get_boards():
    return get_all_boards()

@app.post("/boards")
async def create_board(board: Board):
    return insert_board(board)

@app.delete("/boards/{board_id}")
async def remove_task(board_id):
    return delete_board(board_id)

@app.put("/boards/{board_id}")
async def update_board(board: Board, board_id: int):
    return edit_board(board, board_id)


@app.get("/logs")
async def get_history():
    return get_logs()

@app.post("/users")
async def create_user(user: User):
    return register_user(user)

@app.post("/project")
async def assign_user(project_member: ProjectMember):
    return add_user_to_project(project_member)

@app.delete("/project")
async def delete_user(project_member: ProjectMember):
    return remove_user_to_project(project_member)