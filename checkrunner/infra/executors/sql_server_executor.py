import logging

import pyodbc

class SQLServerExecutor:
    def __init__(self, conn):
        self.conn = conn

    def execute(self, test):
        try:
            with pyodbc.connect(self.conn) as conn:
                cursor = conn.cursor()
                cursor.execute(test)
                return cursor.fetchone()[0]
        except pyodbc.OperationalError as e:
            logging.error(str(e))
            raise