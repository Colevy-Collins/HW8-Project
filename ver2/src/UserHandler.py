from src.InputHandler import InputHandler

class UserHandler(InputHandler):

    def __init__(self, input_handler, search_handler, report_handler):
        super().__init__()
        self.choice = ""
        self.input_handler = input_handler
        self.search_handler = search_handler
        self.report_handler = report_handler

    def take_task(self):
        print("What would you like to do.")
        print("Enter 1 to input information")
        print("Enter 2 to search for information")
        print("Enter 3 to run a report")
    
        while True:
            task_to_do = input("What do you want to, Enter your choice 1 - 3:")
            if self.input_verifier.verify_input(task_to_do, "option"):
                self.choice = task_to_do
                break
            else:
                print("Invalid option. Please enter 1 - 3.")

        options = {
            "1": self.input_data,
            "2": self.search_for_data,
            "3": self.run_report
        }

        selected_option = options.get(self.choice)
        selected_option()

    def input_data(self):
        if self.input_handler.take_task():
            print("Data successfully inserted into the database.")
        else:
            print("There was an error, please try again.")
        
    def search_for_data(self):
        print("What would you like to do.")
        print("Enter 1 to search for tasks on a date")
        print("Enter 2 to search for tasks that start at a certain time")
        print("Enter 3 to search for tasks that end at a certain time")
        print("Enter 4 to search for tasks with a certain name")
        print("Enter 5 to search for tasks with a certain tag")
        print("Enter 6 to search for tasks with a certain start and end time")
        while True:
            task_to_do = input("What do you want to do, Enter your choice 1 - 6:")
            if self.input_verifier.verify_input(task_to_do, "search_option"):
                break
            else:
                print("Invalid option. Please enter a number between 1 and 6.")

        search_results = self.search_handler.take_task(task_to_do)

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

    def run_report(self):
        print("What would you like to do.")
        print("Enter 1 to run a Date Range report to see what task have been complete between two dates")
        print("Enter 2 to to run a Time Consumption report to see what task have the most time spent on them")

        while True:
            task_to_do = input("What do you want to do, Enter your choice 1 - 2:")
            if self.input_verifier.verify_input(task_to_do, "report_option"):
                break
            else:
                print("Invalid option. Please enter a number between 1 and 2.")

        report_results = self.report_handler.take_task(task_to_do)

        print(report_results)
        