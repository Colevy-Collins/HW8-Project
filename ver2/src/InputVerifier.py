import re
class Verifier(object):
    def __init__(self):
        self.is_valid_input = False

    def verify(self, user_input):
        pass

class DateVerifier(Verifier):
    def verify(self, user_input):
        match = re.match(r'^\d{4}/\d{2}/\d{2}$', user_input)
        return match

class TimeVerifier(Verifier):
    def verify(self, user_input):
        match = re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', user_input)
        return match

class OptionVerifier(Verifier):
    def verify(self, user_input):
        if user_input in ["1", "2", "3"]:
            self.is_valid_input = True
        return self.is_valid_input

class SearchOptionVerifier(Verifier):
    def verify(self, user_input):
        if user_input in map(str, range(1, 7)):
            self.is_valid_input = True
        return self.is_valid_input

class ReportOptionVerifier(Verifier):
    def verify(self, user_input):
        if user_input in map(str, range(1, 3)):
            self.is_valid_input = True
        return self.is_valid_input

class DefaultVerifier(Verifier):
    def verify(self, user_input):
        return self.is_valid_input 

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
            "report_option": ReportOptionVerifier(),
        }
        return verifiers.get(data_type, DefaultVerifier())
    
    def convert_to_24_hour_format(self, time_str, am_or_pm):
        # Split the time string into hours and minutes
        hours, minutes = map(int, time_str.split(':'))

        # Check if it's PM and hours are less than 12
        if am_or_pm.lower() == 'pm' and hours < 12:
            # Add 12 to the hours
            hours += 12

        # Format the result in HH:MM format
        new_time_str = '{:02d}:{:02d}'.format(hours % 24, minutes)

        return new_time_str
