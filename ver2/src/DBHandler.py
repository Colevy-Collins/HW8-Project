from typing import Any
import sqlite3


class DatabaseHandler:

    def __init__(self, database_path="your_database_file.db"):
        self.database_path = database_path
        self.connection = None
        self.cursor = None
        default_table_query = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_of_task DATE,
            start_time_of_task TIME,
            end_time_of_task TIME,
            task_name TEXT,
            task_tag TEXT
        )
        '''
        self.execute_update(default_table_query)

    def connect(self):
        self.connection = sqlite3.connect(self.database_path)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def execute_update(self, query, parameters=None):
        try:
            self.connect()
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            self.connection.commit()
            return True  # Indicate success

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return False  # Indicate failure

        finally:
            self.close_connection()

    # CRUD operations
    def select(self, query, parameters=None):
        try:
            self.connect()
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            return self.cursor.fetchall()

        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            return None

        finally:
            self.close_connection()

    def insert(self, query, parameters=None):
        return self.execute_update(query, parameters)
