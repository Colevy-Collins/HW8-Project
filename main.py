import sqlite3
import re

def verify_input(user_input, data_type):
    if data_type == "date":
        if not verify_date(user_input):
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            return False

    elif data_type == "time":
        if not verify_time(user_input):
            print("Invalid time format. Please use the format HH:MM.")
            return False
    
    elif data_type == "option":
        if user_input not in ["1", "2"]:
            print("Invalid option. Please enter 1 or 2.")
            return False

    elif data_type == "search_option":
        if user_input not in [*map(str, range(1, 7))]:
            print("Invalid option. Please enter 1 or 2.")
            return False

    else:
        print("Invalid input. Please try again.")
        return False

    return True

# Function to verify date format
def verify_date(date):
    return re.match(r'^\d{4}-\d{2}-\d{2}$', date)

# Function to verify time format
def verify_time(time):
    return re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', time)

def search_and_print_results(cursor):
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
    
    while True:
        task_to_do = input("What do you want to, Enter your choice 1 - 2:")
        if verify_input(task_to_do, "option"):
            break

    # Get user input and verify
    if task_to_do == "1":
        date_of_task = input("Enter date (YYYY-MM-DD): ")
        while not verify_input(date_of_task, "date"):
            date_of_task = input("Enter date (YYYY-MM-DD): ")

        start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")
        while not verify_input(start_time_of_task, "time"):
            start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")

        end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")
        while not verify_input(end_time_of_task, "time"):
            end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")

        task_name = input("Enter task name: ")
        task_tag = input("Enter task tag: ")

        # Insert data into the table
        connection.execute('''
        INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag) VALUES (?, ?, ?, ?, ?)
        ''', (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag))

        connection.commit()

        print("Data successfully inserted into the database.")

    elif task_to_do == "2":
        cursor = ""

        print("What would you like to do.")
        print("Enter 1 to search for tasks on a date")
        print("Enter 2 to search for tasks that start at a certain time (in military time / 24 base)")
        print("Enter 3 to search for tasks that end at a certain time (in military time / 24 base)")
        print("Enter 4 to search for tasks with a certain name")
        print("Enter 5 to search for tasks with a certain tag")
        print("Enter 6 to search for tasks with a certain start and end time (in military time / 24 base)")
        
        while True:
            task_to_do = input("What do you want to do, Enter your choice 1 - 6:")
            if verify_input(task_to_do, "search_option"):
                break

        if task_to_do == "1":
            # Search the database based on user input
            search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")
            while not verify_input(search_date, "date"):
                print("Invalid date format. Please use the format YYYY-MM-DD.")
                search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")
            
            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE date_of_task = ?
            ''', (search_date,))
            search_and_print_results(cursor)
        
        elif task_to_do == "2":
            search_start_time = input("Enter the start time you want to search for (HH:MM): ")
            while not verify_input(search_start_time, "time"):
                print("Invalid time format. Please use the format HH:MM.")
                search_start_time = input("Enter the start time you want to search for (HH:MM): ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE start_time_of_task = ?
            ''', (search_start_time,))
            search_and_print_results(cursor)

        elif task_to_do == "3":
            search_end_time = input("Enter the end time you want to search for (HH:MM): ")
            while not verify_input(search_end_time, "time"):
                print("Invalid time format. Please use the format HH:MM.")
                search_end_time = input("Enter the end time you want to search for (HH:MM): ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE end_time_of_task = ?
            ''', (search_end_time,))
            search_and_print_results(cursor)

        elif task_to_do == "4":
            search_task_name = input("Enter the task name you want to search for: ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE task_name = ?
            ''', (search_task_name,))
            search_and_print_results(cursor)

        elif task_to_do == "5":
            search_task_tag = input("Enter the task tag you want to search for: ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE task_tag = ?
            ''', (search_task_tag,))
            search_and_print_results(cursor)

        elif task_to_do == "6":
            search_start_time = input("Enter the start time you want to search for (HH:MM): ")
            while not verify_input(search_start_time, "time"):
                print("Invalid time format. Please use the format HH:MM.")
                search_start_time = input("Enter the start time you want to search for (HH:MM): ")

            search_end_time = input("Enter the end time you want to search for (HH:MM): ")
            while not verify_input(search_end_time, "time"):
                print("Invalid time format. Please use the format HH:MM.")
                search_end_time = input("Enter the end time you want to search for (HH:MM): ")

            # Query the database based on the user input
            cursor = connection.execute('''
            SELECT * FROM tasks WHERE start_time_of_task = ? AND end_time_of_task = ?
            ''', (search_start_time, search_end_time))
            search_and_print_results(cursor)

    connection.close()

if __name__ == "__main__":
    main()
