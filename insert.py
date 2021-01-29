import mysql.connector as a
mydb =a.connect(host="localhost",user="root",passwd="password123",database="studentdb")
mycursor=mydb.cursor()
form="Insert into student(name,rno) values(%s,%s)"
students=[("Rohith",150),("Nikhila",192),("sahithi",202),]
mycursor.executemany(form, students)
mydb.commit()