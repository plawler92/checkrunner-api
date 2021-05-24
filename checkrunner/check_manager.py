from checkrunner.check import Check
from checkrunner.check_memory import CheckMemory
from checkrunner import file_util as futil

class CheckManager:
    def __init__(self, checks_path, check_factory):
        self.checks_path = checks_path
        self.check_memory = CheckMemory()
        self.check_factory = check_factory

    def refresh_checks(self):
        self.check_memory.set_checks([
            self.check_factory.create_check(futil.read_yaml(ya))
            for ya in futil.get_files(self.checks_path)
        ])

    def run_check_by_name(self, check_name):
        return self.check_memory.get_check_by_name(check_name).run_check()

    def run_checks_by_type(self, check_type):
        return [
            c.run_check()
            for c in self.check_memory.get_checks_by_type(check_type)
        ]

    def run_checks_by_suite(self, check_suite):
        return [
            c.run_check()
            for c in self.check_memory.get_checks_by_suite(check_suite)
        ]