import re
from src.InputHandler import InputHandler

class SearchOption(InputHandler):
    def __init__(self):
        super().__init__()
        self.cursor = None
        self.to_search = []
        self.db_value_name = []

    def query_DB(self, to_search, db_value_names):
        self.to_search.extend(to_search)
        self.db_value_name.extend(db_value_names)
        if len(self.to_search) == 1:
            conditions = f"{self.db_value_name[0]} = ?"
        else:
            conditions = f"{self.db_value_name[0]} = ?"
            conditions += ''.join(f" AND {name} = ?" for name in self.db_value_name[1:])

        query = f'''
        SELECT * FROM tasks WHERE {conditions}
        '''

        self.cursor = self.db_controler.select(query, tuple(self.to_search))
        return self.cursor
    



class DateSearchOption(SearchOption):
    def search(self):
        search_date = input("Enter the date you want to search for (YYYY/MM/DD): ")
        while not self.input_verifier.verify_input(search_date, "date"):
            print("Invalid date format. Please use the format YYYY/MM/DD.")
            search_date = input("Enter the date you want to search for (YYYY/MM/DD): ")

        results = self.query_DB([search_date], ["date_of_task"])
        return results

class StartTimeSearchOption(SearchOption):
    def search(self):
        search_time = input(f"Enter the start time you want to search for (HH:MM): ")
        while not self.input_verifier.verify_input(search_time, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            search_time = input(f"Enter the start time you want to search for (HH:MM): ")

        am_or_pm = input(f"Enter am or pm for your time. If you entered millitary time, please type m: ")
        while am_or_pm.lower() != "am" and am_or_pm.lower() != "pm" and am_or_pm.lower() != "m":
            print("Invalid input. you must enter am, pm, or m")
            am_or_pm = input(f"Enter am or pm for your time. If you entered millitary time, please type m: ")

        search_time = self.input_verifier.convert_to_24_hour_format(search_time, am_or_pm)

        results = self.query_DB([search_time], ["start_time_of_task"])
        return results
        

class EndTimeSearchOption(SearchOption):
    def search(self):
        search_time = input(f"Enter the end time you want to search for (HH:MM): ")
        while not self.input_verifier.verify_input(search_time, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            search_time = input(f"Enter the end time you want to search for (HH:MM): ")

        am_or_pm = input(f"Enter am or pm for your time. If you entered millitary time, please type m: ")
        while am_or_pm.lower() != "am" and am_or_pm.lower() != "pm" and am_or_pm.lower() != "m":
            print("Invalid input. you must enter am, pm, or m")
            am_or_pm = input(f"Enter am or pm for your time. If you entered millitary time, please type m: ")      

        search_time = self.input_verifier.convert_to_24_hour_format(search_time, am_or_pm)  

        results = self.query_DB([search_time], ["end_time_of_task"])
        return results

class NameSearchOption(SearchOption):
    def search(self):
        search_task_name = input("Enter the task name you want to search for: ")

        results = self.query_DB([search_task_name], ["task_name"])
        return results

class TagSearchOption(SearchOption):
    def search(self):
        search_task_tag = input("Enter the task tag you want to search for: ")

        results = self.query_DB([search_task_tag], ["task_tag"])
        return results

class TimeRangeSearchOption(SearchOption):
    def search(self):
        search_start_time = input("Enter the start time you want to search for (HH:MM): ")
        while not self.input_verifier.verify_input(search_start_time, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            search_start_time = input("Enter the start time you want to search for (HH:MM): ")

        search_end_time = input("Enter the end time you want to search for (HH:MM): ")
        while not self.input_verifier.verify_input(search_end_time, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            search_end_time = input("Enter the end time you want to search for (HH:MM): ")

        results = self.query_DB([search_start_time, search_end_time], ["start_time_of_task","end_time_of_task"])
        return results


class SearchHandler(InputHandler):
    SEARCH_OPTIONS = {
        "1": DateSearchOption,
        "2": StartTimeSearchOption,
        "3": EndTimeSearchOption,
        "4": NameSearchOption,
        "5": TagSearchOption,
        "6": TimeRangeSearchOption,
    }

    def take_task(self, choice):
        task_to_do = choice

        search_option = self.SEARCH_OPTIONS.get(task_to_do)
        if search_option:
            search_handler = search_option()
            results = search_handler.search()
            return results
        else:
            print("Invalid option. Please enter a valid search option.")

        self.db_controler.close_connection()

        
