from src.InputHandler import InputHandler

class StoreDataHandler(InputHandler):

    def __init__(self):
        super().__init__()
        self.date_of_task = ""
        self.start_time_of_task = ""
        self.end_time_of_task = ""
        self.task_name = ""
        self.task_tag = ""
        self.is_succeful = False

    def take_task(self):
        self.date_of_task = input("Enter date (YYYY-MM-DD): ")
        while not self.input_verifier.verify_input(self.date_of_task, "date"):
            print("Invalid time format. Please use the format HH:MM.")
            self.date_of_task = input("Enter date (YYYY-MM-DD): ")

        self.start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")
        while not self.input_verifier.verify_input(self.start_time_of_task, "time"):
            print("Invalid time format. Please use the format HH:MM.")
            self.start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")

        self.end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")
        while not self.input_verifier.verify_input(self.end_time_of_task, "time"):
            print("Invalid date format. Please use the format YYYY-MM-DD.")
            self.end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")

        self.task_name = input("Enter task name: ")
        self.task_tag = input("Enter task tag: ")

        query = 'INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag) VALUES (?, ?, ?, ?, ?)'
        parameters = (self.date_of_task, self.start_time_of_task, self.end_time_of_task, self.task_name, self.task_tag)
        # Insert data into the table
        
        if self.db_controler.execute_update(query, parameters):
             self.is_succeful = True
        
        return self.is_succeful

