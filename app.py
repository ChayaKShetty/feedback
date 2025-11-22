from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')
@app.route('/submit',methods=['POST'])
def submit():
    fullname=request.form.get('fullname')
    usn=request.form.get('usn')
    contact=request.form.get('contact')
    email=request.form.get('email')
    message=request.form.get('message')
    connection=sqlite3.connect('feedback.db')
    cursor=connection.cursor()
    cursor.execute('INSERT INTO FEEDBACK(fullname,usn,contact,email,message)values(?,?,?,?,?)',(fullname,usn,contact,email,message))
    connection.commit()
    feedbacks=cursor.execute('select fullname,usn from FEEDBACK').fetchall()
    connection.close()
    return render_template('sucess.html',feedbacks=feedbacks,name=fullname)
    return feedbacks
    

if __name__ == '__main__':
    app.run(debug=True)