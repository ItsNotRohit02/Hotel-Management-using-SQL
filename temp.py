import mysql.connector as connector

global con, cur
con = connector.connect(host='localhost', port='3306',
                        user='root', password='8792894300',
                        database='pythontest')
cur = con.cursor()


def createtable():
    query = "create table if not exists user(userID int primary key, username varchar(50), phone varchar(12))"
    cur.execute(query)
    print('Created')


def insert(id, name, ph):
    query = f"insert into user values({id},'{name}','{ph}')"
    print(query)
    cur.execute(query)
    con.commit()
    print('Inserted')


def fetch():
    query = 'select * from user'
    cur.execute(query)
    for row in cur:
        print(row)


def delete(id):
    query = f"delete from user where userID={id}"
    cur.execute(query)
    con.commit()
    print('Deleted')


delete(1410)
