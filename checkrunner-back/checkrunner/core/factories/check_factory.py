from checkrunner.infra.executors import SQLServerExecutor
from checkrunner.core.check import Check

# class CheckFactory:
#     def __init__(self, databases):
#         self.databases = databases

#     def create_check(self, check_params):
#         if check_params["checkType"] == "sqlserver":
#             return Check(
#                 check_name=check_params["checkName"],
#                 check_type=check_params["checkType"],
#                 check = check_params["sql"],
#                 check_pass_value = check_params["passValue"],
#                 executor = SQLServerExecutor(self.databases[check_params["database"]]),
#                 suites=check_params.get("checkSuites")
#             )

class CheckFactory:
    def __init__(self, factory_classes=[]):
        self.factory_classes = factory_classes

    def add_factory(self, factory_class):
        self.factory_classes.append(factory_class)

    def create_check(self, check_params):
        for i in self.factory_classes:
            if i.factory_type == check_params["checkType"]:
                return i.create_check(check_params)