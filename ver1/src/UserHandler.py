class UserHandler(object):

    def __init__(self, input_handler, search_handler, input_verifier):
        self.choice = ""
        self.input_handler = input_handler
        self.search_handler = search_handler
        self.input_verifier = input_verifier

    def take_choice(self):
        print("What would you like to do.")
        print("Enter 1 to input information")
        print("Enter 2 to search for information")
    
        while True:
            task_to_do = input("What do you want to, Enter your choice 1 - 2:")
            if self.input_verifier.verify_input(task_to_do, "option"):
                self.choice = task_to_do
                break

        self.provide_options()

    def provide_options(self):
        options = {
            "1": self.input_handler.take_task,
            "2": self.search_handler.take_task,
        }

        selected_option = options.get(self.choice)
        selected_option()