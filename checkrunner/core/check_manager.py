from checkrunner.core.check import Check
import logging

from checkrunner.core.check_results import CheckResults
from checkrunner.core.exceptions import FactoryClassTypeNotFoundError
from checkrunner.core.check_collection import CheckSuiteCollection

class CheckManager:
    def __init__(self, check_factory, yaml_manager, check_memory=None):
        self.check_factory = check_factory
        self.yaml_manager = yaml_manager
        self.check_memory = check_memory

    def get_check_suites(self):
        suites = CheckSuiteCollection()
        if self.check_memory:
            pass
        else:
            yamls = self.yaml_manager.get_yamls()
            checks = self.create_checks(yamls)
            suites.add_checks(checks)
        return suites

    def run_check_suite(self, suite_name):
        check_suite_collection = self.get_check_suites()
        checks = check_suite_collection.suites.get(suite_name)
        results = []
        for check in checks:
            results.append(check.run_check())
        return CheckResults(suite_name, results)

    def run_check_by_name(self, check_name):
        yamls = self.yaml_manager.get_yamls()
        checks = self.create_checks(yamls)
        results = []
        for check in checks:
            if check.check_name == check_name:
                results.append(check.run_check())
                break
        return CheckResults(check_name, results)

    def create_checks(self, yamls):
        checks = []
        for y in yamls:
            try:
                c = self.check_factory.create_check(y)
                if c: 
                    checks.append(c)
            except FactoryClassTypeNotFoundError as e:
                logging.warning(str(e))
        return checks
            


# class CheckManager:
#     def __init__(self, check_factory, check_memory, yaml_manager):
#         self.check_memory = check_memory
#         self.check_factory = check_factory
#         self.yaml_manager = yaml_manager

#     def refresh_checks(self):
#         checks = []
#         for y in self.yaml_manager.get_yamls():
#             c = self.check_factory.create_check(y)
#             if c:
#                 checks.append(c)
#         self.check_memory.set_checks(checks)

#     def run_check_by_name(self, check_name):
#         results = []
#         check = self.check_memory.get_check_by_name(check_name)
#         if check:
#             results.append(check.run_check())
#         return CheckResults(check_name, results)             

#     def run_checks_by_type(self, check_type):
#         return CheckResults(check_type, [
#             c.run_check()
#             for c in self.check_memory.get_checks_by_type(check_type)
#         ])

#     def run_checks_by_suite(self, check_suite):
#         check_results = []
#         checks = self.check_memory.get_checks_by_suite(check_suite)
#         for c in checks:
#             result = c.run_check()
#             check_results.append(result)
#         return CheckResults(check_suite, check_results)

#     def get_check_names(self):
#         return self.check_memory.get_check_names()

#     def get_check_suites(self):
#         return self.check_memory.get_check_suites()