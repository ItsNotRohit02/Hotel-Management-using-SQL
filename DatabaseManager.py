import mysql.connector as connector
import pandas as pd

global con, cur
con = connector.connect(host='localhost', port='3306', user='root', password='root', database='hoteldatabase')
cur = con.cursor()


def createTables():
    queries = [
        "create table if not exists customerdetails(cid int primary key,aadhar char(20), cname char(50), cage int, phone char(20), caddress char(100), finalprice float, checkin date,checkout date)",
        "create table if not exists room(roomnum int primary key,roomtypeid int, size int)",
        "create table if not exists roomtype(roomtypeid int primary key,bednum int, ac char(10), rate float, description char(200))",
        "create table if not exists roomservice(orderid int primary key,itemid int, quantity int, rscid int)",
        "create table if not exists items(itemid int primary key,itemname char(20), rate float)",
        "create table if not exists bookingdetails(bid int primary key,cid int, checkin date, checkout date, finalprice float)",
        "create table if not exists employees(empid int primary key, aadhar char(20), ename char(50), age int, gender char(10), roleid int, sal float)",
        "create table if not exists roles(roleid int primary key, rolename char(50),sal float)"]
    for query in queries:
        cur.execute(query)
        print("OK ", query)


def addDefaultValues():
    queries = [
        "insert into customerdetails values(115,'669524138972','Rohit M S',20,'9358432100','#41, 1st Main, Marathahalli, Bangalore',1500,'2022-11-12','2022-11-13')",
        "insert into roles values(11,'Manager',95000)",
        "insert into employees values(31,'668574239817','Samuel Johnson',32,'Male',11,95000)",
        "insert into items values(1,'Chocolate Ice Cream',150)",
        "insert into roomtype values(1,2,'AC',2500,'Comfortable double room with AC, two single beds, a wardrobe and an outward facing window')",
        "insert into room values(188,1,268)",
        "insert into roomservice values(1768,1,3,115)",
        "insert into bookingdetails values(1327,115,'2022-11-12','2022-11-13',1950)"]
    for query in queries:
        cur.execute(query)
        con.commit()
        print("OK ", query)


def addForeignKeys():
    queries = [
        "alter table room add foreign key(roomtypeid) references roomtype(roomtypeid) on update cascade on delete cascade",
        "alter table roomservice add foreign key(itemid) references items(itemid) on update cascade on delete cascade",
        "alter table bookingdetails add foreign key(cid) references customerdetails(cid) on update cascade on delete cascade",
        "alter table employees add foreign key(roleid) references roles(roleid) on update cascade on delete cascade",
        "alter table roomservice add foreign key(rscid) references customerdetails(cid)"]
    for query in queries:
        cur.execute(query)
        con.commit()
        print("OK ", query)


def addCustDetails(aadhar, cname, cage, phone, caddress, finalprice, checkin, checkout):
    query = 'select cid from customerdetails order by cid desc limit 1'
    cur.execute(query)
    for row in cur:
        cid = int(row[0])
    cid += 10
    query = f"insert into customerdetails values({cid},{aadhar},'{cname}',{cage},{phone},'{caddress}',{finalprice},'{checkin}','{checkout}')"
    cur.execute(query)
    con.commit()
    return cid


def addEmployeeDetails(empid, aadhar, ename, age, gender, roleid):
    query = f'select sal from roles where roleid = {roleid}'
    cur.execute(query)
    for row in cur:
        sal = float(row[0])
    query = f"insert into employees values({empid},'{aadhar}','{ename}',{age},'{gender}',{roleid},{sal})"
    cur.execute(query)
    con.commit()


def addItem(itemid, itemname, itemrate):
    query = f"insert into items values({itemid},'{itemname}',{itemrate})"
    cur.execute(query)
    con.commit()


def addRole(roleid, rolename, rolesal):
    query = f"insert into roles values({roleid},'{rolename}',{rolesal})"
    cur.execute(query)
    con.commit()


def addRoomType(roomtypeid, bednum, ac, roomrate, desc):
    query = f"insert into roomtype values({roomtypeid},{bednum},'{ac}',{roomrate},'{desc}')"
    cur.execute(query)
    con.commit()


