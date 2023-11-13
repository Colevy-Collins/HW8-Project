import re

class SearchOption:
    def __init__(self, connection, input_verifier):
        self.connection = connection
        self.input_verifier = input_verifier
        self.cursor = None

    def search_and_print_results(self):
        # Fetch and print the search results
        search_results = self.cursor.fetchall()

        if search_results:
            print("Search Results:")
            for result in search_results:
                print("ID:", result[0])
                print("Date of Task:", result[1])
                print("Start Time of Task:", result[2])
                print("End Time of Task:", result[3])
                print("Task Name:", result[4])
                print("Task Tag:", result[5])
                print("------------------------------")
        else:
            print("No results found for the search criteria.")

class DateSearchOption(SearchOption):
    def search(self):
        search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")
        while not self.input_verifier.verify_input(search_date, "date"):
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            search_date = input("Enter the date you want to search for (YYYY-MM-DD): ")

        # Query the database based on the user input
        self.cursor = self.connection.execute('''
        SELECT * FROM tasks WHERE date_of_task = ?
        ''', (search_date,))
        self.search_and_print_results()

class StartTimeSearchOption(SearchOption):
    def search(self):
        search_time = input(f"Enter the start time you want to search for (HH:MM): ")
        while not self.input_verifier.verify_input(search_time, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            search_time = input(f"Enter the start time you want to search for (HH:MM): ")

        # Query the database based on the user input
        self.cursor = self.connection.execute(f'''
        SELECT * FROM tasks WHERE start_time_of_task = ?
        ''', (search_time,))
        self.search_and_print_results()

class EndTimeSearchOption(SearchOption):
    def search(self):
        search_time = input(f"Enter the end time you want to search for (HH:MM): ")
        while not self.input_verifier.verify_input(search_time, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            search_time = input(f"Enter the end time you want to search for (HH:MM): ")

        # Query the database based on the user input
        self.cursor = self.connection.execute(f'''
        SELECT * FROM tasks WHERE end_time_of_task = ?
        ''', (search_time,))
        self.search_and_print_results()

class NameSearchOption(SearchOption):
    def search(self):
        search_task_name = input("Enter the task name you want to search for: ")

        # Query the database based on the user input
        self.cursor = self.connection.execute('''
        SELECT * FROM tasks WHERE task_name = ?
        ''', (search_task_name,))
        self.search_and_print_results()

class TagSearchOption(SearchOption):
    def search(self):
        search_task_tag = input("Enter the task tag you want to search for: ")

        # Query the database based on the user input
        self.cursor = self.connection.execute('''
        SELECT * FROM tasks WHERE task_tag = ?
        ''', (search_task_tag,))
        self.search_and_print_results()

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

        # Query the database based on the user input
        self.cursor = self.connection.execute('''
        SELECT * FROM tasks WHERE start_time_of_task = ? AND end_time_of_task = ?
        ''', (search_start_time, search_end_time))
        self.search_and_print_results()

class SearchHandler(object):
    SEARCH_OPTIONS = {
        "1": DateSearchOption,
        "2": StartTimeSearchOption,
        "3": EndTimeSearchOption,
        "4": NameSearchOption,
        "5": TagSearchOption,
        "6": TimeRangeSearchOption,
    }

    def __init__(self, connection, input_verifier):
        self.connection = connection
        self.input_verifier = input_verifier

    def take_task(self):
        print("What would you like to do.")
        print("Enter 1 to search for tasks on a date")
        print("Enter 2 to search for tasks that start at a certain time (in military time / 24 base)")
        print("Enter 3 to search for tasks that end at a certain time (in military time / 24 base)")
        print("Enter 4 to search for tasks with a certain name")
        print("Enter 5 to search for tasks with a certain tag")
        print("Enter 6 to search for tasks with a certain start and end time (in military time / 24 base)")

        while True:
            task_to_do = input("What do you want to do, Enter your choice 1 - 6:")
            if self.input_verifier.verify_input(task_to_do, "search_option"):
                break

        search_option = self.SEARCH_OPTIONS.get(task_to_do)
        if search_option:
            search_handler = search_option(self.connection, self.input_verifier)
            search_handler.search()
        else:
            print("Invalid option. Please enter a valid search option.")

        self.connection.close()
