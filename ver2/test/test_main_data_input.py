from unittest.mock import patch
from io import StringIO
import sys
import os
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main

def clear_table(db_name, table_name):
    # Connect to the specified SQLite database
    connection = sqlite3.connect(db_name)

    try:
        cursor = connection.cursor()
        cursor.execute(f'DROP TABLE IF EXISTS {table_name}')
        connection.commit()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the connection
        connection.close()

@patch('builtins.input', side_effect=["1", "2023/10/31", "12:30", "am", "13:30", "pm", "Test Task", "Test Tag1",
                                      "1", "2023/10/31", "12:30", "am", "13:30", "pm", "Test Task", "Test Tag2",
                                      "1", "2023/10/31", "12:30", "am", "13:30", "pm", "Test Task", "Test Tag3",
                                      "1", "2023/11/31", "12:00", "am", "13:10", "pm", "Test Task2", "Test Tag1",
                                      "1", "2023/11/31", "12:00", "am", "13:10", "pm", "Test Task2", "Test Tag2",
                                      "1", "2023/11/31", "12:00", "am", "13:10", "pm", "Test Task2", "Test Tag3",
                                      "1", "2023/12/31", "12:10", "am", "13:00", "pm", "Test Task3", "Test Tag1",
                                      "1", "2023/12/31", "12:10", "am", "13:00", "pm", "Test Task3", "Test Tag2",
                                      "1", "2023/12/31", "12:10", "am", "13:00", "pm", "Test Task3", "Test Tag3",
                                      "1", "2023/01/31", "12:20", "am", "13:20", "pm", "Test Task1", "Test Tag1",
                                      "1", "2023/01/31", "12:20", "am", "13:20", "pm", "Test Task1", "Test Tag2",
                                      "1", "2023/01/31", "12:20", "am", "13:20", "pm", "Test Task1", "Test Tag3",
                                      "1", "2023/02/31", "12:40", "am", "13:40", "pm", "Test Task4", "Test Tag1",
                                      "1", "2023/02/31", "12:40", "am", "13:40", "pm", "Test Task4", "Test Tag2",
                                      "1", "2023/02/31", "12:40", "am", "13:40", "pm", "Test Task4", "Test Tag3"])


def test_main_data_input(mock_input):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        clear_table("tasks", "tasks")

        count = 0
        while count < 15:
            main()
            count += 1


        output = fake_out.getvalue().strip()

        expected_outputs = [
            "What would you like to do.",
            "Enter 1 to input information",
            "Enter 2 to search for information",
            "Enter 3 to run a report",
            "Data successfully inserted into the database."
        ]

        for expected_output in expected_outputs:
            assert expected_output in output, f"Expected '{expected_output}' to be printed, but got '{output}' instead."

