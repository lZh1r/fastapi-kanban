from core.connect import conn
from model.Board import Board


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