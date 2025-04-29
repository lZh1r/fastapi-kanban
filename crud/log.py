from core.connect import conn


def get_logs():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM history ORDER BY id;")
        return cur.fetchall()