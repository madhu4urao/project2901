import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="password123",database="studentdb")
mycursor=mydb.cursor()
sql ="Update student SET rno=150 WHERE name='Nikhila'"
mycursor.execute(sql)
mydb.commit()