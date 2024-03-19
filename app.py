from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)

# Database connection parameters
DB_NAME = 'my_database'
DB_USER = 'postgres'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_PORT = '5432'

# Function to establish a connection to the database
def connect_to_db():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    return conn

# Function to retrieve all students from the database
@app.route('/students', methods=['GET'])
def getAllStudents():
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return jsonify(rows)

# Function to add a new student to the database
@app.route('/students', methods=['POST'])
def addStudent():
    data = request.get_json()
    first_name = data['first_name']
    last_name = data['last_name']
    email = data['email']
    enrollment_date = data['enrollment_date']
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Student added successfully'})

# Function to update a student's email
@app.route('/students/<int:student_id>', methods=['PUT'])
def updateStudentEmail(student_id):
    data = request.get_json()
    new_email = data['email']
    
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Email updated successfully'})

# Function to delete a student from the database
@app.route('/students/<int:student_id>', methods=['DELETE'])
def deleteStudent(student_id):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'Student deleted successfully'})

if __name__ == "__main__":
    app.run(debug=True)