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
cursor.execute("INSERT INTO student_details (name,phone,class) VALUES ('daksh',2589631475,'BCA')")
conn.commit()
conn.close()

