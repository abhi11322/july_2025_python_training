import sqlite3
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

cursor.execute("select * from users")
rows=cursor.fetchall()

for rows in rows:
    print(rows)

conn.close()    