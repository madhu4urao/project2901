import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="password123",database="studentdb")
mycursor=mydb.cursor()
# mycursor.execute("Create table student(name varchar(200),rno int(10))")
mycursor.execute("show tables")
for tb in mycursor:
    print(tb)