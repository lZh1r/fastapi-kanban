import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    dbname="kanban",
    port="5432",
)
conn.autocommit = True

def get_all_tasks():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM task ORDER BY id;")
        return cur.fetchall()

def get_all_columns():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM column ORDER BY id;")
        return cur.fetchall()

def get_all_boards():
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM board ORDER BY id;")
        return cur.fetchall()
