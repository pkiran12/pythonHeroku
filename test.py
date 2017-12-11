import sqlite3


connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table="Create table users (id int, username text,password text)"

cursor.execute(create_table)

user= (1,"kiran","abcd")


users=[

(2,"kiran1","abcd"),
(4,"kiran2","abcd"),
(3,"kiran3","abcd")

]



insert_query="Insert into users values (?,?,?) "

#cursor.execute(insert_query,user)

cursor.executemany(insert_query,users)


select_query ="Select * from users"

value=cursor.execute(select_query)

for row in value:
    print(row)

connection.commit()

connection.close()
