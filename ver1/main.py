import sqlite3

from src.StoreDataHandler import StoreDataHandler
from src.InputVerifier import InputVerifier
from src.SearchHandler import SearchHandler
from src.UserHandler import UserHandler
from src.DBHandler import DatabaseHandler

def main():

    db_controler = DatabaseHandler("tasks")
    input_verifier = InputVerifier()
    store_data_hadler= StoreDataHandler(db_controler, input_verifier)
    search_handler = SearchHandler(db_controler, input_verifier)
    user_handler = UserHandler(store_data_hadler, search_handler, input_verifier)

    user_handler.take_choice()

if __name__ == "__main__":
    main()