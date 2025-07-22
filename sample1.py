import sqlite3
conn = sqlite3.connect('mydata.db')
cursor=conn.cursor()
cursor.execute('''
create table if not exists users (
    id Integer primary key autoincrement,
    name text not null,
    age integer 
)
''')

cursor.execute("insert into users(name,age) values(?,?)",("alice",25))
cursor.execute("insert into users(name,age) values(?,?)",("bob",24))
conn.commit()
conn.close()