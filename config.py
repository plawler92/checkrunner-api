import os
import logging

class Config:
    checks_path = os.getenv("CHECKS_PATH", default="checks/")

    databases = {
        "ODSVault": os.getenv("DB_ODS_ODSVAULT", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ODSVault;UID=sa;PWD=Echo1234"),
        "ODSMartTracking": os.getenv("DB_ODS_ODSMARTTRACKING", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ODSMartTracking;UID=sa;PWD=Echo1234"),
        "ODSMartSourcing": os.getenv("DB_ODS_MARTSOURCING", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TestDB;UID=sa;PWD=Echo1234"),
        "ODSMartTLQuoting": os.getenv("DB_ODS_ODSMARTTLQUOTING", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ODSMartTLQuoting;UID=sa;PWD=Echo1234"),
        "ODSLog": os.getenv("DB_ODS_ODSLOG", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ODSLog;UID=sa;PWD=Echo1234"),
        "EchoOptimizer": os.getenv("DB_DB01_ECHOOPTIMIZER", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=EchoOptimizer;UID=sa;PWD=Echo1234"),
        "ODSIntegration": os.getenv("DB_DB01_ODSINTEGRATION", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=ODSIntegration;UID=sa;PWD=Echo1234"),
    }

    #10, 20, 30, 40
    LOG_LEVEL = os.getenv("LOG_LEVEL", default=logging.DEBUG)

# class LoggerConfig:
#     LOGGING_CONFIG = {
#         "version": 1,
#         "disable_existing_loggers": False,
#         "formatters" : {
#             "json": {
#                 "format": "%(timestamp)s %(level)s %(source)s %(functionName)s %(message)s %(requestProperties)s",
#                 "class": ""
#             }
#         }
#     }