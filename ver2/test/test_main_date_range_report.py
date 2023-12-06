from unittest.mock import patch
from io import StringIO
import sys
import os
import sqlite3
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main

@patch('builtins.input', side_effect=["3", "1", "2023/01/01", "2023/12/31"])

def test_main_search_date(mock_input):
    with patch('sys.stdout', new=StringIO()) as fake_out:

        main()


        output = fake_out.getvalue().strip()

        expected_outputs = [
            "What would you like to do.",
            "Enter 1 to input information",
            "Enter 2 to search for information",
            "Enter 3 to run a report",
            "Enter 1 to run a Date Range report to see what task have been complete between two dates",
            "Enter 2 to to run a Time Consumption report to see what task have the most time spent on them",
            "ID | Date       | Start Time | End Time   | Task Name    | Task Tag ",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
            "27",
            "28",
            "29",
            "30"            
        ]


        for expected_output in expected_outputs:
            assert expected_output in output, f"Expected '{expected_output}' to be printed, but got '{output}' instead."
