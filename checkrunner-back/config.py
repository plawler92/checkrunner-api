import os
import logging

class Config:
    checks_path = os.getenv("CHECKS_PATH", default="checks/")
    s3_bucket = os.getenv("S3_BUCKET", default="checkrunner-yamls")
    aws_access_key = os.getenv("AWS_ACCESS_KEY", default="AKIAYI22PJTYNIMGGWN7")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", default="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")

    databases = {
        "TestDB": os.getenv("TestDB", default="DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=TestDB;UID=sa;PWD=Echo1234"),
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