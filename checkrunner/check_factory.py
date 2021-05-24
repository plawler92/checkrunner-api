from checkrunner.executors import SQLServerExecutor
from checkrunner.check import Check

class CheckFactory:
    def __init__(self, databases):
        self.databases = databases

    def create_check(self, check_params):
        if check_params["checkType"] == "sqlserver":
            return Check(
                check_name=check_params["checkName"],
                check_type=check_params["checkType"],
                check = check_params["sql"],
                check_pass_value = check_params["passValue"],
                executor = SQLServerExecutor(self.databases[check_params["database"]])
            )