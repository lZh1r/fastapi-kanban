from core.connect import conn
from model.Column import Column


def get_all_columns():
    with conn.cursor() as cur:
        cur.execute('SELECT * FROM "column" ORDER BY id;')
        return cur.fetchall()

def insert_column(column: Column):
    with conn.cursor() as cur:
        cur.execute(
            'INSERT INTO "column" (board_id, title) VALUES (%s, %s);',
            (column.board_id, column.title)
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
