# application.py

from bottle import Bottle, request, template
import sqlite3

app = Bottle()

# Function to establish a database connection
def connect_db():
    return sqlite3.connect('school.db')

# Index route
@app.route('/')
def index():
    # Fetch data from Class and Student tables
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Class')
    classes = cursor.fetchall()

    cursor.execute('SELECT * FROM Student')
    students = cursor.fetchall()

    conn.close()

    # Render the template with the data
    return template('index', classes=classes, students=students)

# Edit a class
@app.route('/editClass/<class_id>', method='GET')
def edit_class(class_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Class WHERE class_id = ?', (class_id,))
    result = cursor.fetchone()
    conn.close()

    return template('edit_class', class_id=result[0], class_name=result[1])

# Update class information
@app.route('/updateClass/<class_id>', method='POST')
def update_class(class_id):
    new_class_name = request.forms.get('new_class_name')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Class SET class_name = ? WHERE class_id = ?', (new_class_name, class_id))
    conn.commit()
    conn.close()

    return index()

# Delete a class
@app.route('/deleteClass/<class_id>', method='GET')
def delete_class(class_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Class WHERE class_id = ?', (class_id,))
    conn.commit()
    conn.close()

    return index()

# Edit a student
@app.route('/editStudent/<student_id>', method='GET')
def edit_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Student WHERE student_id = ?', (student_id,))
    result = cursor.fetchone()
    conn.close()

    return template('edit_student', student_id=result[0], student_name=result[1], class_id=result[2])

# Update student information
@app.route('/updateStudent/<student_id>', method='POST')
def update_student(student_id):
    new_student_name = request.forms.get('new_student_name')
    new_class_id = request.forms.get('new_class_id')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('UPDATE Student SET student_name = ?, class_id = ? WHERE student_id = ?', (new_student_name, new_class_id, student_id))
    conn.commit()
    conn.close()

    return index()

# Delete a student
@app.route('/deleteStudent/<student_id>', method='GET')
def delete_student(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Student WHERE student_id = ?', (student_id,))
    conn.commit()
    conn.close()

    return index()

# Add a new class
@app.route('/addClass', method='POST')
def add_class():
    class_name = request.forms.get('class_name')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Class (class_name) VALUES (?)', (class_name,))
    conn.commit()
    conn.close()

    return index()

# Add a new student
@app.route('/addStudent', method='POST')
def add_student():
    student_name = request.forms.get('student_name')
    class_id = request.forms.get('class_id')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Student (student_name, class_id) VALUES (?, ?)', (student_name, class_id))
    conn.commit()
    conn.close()

    return index()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
