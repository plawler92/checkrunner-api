from checkrunner.check import Check
from checkrunner.check_memory import CheckMemory
from checkrunner import file_util as futil
from checkrunner.check_suite import CheckSuite

class CheckManager:
    def __init__(self, checks_path, check_factory, check_memory):
        self.checks_path = checks_path
        self.check_memory = check_memory
        self.check_factory = check_factory

    def refresh_checks(self):
        checks = []
        files = futil.get_files(self.checks_path)
        for file in files:
            ya = futil.read_yaml(file)
            c = self.check_factory.create_check(ya)
            checks.append(c)
        self.check_memory.set_checks(checks)
        # self.check_memory.set_checks([
        #     self.check_factory.create_check(futil.read_yaml(ya))
        #     for ya in futil.get_files(self.checks_path)
        # ])

    def run_check_by_name(self, check_name):
        return CheckSuite(check_name, [self.check_memory.get_check_by_name(check_name).run_check()])        

    def run_checks_by_type(self, check_type):
        return CheckSuite(check_type, [
            c.run_check()
            for c in self.check_memory.get_checks_by_type(check_type)
        ])

    def run_checks_by_suite(self, check_suite):
        check_results = []
        checks = self.check_memory.get_checks_by_suite(check_suite)
        for c in checks:
            result = c.run_check()
            check_results.append(result)
        return CheckSuite(check_suite, check_results)
        # return [
        #     c.run_check()
        #     for c in self.check_memory.get_checks_by_suite(check_suite)
        # ]