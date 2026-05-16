<<<<<<< HEAD
from flask import *
import mysql.connector
import os

connection = mysql.connector.connect(
    host=os.environ.get('DB_HOST'),
    port=int(os.environ.get('DB_PORT')),
    user=os.environ.get('DB_USER'),
    password=os.environ.get('DB_PASSWORD'),
    database=os.environ.get('DB_NAME')
)


cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS blooddonar (
        birthday VARCHAR(20),
        collegename VARCHAR(100),
        collegeid INT,
        collegearea VARCHAR(100),
        password VARCHAR(100),
        name VARCHAR(100),
        branch VARCHAR(100),
        age INT,
        collegecontactnumber BIGINT,
        bloodgroup VARCHAR(5)
    )
""")
connection.commit()

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template("display.html")

@app.route("/donar")
def registration_page():
    return render_template("reg.html")

@app.route("/receiver")
def receiver_page():
    return render_template("receiver.html")

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    try:
        birthday = request.form.get("birthdate")
        collegename = request.form.get("collegename")
        collegeid = int(request.form.get("collegeid"))
        collegearea = request.form.get("collegearea")
        password = request.form.get("password")
        name = request.form.get("name")
        branch = request.form.get("branch")
        bloodgroup = request.form.get("bloodgroup")
        age = int(request.form.get("age"))
        collegecontactnumber = int(request.form.get("collegecontactnumber"))

        cursor.execute("""
            INSERT INTO blooddonar VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """, (birthday, collegename, collegeid, collegearea, password, name, branch, age, collegecontactnumber, bloodgroup))
        connection.commit()

        return render_template("availability.html")
    except Exception as e:
        return str(e)

@app.route('/processdata', methods=['GET', 'POST'])
def display_table():
    bloodgroup = request.form.get("bloodgroup")
    cursor.execute("SELECT * FROM blooddonar WHERE bloodgroup = %s", (bloodgroup,))
    data = cursor.fetchall()
    return render_template('informationtable.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
=======
from flask import *
import mysql.connector
connection = mysql.connector.connect(
host='localhost',
user='root',
password='VSLYFTP143',
db='teja'
)
cursor = connection.cursor()
app=Flask(__name__)
@app.route("/")
def home_page():
    return render_template("display.html")
@app.route("/donar")
def registration_page():
    return render_template("reg.html")
@app.route("/receiver")
def receiver_page():
    return render_template("receiver.html")
@app.route("/submit",methods=['GET','POST'])
def submit():
    print('entered')
    try:

        birthday=request.form.get("birthdate")
        collegename=request.form.get("collegename")
        collegeid=int(request.form.get("collegeid"))
        collegearea=request.form.get("collegearea")
        password=request.form.get("password")
        name=request.form.get("name")
        branch=request.form.get("branch")
        bloodgroup=request.form.get("bloodgroup")
        print("bloodgrooup=",bloodgroup,type(bloodgroup))
        age=int(request.form.get("age"))
        collegecontactnumber=int(request.form.get("collegecontactnumber"))
        print(birthday,collegename,collegeid,collegearea,password,name,branch)
        cursor.execute(f"INSERT INTO blooddonar VALUES ('{birthday}','{collegename}',{collegeid},'{collegearea}','{password}','{name}','{branch}',{age},{collegecontactnumber},'{bloodgroup}' )")
        connection.commit()
        print('registered')
        return render_template("availability.html")
    except Exception as e:
        print(" failed")
        return(str(e))
@app.route('/processdata',methods=['GET','POST'])
def display_table():
    bloodgroup=request.form.get("bloodgroup")
    print(bloodgroup,type(bloodgroup))
    #session['bloodgroup'] = bloodgroup
    cursor.execute("SELECT * FROM blooddonar WHERE bloodgroup = %s", (bloodgroup,))

    data = cursor.fetchall()
    return render_template('informationtable.html', data=data)

if __name__=='__main__':
    app.run(debug=True)
>>>>>>> d7659c3fe5c407d6f7d5a11b532b3f72ba6c06d5
