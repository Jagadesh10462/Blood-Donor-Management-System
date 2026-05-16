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