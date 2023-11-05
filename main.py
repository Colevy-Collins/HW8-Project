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

def main():

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

    print("What would you like to do.")
    print("Enter 1 to input information")
    print("Enter 2 to search for information")
    task_to_do = input("What do you want to, Enter your choice 1 - 2:")
    # Get user input and verify
    if(task_to_do == "1"):
        date_of_task = input("Enter date (YYYY-MM-DD): ")
        while not verify_date(date_of_task):
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            date_of_task = input("Enter date (YYYY-MM-DD): ")

        start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")
        while not verify_time(start_time_of_task):
            print("Invalid time format. Please use the format HH:MM.")
            start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")

        end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")
        while not verify_time(end_time_of_task):
            print("Invalid time format. Please use the format HH:MM.")
            end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")
        task_name = input("Enter task name: ")
        task_tag = input("Enter task tag: ")

        # Insert data into the table
        connection.execute('''
        INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag) VALUES (?, ?, ?, ?, ?)
        ''', (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag))

        connection.commit()

        print("Data successfully inserted into the database.")

        connection.close()
    elif(task_to_do == "2"):
        cursor = ""

        print("What would you like to do.")
        print("Enter 1 to search for tasks on a date")
        print("Enter 2 to search for tasks that start at a certain time (in military time / 24 base)")
        print("Enter 3 to search for tasks that end at a certain time (in military time / 24 base)")
        print("Enter 4 to search for tasks with a certain name")
        print("Enter 5 to search for tasks with a certain tag")
        print("Enter 6 to search for tasks with a certain start and end time (in military time / 24 base)")
        task_to_do = input("What do you want to do, Enter your choice 1 - 6:")

        if(task_to_do == "1"):
            # Search the database based on user input
            search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")
            while not verify_date(search_date):
                print("Invalid date format. Please use the format YYYY-MM-DD.")
                search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")
            
            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE date_of_task = ?
            ''', (search_date,))
        if(task_to_do == "2"):
            search_start_time = input("Enter the start time you want to search for (HH:MM): ")
            while not verify_time(search_start_time):
                print("Invalid time format. Please use the format HH:MM.")
                search_start_time = input("Enter the start time you want to search for (HH:MM): ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE start_time_of_task = ?
            ''', (search_start_time,))

        if(task_to_do == "3"):
            search_end_time = input("Enter the end time you want to search for (HH:MM): ")
            while not verify_time(search_end_time):
                print("Invalid time format. Please use the format HH:MM.")
                search_end_time = input("Enter the end time you want to search for (HH:MM): ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE end_time_of_task = ?
            ''', (search_end_time,))
        if(task_to_do == "4"):
            search_task_name = input("Enter the task name you want to search for: ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE task_name = ?
            ''', (search_task_name,))
        if(task_to_do == "5"):
            search_task_tag = input("Enter the task tag you want to search for: ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE task_tag = ?
            ''', (search_task_tag,))
        if(task_to_do == "6"):
            search_start_time = input("Enter the start time you want to search for (HH:MM): ")
            while not verify_time(search_start_time):
                print("Invalid time format. Please use the format HH:MM.")
                search_start_time = input("Enter the start time you want to search for (HH:MM): ")

            search_end_time = input("Enter the end time you want to search for (HH:MM): ")
            while not verify_time(search_end_time):
                print("Invalid time format. Please use the format HH:MM.")
                search_end_time = input("Enter the end time you want to search for (HH:MM): ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE start_time_of_task = ? AND end_time_of_task = ?
            ''', (search_start_time, search_end_time))


        # Fetch and print the search results
        search_results = cursor.fetchall()

        if search_results:
            print("Search Results:")
            for result in search_results:
                print("ID:", result[0])
                print("Date of Task:", result[1])
                print("Start Time of Task:", result[2])
                print("End Time of Task:", result[3])
                print("Task Name:", result[4])
                print("Task Tag:", result[5])
                print("------------------------------")
        else:
            print("No results found for the search criteria.")

        connection.close()
    else:
        print("invalid input, please try again")

if __name__ == "__main__":
    main()