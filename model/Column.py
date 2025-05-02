from pydantic import BaseModel


class Column(BaseModel):
    board_id: int
    title: str
    id: int = 0
