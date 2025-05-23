# print("Django Practice")
import psycopg2 as pg
conn = pg.connect(
    host = "localhost",
    user = "postgres",
    password = "1234",
    dbname = "school"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM student_details")
for data in cursor.fetchall():
    print(data)
conn.close()