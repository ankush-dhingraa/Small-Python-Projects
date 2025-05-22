import psycopg2
conn = psycopg2.connect(
    host = "localhost",
    user = "postgres",
    password = "1234",
    dbname = "school"
)

def insert(table,value,columns):
    v = tuple(value)
    cl = tuple(columns)
    query = f"INSERT INTO {table} {columns} VALUES {v}"
    return query


cursor = conn.cursor()
# cursor.execute(insert("student_details",columns=(name,'phone','class'),value=))
# cursor.execute("INSERT INTO student_details (name,phone,class) VALUES ('jatin',2589631445,'MEDICAL')")
# conn.commit()
cursor.execute("select * from student_details where class = 'MEDICAL'")
for data in cursor.fetchall():
    print(data)
conn.close()

