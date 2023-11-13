import sqlite3

from src.Input_Handler import Input_Handler
from src.Input_Verifier import Input_Verifier
from src.Search_Handler import Search_Handler
from src.User_Handler import User_Handler

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
    
    input_verifier = Input_Verifier()
    input_handler = Input_Handler(connection, input_verifier)
    search_handler = Search_Handler(connection, input_verifier)
    user_handler = User_Handler(input_handler, search_handler, input_verifier)

    user_handler.take_choice()

if __name__ == "__main__":
    main()
