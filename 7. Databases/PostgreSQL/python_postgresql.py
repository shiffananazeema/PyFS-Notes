import psycopg2

conn = psycopg2.connect(
    dbname="learning",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cur = conn.cursor()
cur.execute("SELECT * FROM users")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
