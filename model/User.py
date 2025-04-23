from dataclasses import dataclass


@dataclass
class User:
    username: str
    id: int = 0
