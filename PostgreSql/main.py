import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "1234",
    dbname = "school"
)
#cursor
cursor = conn.cursor()
cursor.execute("INSERT INTO student_details (name,phone,class) VALUES ('ANUJ',2589631235,'LAW')")
conn.commit()
cursor.execute("select * from student_details")
for data in cursor.fetchall():
    print(data)
conn.close()

