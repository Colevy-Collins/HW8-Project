from unittest.mock import patch
from io import StringIO
import sys
import os
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main
def drop_tasks_table():
    try:
        # Connect to SQLite database (or create a new one if it doesn't exist)
        conn = sqlite3.connect('tasks')
        cursor = conn.cursor()

        # Execute SQL command to drop the tasks table
        cursor.execute('DROP TABLE IF EXISTS tasks')

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        print("Tasks table dropped successfully.")
    except Exception as e:
        print("Error dropping tasks table:", e)


@patch('builtins.input', side_effect=["1", "2023-10-31", "12:30", "13:30", "Test Task", "Test Tag1",
                                      "1", "2023-10-31", "12:30", "13:30", "Test Task", "Test Tag2",
                                      "1", "2023-10-31", "12:30", "13:30", "Test Task", "Test Tag3",
                                      "1", "2023-11-31", "12:00", "13:10", "Test Task2", "Test Tag1",
                                      "1", "2023-11-31", "12:00", "13:10", "Test Task2", "Test Tag2",
                                      "1", "2023-11-31", "12:00", "13:10", "Test Task2", "Test Tag3",
                                      "1", "2023-12-31", "12:10", "13:00", "Test Task3", "Test Tag1",
                                      "1", "2023-12-31", "12:10", "13:00", "Test Task3", "Test Tag2",
                                      "1", "2023-12-31", "12:10", "13:00", "Test Task3", "Test Tag3",
                                      "1", "2023-01-31", "12:20", "13:20", "Test Task1", "Test Tag1",
                                      "1", "2023-01-31", "12:20", "13:20", "Test Task1", "Test Tag2",
                                      "1", "2023-01-31", "12:20", "13:20", "Test Task1", "Test Tag3",
                                      "1", "2023-02-31", "12:40", "13:40", "Test Task4", "Test Tag1",
                                      "1", "2023-02-31", "12:40", "13:40", "Test Task4", "Test Tag2",
                                      "1", "2023-02-31", "12:40", "13:40", "Test Task4", "Test Tag3", "3", "2"])

def test_main_search_date(mock_input):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        drop_tasks_table()

        count = 0
        while count < 16:
            main()
            count += 1


        output = fake_out.getvalue().strip()

        expected_outputs = [
            "What would you like to do.",
            "Enter 1 to input information",
            "Enter 2 to search for information",
            "Enter 3 to run a report",
            "Enter 1 to run a Date Range report to see what task have been complete between two dates",
            "Enter 2 to to run a Time Consumption report to see what task have the most time spent on them",
            "Task Tag | Total Duration (minutes)",
            "Test Tag3",
            "Test Tag2",
            "Test Tag1",
            "300"
        ]


        for expected_output in expected_outputs:
            assert expected_output in output, f"Expected '{expected_output}' to be printed, but got '{output}' instead."



