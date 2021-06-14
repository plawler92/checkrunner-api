import os
import logging

class Config:
    yaml_manager_type = os.getenv("YAML_MANAGER_TYPE", default="s3") # file, s3
    checks_path = os.getenv("CHECKS_PATH", default="newchecks/")
    s3_bucket = os.getenv("S3_BUCKET", default="echo-bi-datateam-dev")
    s3_folder = os.getenv("S3_FOLDER", default="checkrunner")
    aws_access_key = os.getenv("AWS_ACCESS_KEY", default="AKIA5BPDHQI65MKEB746")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY", default="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")
    aws_role_arn = os.getenv("AWS_ROLE_ARN", default="arn:aws:iam::896514097725:role/echo-sec-dev-bi-datateam-checkrunner-role")
    aws_external_id = os.getenv("AWS_EXTERNAL_ID", default="896514097725")

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

    LOG_LEVEL = os.getenv("LOG_LEVEL", default=logging.DEBUG)