def addRoomService(itemid, quantity, rscid):
    query = 'select orderid from roomservice order by orderid desc limit 1'
    cur.execute(query)
    for row in cur:
        orderid = int(row[0])
    orderid += 10
    query = f"insert into roomservice values({orderid},{itemid},{quantity},{rscid})"
    cur.execute(query)
    con.commit()


def addRoom(roomnum, roomid, size):
    query = f"insert into room values({roomnum},{roomid},{size})"
    cur.execute(query)
    con.commit()


def addBookingDetails(cid, totalamt):
    query = 'select bid from bookingdetails order by bid desc limit 1'
    cur.execute(query)
    for row in cur:
        bid = int(row[0])
    bid += 10
    print(bid)
    query = f'select checkin from customerdetails where cid = {cid}'
    cur.execute(query)
    for row in cur:
        checkin = row[0]
    query = f'select checkout from customerdetails where cid = {cid}'
    cur.execute(query)
    for row in cur:
        checkout = row[0]
    query = f"insert into bookingdetails values({bid},{cid},'{checkin}','{checkout}',{totalamt})"
    cur.execute(query)
    con.commit()


def getFinalAmount(cid):
    query1 = f"select finalprice from customerdetails where cid={cid}"
    cur.execute(query1)
    for row1 in cur:
        p1 = float(row1[0])
    query2 = f"select sum(items.rate * roomservice.quantity) as total_price from roomservice join items on roomservice.itemid = items.itemid where roomservice.rscid = {cid}"
    cur.execute(query2)
    for row2 in cur:
        try:
            p2 = float(row2[0])
        except TypeError:
            p2 =0
        else:
            p2 = float(row2[0])
    return p1 + p2


def getRoomType(roomtypeid):
    query = f'select * from roomtype where roomtypeid={roomtypeid}'
    cur.execute(query)
    for row in cur:
        return row


def selectRoom(roomtypeid, checkin, checkout):
    query = f'select rate from roomtype where roomtypeid={roomtypeid}'
    cur.execute(query)
    for row in cur:
        rate = int(row[0])
    delta = checkout - checkin
    totalprice = rate * delta.days
    return totalprice


def getCustDetails(cid):
    query = f'select * from customerdetails where cid={cid}'
    cur.execute(query)
    for row in cur:
        return row


def getAllItems():
    query = pd.read_sql_query('select * from items', con)
    df = pd.DataFrame(query, columns=['itemid', 'itemname', 'rate'])
    return df


def getAllRoles():
    query = pd.read_sql_query('select * from roles', con)
    df = pd.DataFrame(query, columns=['roleid', 'rolename', 'sal'])
    return df


def getAllEmployees():
    query = pd.read_sql_query('select * from employees', con)
    df = pd.DataFrame(query, columns=['empid', 'ename', 'aadhar', 'age', 'gender', 'roleid', 'sal'])
    return df


def getAllRooms():
    query = pd.read_sql_query('select * from room', con)
    df = pd.DataFrame(query, columns=['roomnum', 'roomtypeid', 'size'])
    return df


def getAllRoomTypes():
    query = pd.read_sql_query('select * from roomtype', con)
    df = pd.DataFrame(query, columns=['roomtypeid', 'bednum', 'ac', 'rate', 'description'])
    return df


def getAllBookingDetails():
    query = pd.read_sql_query('select * from bookingdetails', con)
    df = pd.DataFrame(query, columns=['bid', 'cid', 'checkin', 'checkout', 'finalprice'])
    return df


def getAllCustomerDetails():
    query = pd.read_sql_query('select * from customerdetails', con)
    df = pd.DataFrame(query, columns=['cid', 'aadhar', 'cname', 'cage', 'phone', 'caddress', 'finalprice', 'checkin',
                                      'checkout'])
    return df


def getAllOrders():
    query = pd.read_sql_query('select * from roomservice', con)
    df = pd.DataFrame(query, columns=['orderid', 'itemid', 'quantity', 'rscid'])
    return df
