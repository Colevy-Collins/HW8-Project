from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from main import main


@patch('builtins.input', side_effect=["1", "2023-10-31", "12:30", "13:30", "Test Task", "Test Tag"])
def test_main(mock_input):
    with patch('sys.stdout', new=StringIO()) as fake_out:
        main()

        output = fake_out.getvalue().strip()

        expected_output_1 = "What would you like to do."
        expected_output_2 = "Enter 1 to input information"
        expected_output_3 = "Enter 2 to search for information"
        expected_output_4 = "Data successfully inserted into the database."

        assert expected_output_1 in output, f"Expected '{expected_output_1}' to be printed, but got '{output}' instead."
        assert expected_output_2 in output, f"Expected '{expected_output_2}' to be printed, but got '{output}' instead."
        assert expected_output_3 in output, f"Expected '{expected_output_3}' to be printed, but got '{output}' instead."
        assert expected_output_4 in output, f"Expected '{expected_output_4}' to be printed, but got '{output}' instead."
