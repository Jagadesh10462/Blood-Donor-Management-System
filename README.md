# Blood Donor Management System

A web-based Blood Donor Management System developed using **Python Flask, HTML, CSS, Bootstrap, and MySQL**.  
This project helps donors register their details and allows receivers to search for blood donors based on blood group.

---

## 📌 Features

- Donor Registration System
- Search Donors by Blood Group
- Store Donor Details in MySQL Database
- Responsive User Interface
- Blood Availability Display
- Simple and Easy-to-Use Web Application

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- Bootstrap
- MySQL

---

## 📂 Project Structure

```bash
Blood-Donor-Management-System/
│
├── backend.py
├── display.html
├── reg.html
├── receiver.html
├── informationtable.html
├── availability.html
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Blood-Donor-Management-System.git
```

---

### 2️⃣ Open Project Folder

```bash
cd Blood-Donor-Management-System
```

---

### 3️⃣ Install Required Libraries

```bash
pip install flask
pip install mysql-connector-python
```

---

### 4️⃣ Configure MySQL Database

Create a database in MySQL:

```sql
CREATE DATABASE teja;
```

Create table:

```sql
CREATE TABLE blooddonar (
    birthday VARCHAR(50),
    collegename VARCHAR(100),
    collegeid INT,
    collegearea VARCHAR(100),
    password VARCHAR(100),
    name VARCHAR(100),
    branch VARCHAR(100),
    age INT,
    collegecontactnumber BIGINT,
    bloodgroup VARCHAR(10)
);
```

---

### 5️⃣ Update Database Credentials

Open `backend.py` and modify:

```python
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='YOUR_PASSWORD',
    db='teja'
)
```

---

## ▶️ Run the Project

Run the Flask application:

```bash
python backend.py
```

OR

```bash
py backend.py
```

---

## 🌐 Open in Browser

After running the server, open:

```bash
http://127.0.0.1:5000/
```

---

## 📸 Project Modules

### 🩸 Donor Page
- Register donor details
- Add blood group and contact information

### 🩸 Receiver Page
- Search available donors by blood group

### 🩸 Availability Page
- Displays successful registration message

### 🩸 Information Table
- Shows matching donor records from database

---

## 🚀 Future Enhancements

- Login Authentication
- Admin Dashboard
- Email Notifications
- SMS Alerts
- Blood Request Tracking
- Cloud Deployment

---

## 📖 Learning Outcomes

This project helped in understanding:

- Flask Web Framework
- Database Connectivity
- CRUD Operations
- Frontend & Backend Integration
- Form Handling in Flask

---

## 👨‍💻 Author

**Naga Jagadesh Nambala**

---

## 📜 License

This project is developed for educational purposes.
