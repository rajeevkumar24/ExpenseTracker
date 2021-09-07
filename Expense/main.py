import db_functions
import mysql.connector as db

import Expense

connection = db.connect(
    host="localhost",
    user="root",
    passwd="ammuz$123",
    database="expensemanager"
)

is_db_initialised = db_functions.check_db_initialised(connection)
print(is_db_initialised)
if not is_db_initialised:
    queries = db_functions.get_initial_queries()
    status = db_functions.execute_queries(queries, connection)
    if status:
        print('DB INITIALISED SUCCESSFULLY')
    else:
        print('ERROR INITIALISING DB')

Expense.launch()
