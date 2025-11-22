import sqlite3

connection=sqlite3.connect("student.db")
cursor = connection.cursor()

cmd = """
        CREATE TABLE IF NOT EXISTS student(
        fullname text not null,
        usn varchar(10) PRIMARY KEY,
        branch varchar(10) not null,
        email text not null,
        cgpa float not null
        )
        """

cursor.execute(cmd)
connection.commit()

cmd=" INSERT INTO student(fullname,usn,branch,email,cgpa)values(?,?,?,?,?)"
#cursor.execute(cmd,('Chaya','4mw23ad007','AIDS','shettychaya553@gmail.com','9.0'))
connection.commit()
f=cursor.execute("SELECT * FROM STUDENT").fetchall()
print(f)
r= cursor.execute("select * from student where fullname =?",('Chaya',)).fetchall()
print(r)
connection.close()


    
