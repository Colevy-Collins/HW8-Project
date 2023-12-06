from unittest.mock import patch
from io import StringIO
import sys
import os
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main

@patch('builtins.input', side_effect=["2", "4", "nothing to be found"])

def test_main_search_task_name(mock_input):
    with patch('sys.stdout', new=StringIO()) as fake_out:

        main()


        output = fake_out.getvalue().strip()

        expected_outputs = [
            "What would you like to do.",
            "Enter 1 to input information",
            "Enter 2 to search for information",
            "Enter 1 to search for tasks on a date",
            "Enter 2 to search for tasks that start at a certain time",
            "Enter 3 to search for tasks that end at a certain time",
            "Enter 4 to search for tasks with a certain name",
            "Enter 5 to search for tasks with a certain tag",
            "Enter 6 to search for tasks with a certain start and end time",
            "No results found for the search criteria."
        ]


        for expected_output in expected_outputs:
            assert expected_output in output, f"Expected '{expected_output}' to be printed, but got '{output}' instead."
