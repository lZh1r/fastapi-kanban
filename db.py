import time

import psycopg2

from model.Task import Task
from model.Column import Column
from model.Board import Board
from model.Log import log

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    dbname="kanban",
    port="5432",
)
conn.autocommit = True


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


def get_all_columns():
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM "column" ORDER BY id;')
        return cur.fetchall()

def insert_column(col: Column):
    with conn.cursor() as cur:
        cur.execute(
            'INSERT INTO "column" (board_id, title) VALUES (%s, %s);',
            (col.board_id, col.title)
        )
    return True

def delete_column(col_id: int):
    with conn.cursor() as cur:
        cur.execute('DELETE FROM "column" WHERE id = %s;', (col_id,))
    return True

def edit_column(col: Column, col_id: int):
    with conn.cursor() as cur:
        cur.execute(
            'UPDATE "column" SET title = %s WHERE id = %s;',
            (col.title, col_id)
        )
    return True


def get_all_boards():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM board ORDER BY id;")
        return cur.fetchall()

def insert_board(board: Board):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO board (title) VALUES (%s);",
            (board.title,)
        )
    return True

def delete_board(board_id: int):
    with conn.cursor() as cur:
        cur.execute("DELETE FROM board WHERE id = %s;", (board_id,))
    return True

def edit_board(board: Board, board_id: int):
    with conn.cursor() as cur:
        cur.execute(
            'UPDATE board SET title = %s WHERE id = %s;',
            (board.title, board_id)
        )
    return True

def get_logs():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM history ORDER BY id;")
        return cur.fetchall()