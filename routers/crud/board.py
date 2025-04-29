from fastapi import APIRouter

from model.Board import Board
from crud.board import get_all_boards, insert_board, delete_board, edit_board


board_router = APIRouter()

@board_router.get("/boards")
async def get_boards():
    return get_all_boards()

@board_router.post("/boards")
async def create_board(board: Board):
    return insert_board(board)

@board_router.delete("/boards/{board_id}")
async def remove_task(board_id):
    return delete_board(board_id)

@board_router.put("/boards/{board_id}")
async def update_board(board: Board, board_id: int):
    return edit_board(board, board_id)