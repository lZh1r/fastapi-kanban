from core.connect import conn
from model.ProjectMember import ProjectMember
from model.User import User


def register_user(user: User):
    with conn.cursor() as cur:
        cur.execute(
            'INSERT INTO users (username) VALUES (%s);',
            (user.username,)
        )
    return True

def add_user_to_project(project_member: ProjectMember):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO project_members (user_id, board_id) VALUES (%s, %s);",
            (project_member.user_id, project_member.board_id)
        )
    return True

def remove_user_from_project(project_member: ProjectMember):
    with conn.cursor() as cur:
        cur.execute(
            "DELETE FROM project_members WHERE (user_id, board_id) = (%s, %s);",
            (project_member.user_id, project_member.board_id)
        )
    return True