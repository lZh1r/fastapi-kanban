from pydantic import BaseModel


class User(BaseModel):
    username: str
    id: int = 0
