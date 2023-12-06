from src.InputHandler import InputHandler

class ReportOption(InputHandler):
    def __init__(self,  input_verifier):
        super().__init__()
        self.cursor = None
        self.to_search = []
        self.db_value_name = []
        self.report = ""
    
    def search(self):
        pass

class DateRangeReportOption(ReportOption):
    def search(self):
        start_date = input("Enter the start date you want to search for (YYYY/MM/DD): ")
        while not self.input_verifier.verify_input(start_date, "date"):
            print("Invalid date format. Please use the format YYYY/MM/DD.")
            start_date = input("Enter the start date you want to search for (YYYY/MM/DD): ")

        end_date = input("Enter the end date you want to search for (YYYY/MM/DD): ")
        while not self.input_verifier.verify_input(end_date, "date"):
            print("Invalid date format. Please use the format YYYY/MM/DD.")
            end_date = input("Enter the end date you want to search for (YYYY/MM/DD): ")

        query = '''SELECT * FROM tasks WHERE date_of_task BETWEEN ? AND ?'''

        self.cursor = self.db_controler.select(query, (start_date, end_date))
        
        rows = self.cursor

        if not rows:
            report = "No tasks found."
            return report
        else:
            table_header = "ID | Date       | Start Time | End Time   | Task Name    | Task Tag "
            header_divider = "\n" + ("-" * 75)
            table_contents = ""
            for row in rows:
                table_contents += "\n" + ("{:<3} | {:<10} | {:<10} | {:<10} | {:<12} | {:<10}".format(row[0], row[1], row[2], row[3], row[4], row[5]))

            report = table_header + header_divider + table_contents
            return report

class TimeConsumptionReportOption(ReportOption):
    def search(self):
        query = '''SELECT task_tag,
               SUM(strftime('%s', end_time_of_task) - strftime('%s', start_time_of_task)) AS total_duration
        FROM tasks
        GROUP BY task_tag
        ORDER BY total_duration DESC'''

        self.cursor = self.db_controler.select(query)

        rows = self.cursor

        if not rows:
            report = "No tasks found."
            return report
        else:
            table_header = "Task Tag | Total Duration (minutes)"
            header_divider = "\n" + ("-" * 40)
            table_contents = ""
            for row in rows:
                total_duration_minutes = abs(int(row[1]) // 60) # Convert total duration from seconds to minutes
                table_contents += "\n" + ("{:<8} | {:<23}".format(row[0], total_duration_minutes))
            
            report = table_header + header_divider + table_contents
            return report

class ReportHandler(InputHandler):
    REPORT_OPTIONS = {
        "1": DateRangeReportOption,
        "2": TimeConsumptionReportOption
    }

    def take_task(self, choice):
        task_to_do = choice

        report_option = self.REPORT_OPTIONS.get(task_to_do)
        if report_option:
            report_handler = report_option(self.input_verifier)
            results = report_handler.search()
            return results
        else:
            print("Invalid option. Please enter a valid search option.")

        self.db_controler.close_connection()
