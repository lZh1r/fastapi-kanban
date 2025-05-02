from pydantic import BaseModel


class Board(BaseModel):
    title: str
    id: int = 0
