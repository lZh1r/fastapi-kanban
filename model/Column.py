from dataclasses import dataclass


@dataclass
class Column:
    board_id: int
    title: str
    id: int = 0
