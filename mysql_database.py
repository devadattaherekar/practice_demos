import mysql.connector

def create_table():
    connection=mysql.connector.connect(database="mydb",user="root",password="redhat",port=3306,host="localhost")
    cursor=connection.cursor()
    cursor.execute('create table  if not exists employee(empid integer primary key, empname text,empsal real)')
    connection.commit()
    connection.close()

create_table()

def add_employee(id,name,sal):
    connection = mysql.connector.connect(database="mydb", user="root", password="redhat", port=3306, host="localhost")
    cursor=connection.cursor()
    cursor.execute('insert into employee values(%s,%s,%s)',(id,name,sal))
    connection.commit()
    connection.close()

# add_employee(1000,"hrishikesh",800000)
# add_employee(2000,"deva",500000)
# add_employee(3000,"arjun",600000)
# add_employee(4000,"shivani",700000)


def select_employee():
    connection = mysql.connector.connect(database="mydb", user="root", password="redhat", port=3306, host="localhost")
    cursor=connection.cursor()
    cursor.execute('select *from employee')
    for id,name,sal in cursor.fetchall():
         print(f'{name} with empid {id} has sal {sal}')
    connection.commit()
    connection.close()

select_employee()


def delete_employee(id):
    connection = mysql.connector.connect(database="mydb", user="root", password="redhat", port=3306, host="localhost")
    cursor=connection.cursor()
    cursor.execute('delete from employee where empid=%s',(id,) )
    connection.commit()
    connection.close()

delete_employee(2000)
select_employee()

def update_employee(id,sal):
    connection = mysql.connector.connect(database="mydb", user="root", password="redhat", port=3306, host="localhost")
    cursor=connection.cursor()
    cursor.execute('update employee set empsal=%s where empid=%s',(sal,id) )
    connection.commit()
    connection.close()

update_employee(1000,900000)
select_employee()