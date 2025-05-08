from fastapi import APIRouter

from crud.column import get_all_columns, insert_column, delete_column, edit_column
from model.Column import Column

column_router = APIRouter()

@column_router.get("/columns")
async def get_columns():
    return get_all_columns()

@column_router.post("/columns")
async def create_column(col: Column):
    return insert_column(col)

@column_router.delete("/columns/{col_id}")
async def remove_column(col_id):
    return delete_column(col_id)

@column_router.put("/columns/{col_id}")
async def update_column(col: Column, col_id: int):
    return edit_column(col, col_id)