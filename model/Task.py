from pydantic import BaseModel


class Task(BaseModel):
    column_id: int
    title: str
    description: str
    id: int = 0
    is_completed: bool = False
