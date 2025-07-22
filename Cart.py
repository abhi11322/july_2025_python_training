import sqlite3
conn = sqlite3.connect('ecom.db')
cursor=conn.cursor()
cursor.execute('''
create table if not exists customer (
    u_id Integer primary key autoincrement,
    name text not null,
    email text not null,
    password text not null       
)
''')
cursor.execute('''
create table if not exists orders (
    o_id Integer primary key autoincrement,
    c_id Integer not null,
    amount integer not null,
    date  date      
)
''')
cursor.execute('''
create table if not exists product (
    p_id Integer primary key autoincrement,
    name text not null,
    price integer not null,
    description text      
)
''')
cursor.execute('''
create table if not exists payment (
    p_id Integer primary key autoincrement,
    type text not null,
    amount integer not null     
)
''')
cursor.execute('''
create table if not exists category (
    c_id Integer primary key autoincrement,
    name text not null,
    picture varchar not null,
    description text    
)
''')
cursor.execute('''
create table if not exists cart (
    c_id Integer primary key autoincrement,
    u_id integer not null    
)
''')
conn.commit()
conn.close()