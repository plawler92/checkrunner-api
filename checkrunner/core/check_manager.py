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

    def get_all_checks(self):
        yamls = self.yaml_manager.get_yamls()
        return self.create_checks(yamls)


    def get_check_suites(self):
        suites = CheckSuiteCollection()
        if self.check_memory:
            pass
        else:
            checks = self.get_all_checks()
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
        checks = self.get_all_checks()
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
