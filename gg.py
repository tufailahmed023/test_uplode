import mysql.connector as conn
mydp=conn.connect(host='localhost',user='root',passwd='tufailahmed023')
print(mydp)
cursor=mydp.cursor()
cursor.execute("show databases")
print(cursor.fetchall())
cursor.execute("use inuron ")

cursor.execute("show tables ")
print(cursor.fetchall())

cursor.execute("select * from bank_details where age> 35 limit 10")
for i in cursor.fetchall():
    print(i)


print("helo")
print("helo")
print("helo")
print("helo")
print("helo")