import sqlite3
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()
num=int(input("enter the number of insertions: "))
for i in range(num):
    name= input("enter the name : ")
    age = int(input("enter the age : "))
    cursor.execute("insert into users(name,age) values(?,?)",(name,age))
conn.commit()
conn.close()