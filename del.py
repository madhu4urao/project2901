import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="password123",database="studentdb")
mycursor=mydb.cursor()
sql ="DELETE FROM student WHERE name='Nikhila'"
mycursor.execute(sql)
mydb.commit()