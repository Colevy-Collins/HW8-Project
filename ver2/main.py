import sqlite3

from src.StoreDataHandler import StoreDataHandler
from src.SearchHandler import SearchHandler
from src.UserHandler import UserHandler
from src.ReportHandler import ReportHandler

def main():

    report_handler = ReportHandler()
    store_data_handler= StoreDataHandler()
    search_handler = SearchHandler()
    user_handler = UserHandler(store_data_handler, search_handler, report_handler)

    user_handler.take_task()

if __name__ == "__main__":
    main()
