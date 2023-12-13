# database.py

import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Create Class table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Class (
        class_id INTEGER PRIMARY KEY,
        class_name TEXT NOT NULL
    )
''')

# Create Student table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Student (
        student_id INTEGER PRIMARY KEY,
        student_name TEXT NOT NULL,
        class_id INTEGER,
        FOREIGN KEY (class_id) REFERENCES Class(class_id)
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
