import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="password123")
mycursor =mydb.cursor()
mycursor.execute("Show Databases")
# mycursor.execute("Create Database studentdb")
for db in mycursor:
    print(db)

