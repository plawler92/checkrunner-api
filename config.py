import os

class Config:
    checks_path = os.getenv("CHECKS_PATH", default="checks/")

    db_user = os.getenv("DB_USER", default="sa")
    db_password = os.getenv("DB_PASSWORD", default="Echo1234")
    server = os.getenv("SERVER", default="localhost")
    testdb = "DRIVER={ODBC Driver 17 for SQL Server};SERVER="+server+";DATABASE=TestDB;UID="+db_user+";PWD="+db_password
    databases = {
        "TestDB": testdb

    }