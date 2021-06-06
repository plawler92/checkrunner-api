import logging

from checkrunner.infra.executors import SQLServerExecutor
from checkrunner.core.check import Check

class SQLServerCheckFactory:
    factory_type = "sqlserver"

    def __init__(self, databases):
        self.databases = databases

    def create_check(self, check_params):
        db = self.databases.get(check_params["database"])
        if db:
            return Check(
                check_name=check_params["checkName"],
                check_type=check_params["checkType"],
                check = check_params["sql"],
                check_pass_value = check_params["passValue"],
                executor = SQLServerExecutor(self.databases[check_params["database"]]),
                suites=check_params.get("checkSuites")
            )
        else: 
            logging.warning(f"Tried to create Check with database {check_params['database']} but a matching connection string does not exist. Check will not be created.")
            return None
    