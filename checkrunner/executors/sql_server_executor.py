import pyodbc

class SQLServerExecutor:
    def __init__(self, conn):
        self.conn = conn

    def execute(self, test):
        with pyodbc.connect(self.conn) as conn:
            cursor = conn.cursor()
            cursor.execute(test)
            return cursor.fetchone()[0]
            


