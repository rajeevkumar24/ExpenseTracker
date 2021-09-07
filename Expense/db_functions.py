
def execute_queries(queries, connection):
    # execute sql queries
    status = False
    try:
        cursor = connection.cursor()
        for query in queries.keys():
            cursor.execute(queries[query])
            status = True
    except Exception as e:
        print(e)
    return status


def check_db_initialised(connection):
    # check db is initialised
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES')
    total_tables = 0
    for table in cursor:
        total_tables += 1
        if total_tables >= 1:
            return True
        else:
            return False


def get_initial_queries():
    # initial queries
    queries = {'create_budget': '''
        CREATE TABLE IF NOT EXISTS `expense` (
            `ItemId` INT AUTO_INCREMENT PRIMARY KEY,
            `date` datetime NOT NULL,
            `Payee` varchar(20) NOT NULL,
            `Type` varchar(20) NOT NULL,
            `Expense` decimal(20) NOT NULL
            
        );
        '''}
    return queries
