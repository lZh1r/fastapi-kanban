from fastapi import APIRouter

from model.ProjectMember import ProjectMember
from model.User import User
from crud.user import register_user, add_user_to_project, remove_user_from_project


user_router = APIRouter()

@user_router.post("/users")
async def create_user(user: User):
    return register_user(user)

@user_router.post("/project")
async def assign_user(project_member: ProjectMember):
    return add_user_to_project(project_member)

@user_router.delete("/project")
async def delete_user(project_member: ProjectMember):
    return remove_user_from_project(project_member)