import re

class DateVerifier:
    def verify(self, user_input):
        match = re.match(r'^\d{4}-\d{2}-\d{2}$', user_input)
        if not match:
            print("Invalid date format. Please use the format YYYY-MM-DD.")
        return match

class TimeVerifier:
    def verify(self, user_input):
        match = re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', user_input)
        if not match:
            print("Invalid time format. Please use the format HH:MM.")
        return match

class OptionVerifier:
    def verify(self, user_input):
        if user_input not in ["1", "2"]:
            print("Invalid option. Please enter 1 or 2.")
            return False
        return True

class SearchOptionVerifier:
    def verify(self, user_input):
        if user_input not in map(str, range(1, 7)):
            print("Invalid option. Please enter a number between 1 and 6.")
            return False
        return True

class DefaultVerifier:
    def verify(self, user_input):
        print("Invalid input. Please try again.")
        return False

class InputVerifier(object):
    def __init__(self):
        self.user_input = ""
        self.data_type = ""

    def verify_input(self, user_input, data_type):
        self.user_input = user_input
        self.data_type = data_type

        verifier = self.get_verifier(data_type)
        return verifier.verify(self.user_input)

    def get_verifier(self, data_type):
        verifiers = {
            "date": DateVerifier(),
            "time": TimeVerifier(),
            "option": OptionVerifier(),
            "search_option": SearchOptionVerifier(),
        }
        return verifiers.get(data_type, DefaultVerifier())
