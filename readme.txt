In tis project you will find a program designed to help manage time.
This project can take date related to date, time, and the task that was done.
This project can also search stored tasks based on values for each data field.
Finally, this project can generate 2 reports, one shows all tasks complete between 2 dates.
The other one shows total time spent on a task based on the tag field. 

In DBHandler.py you will find a class that handles CRUD operation with the database.

In InputHandler.py you will find an interface for classes that handle input.

In InputVerifier.py you will find several classes that verify that user input follows data input rules.

In SearchHandler.py you will find several classes that build and send search queries to DBHandler.

In StoreDatahandler.py you will find a class that handles the collection of input, creates a query and sends it to DBHandler.

In UserHandler.py you will find a class that takes user input and progress the program according to the input.
