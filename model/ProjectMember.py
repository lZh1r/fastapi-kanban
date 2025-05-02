from pydantic import BaseModel


class ProjectMember(BaseModel):
    user_id: int
    board_id: int
