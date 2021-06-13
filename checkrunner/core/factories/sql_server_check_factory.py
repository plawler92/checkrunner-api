import logging

from checkrunner.infra.executors import SQLServerExecutor
from checkrunner.core.check import Check

class SQLServerCheckFactory:
    factory_type = "sqlserver"

    # this needs to be pass in an executor
    # executor factory?
    def __init__(self, databases, executor):
        self.databases = databases
        self.executor = executor

    def create_check(self, check_params):
        type_params = check_params.get("checkType")
        db = self.databases.get(type_params["database"])
        if db:
            return Check(
                check_name=check_params["checkName"],
                check_type=check_params["checkType"],
                check = type_params["sql"],
                check_pass_value = type_params["passValue"],
                executor = self.executor(db),
                suites=check_params.get("checkSuites")
            )
        else: 
            logging.warning(f"Tried to create Check with database {type_params['database']} but a matching connection string does not exist. Check will not be created.")
            return None
    