import sqlite3
import re

# Function to verify date format
def verify_date(date):
    if re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        return True
    return False

# Function to verify time format
def verify_time(time):
    if re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', time):
        return True
    return False

# Create a new database or connect to an existing one
connection = sqlite3.connect('tasks.db')

# Create a table to store the tasks
connection.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date_of_task DATE,
    start_time_of_task TIME,
    end_time_of_task TIME,
    task_name TEXT,
    task_tag TEXT
)
''')

# Get user input and verify
date_of_task = input("Enter date (YYYY-MM-DD): ")
while not verify_date(date_of_task):
    print("Invalid date format. Please use the format YYYY-MM-DD.")
    date_of_task = input("Enter date (YYYY-MM-DD): ")

start_time_of_task = input("Enter start time (HH:MM): ")
while not verify_time(start_time_of_task):
    print("Invalid time format. Please use the format HH:MM.")
    start_time_of_task = input("Enter start time (HH:MM): ")

end_time_of_task = input("Enter end time (HH:MM): ")
while not verify_time(end_time_of_task):
    print("Invalid time format. Please use the format HH:MM.")
    end_time_of_task = input("Enter end time (HH:MM): ")
task_name = input("Enter task name: ")
task_tag = input("Enter task tag: ")

# Insert data into the table
connection.execute('''
INSERT INTO tasks (date, start_time, end_time, task_name, task_tag) VALUES (?, ?, ?, ?, ?)
''', (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag))

connection.commit()

print("Data successfully inserted into the database.")

connection.close()
