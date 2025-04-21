import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="postgres",
    password="123456",
    dbname="kanban",
    port="5432",
)

