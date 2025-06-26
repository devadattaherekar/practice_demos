import sqlite3

# It does not perform multiple write operations but multiple reads are allowed RDBMS (Relational Database Management Systems)
# integer, real, text, blob, null

# 5 steps to connect to any database
# create connection
# create cursor using connection reference
# execute query using cursor
# commit connection
# close connection

def create_table():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    cursor.execute('create table  if not exists employee(empid integer primary key, empname text,empsal real)')
    connection.commit()
    connection.close()

create_table()

def add_employee(id,name,sal):
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    cursor.execute('insert into employee values(?,?,?)',(id,name,sal))
    connection.commit()
    connection.close()

# add_employee(1000,"hrishikesh",800000)
# add_employee(2000,"deva",500000)
# add_employee(3000,"arjun",600000)
# add_employee(4000,"shivani",700000)


def select_employee():
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    data=cursor.execute('select *from employee')
    #print(data.fetchall())
    # first_row=data.fetchone()
    # print("First row is ",first_row)
    print(data.fetchall())
    for id,name,sal in data.fetchall():
         print(f'{name} with empid {id} has sal {sal}')
    connection.commit()
    connection.close()




def delete_employee(id):
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    cursor.execute('delete from employee where empid=?',(id,) )
    connection.commit()
    connection.close()

delete_employee(2000)

select_employee()


def update_employee(id,sal):
    connection=sqlite3.connect('database.db')
    cursor=connection.cursor()
    cursor.execute('update employee set empsal=? where empid=?',(sal,id) )
    connection.commit()
    connection.close()

update_employee(1000,900000)

select_employee()