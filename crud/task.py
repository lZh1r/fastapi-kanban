from core.connect import conn
from model.Log import log
from model.Task import Task


def get_all_tasks():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM task ORDER BY id;")
        return cur.fetchall()

def get_tasks_from_col(col_id: int):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT * FROM task WHERE column_id = %s ORDER BY id;",
            (col_id,)
        )
        return cur.fetchall()

def insert_task(task: Task):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO task (column_id, title, description, is_completed) VALUES (%s, %s, %s, %s);",
            (task.column_id, task.title, task.description, task.is_completed)
        )
    return True

def delete_task(task_id: int):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM task WHERE id = %s;", (task_id,))
        log("delete", task_id, conn)
    return True

def edit_task(task: Task, task_id: int):
    with conn.cursor() as cur:
        cur.execute(
            "UPDATE task SET column_id = %s, title = %s, description = %s, is_completed = %s WHERE id = %s;",
            (task.column_id, task.title, task.description, task.is_completed, task_id)
        )
        log("edit", task_id, conn)
    return True