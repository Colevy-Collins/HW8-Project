class Input_Handler(object):

    def __init__(self, connection, input_verifier):
        self.date_of_task = ""
        self.start_time_of_task = ""
        self.end_time_of_task = ""
        self.task_name = ""
        self.task_tag = ""
        self.connection = connection
        self.input_verifier = input_verifier

    def take_task(self):
        self.date_of_task = input("Enter date (YYYY-MM-DD): ")
        while not self.input_verifier.verify_input(self.date_of_task, "date"):
            self.date_of_task = input("Enter date (YYYY-MM-DD): ")

        self.start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")
        while not self.input_verifier.verify_input(self.start_time_of_task, "time"):
            self.start_time_of_task = input("Enter start time in military time / 24 base (HH:MM): ")

        self.end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")
        while not self.input_verifier.verify_input(self.end_time_of_task, "time"):
            self.end_time_of_task = input("Enter end time in military time / 24 base (HH:MM): ")

        self.task_name = input("Enter task name: ")
        self.task_tag = input("Enter task tag: ")

        # Insert data into the table
        self.connection.execute('''
        INSERT INTO tasks (date_of_task, start_time_of_task, end_time_of_task, task_name, task_tag) VALUES (?, ?, ?, ?, ?)
        ''', (self.date_of_task, self.start_time_of_task, self.end_time_of_task, self.task_name, self.task_tag))

        self.connection.commit()

        print("Data successfully inserted into the database.")

