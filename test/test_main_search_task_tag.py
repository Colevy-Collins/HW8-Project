from unittest.mock import patch
from io import StringIO
import sys
import os
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main

@patch('builtins.input', side_effect=["2", "5", "Test Tag2"])

def test_main_search_task_tag(mock_input):
    with patch('sys.stdout', new=StringIO()) as fake_out:

        main()


        output = fake_out.getvalue().strip()

        expected_outputs = [
            "What would you like to do.",
            "Enter 1 to input information",
            "Enter 2 to search for information",
            "Enter 1 to search for tasks on a date",
            "Enter 2 to search for tasks that start at a certain time (in military time / 24 base)",
            "Enter 3 to search for tasks that end at a certain time (in military time / 24 base)",
            "Enter 4 to search for tasks with a certain name",
            "Enter 5 to search for tasks with a certain tag",
            "Enter 6 to search for tasks with a certain start and end time (in military time / 24 base)",
            "Search Results",
            "Date of Task: 2023-10-31",
            "Start Time of Task: 12:30",
            "End Time of Task: 13:30",
            "Task Name: Test Task",
            "Task Tag: Test Tag2",
            "Date of Task: 2023-01-31",
            "Date of Task: 2023-02-31",
            "Date of Task: 2023-11-31",
            "Date of Task: 2023-12-31",
        ]


        for expected_output in expected_outputs:
            assert expected_output in output, f"Expected '{expected_output}' to be printed, but got '{output}' instead."
