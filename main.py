import sqlite3

from src.InputHandler import InputHandler
from src.InputVerifier import InputVerifier
from src.SearchHandler import SearchHandler
from src.UserHandler import UserHandler

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
    
    input_verifier = InputVerifier()
    input_handler = InputHandler(connection, input_verifier)
    search_handler = SearchHandler(connection, input_verifier)
    user_handler = UserHandler(input_handler, search_handler, input_verifier)

    user_handler.take_choice()

if __name__ == "__main__":
    main()
