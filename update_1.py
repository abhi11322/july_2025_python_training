import sqlite3
conn=sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute("update users set name = 'abhishek' where id = 1")
cursor.execute("update users set age = 25 where id = 5")
conn.commit()
conn.close()