from src.InputVerifier import InputVerifier
from src.DBHandler import DatabaseHandler

class InputHandler(object):
    def __init__(self):
        self.input_verifier = InputVerifier()
        self.db_controler = DatabaseHandler("tasks")
        
    def take_task(): pass



