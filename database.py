import sqlite3

connection=sqlite3.connect("feedback.db")
cursor = connection.cursor()

cmd = """
        CREATE TABLE IF NOT EXISTS FEEDBACK(
        id integer primary key AUTOINCREMENT,
        fullname text not null,
        usn varchar(10) not null,
        contact varchar(10) not null,
        email text not null,
        message text not null
        )
        """

cursor.execute(cmd)
connection.commit()

cmd=" INSERT INTO FEEDBACK(fullname,usn,contact,email,message)values(?,?,?,?,?)"
cursor.execute(cmd,('Chaya','4mw23ad007','8765978888','shettychaya553@gmail.com','Good morning !'))
connection.commit()
f=cursor.execute("SELECT * FROM FEEDBACK").fetchall()
print(f)
connection.close()


    
