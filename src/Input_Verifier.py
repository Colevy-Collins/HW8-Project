import re

class Input_Verifier(object):
    
    def __init__(self):
        self.user_input = ""
        self.data_type = ""
        self.date = ""
        self.time = ""

    def verify_input(self, user_input, data_type):
        self.user_input = user_input
        self.data_type = data_type

        if self.data_type == "date":
            if not self.verify_date(self.user_input):
                print("Invalid date format. Please use the format YYYY-MM-DD.")
                return False

        elif self.data_type == "time":
            if not self.verify_time(self.user_input):
                print("Invalid time format. Please use the format HH:MM.")
                return False
        
        elif self.data_type == "option":
            if self.user_input not in ["1", "2"]:
                print("Invalid option. Please enter 1 or 2.")
                return False

        elif self.data_type == "search_option":
            if self.user_input not in [*map(str, range(1, 7))]:
                print("Invalid option. Please enter 1 or 2.")
                return False

        else:
            print("Invalid input. Please try again.")
            return False

        return True

    # Function to verify date format
    def verify_date(self, date):
        self.date = date
        return re.match(r'^\d{4}-\d{2}-\d{2}$', self.date)

    # Function to verify time format
    def verify_time(self, time):
        self.time = time
        return re.match(r'^([01]\d|2[0-3]):([0-5]\d)$', self.time)
