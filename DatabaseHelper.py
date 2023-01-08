import mysql.connector as connector

global con, cur
con = connector.connect(host='localhost', port='3306', user='root', password='8792894300', database='hotelmanagement')
cur = con.cursor()


def createtables():
    query = "create table if not exists customerdetails(cid int primary key,aadhar int, cname char(50), cage int, phone int, caddress char(100))"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists room(roomnum int primary key,roomtypeid int, size int, availability char(20))"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists roomtype(roomtypeid int primary key,bednum int, ac char(5), rate float, description char(200))"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists roomservice(orderid int primary key,itemid int, quantity int, price float)"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists items(itemid int primary key,itemname char(20), rate float)"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists bookingdetails(bid int primary key,cid int, roomnum int, checkin date, checkout date, finalprice float, paymentstatus char(20))"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists expenses(cid int, roomnum int, orderid int, orderprice float, roomprice float , finalprice float)"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists employees(empid int primary key, aadhar int, ename char(50), bday date, age int, gender char(10), roleid int, sal float)"
    cur.execute(query)
    print("OK ", query)
    query = "create table if not exists roles(roleid int primary key, rolename char(50),sal float)"
    cur.execute(query)
    print("OK ", query)


def addforeignkeys():
    query = "alter table room add foreign key(roomtypeid) references roomtype(roomtypeid) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table roomservice add foreign key(itemid) references items(itemid) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table bookingdetails add foreign key(cid) references customerdetails(cid) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table bookingdetails add foreign key(roomnum) references room(roomnum) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table expenses add foreign key(cid) references customerdetails(cid) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table expenses add foreign key(roomnum) references room(roomnum) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table expenses add foreign key(orderid) references roomservice(orderid) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)
    query = "alter table employees add foreign key(roleid) references roles(roleid) on update cascade on delete cascade"
    cur.execute(query)
    print("OK ", query)



