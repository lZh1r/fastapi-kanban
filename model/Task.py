from dataclasses import dataclass


@dataclass
class Task:
    column_id: int
    title: str
    description: str
    id: int = 0
    is_completed: bool = False
