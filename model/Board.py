from dataclasses import dataclass


@dataclass
class Column:
    title: str
    id: int = 0
