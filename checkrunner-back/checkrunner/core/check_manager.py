from checkrunner.core.check_suite import CheckSuite

class CheckManager:
    def __init__(self, check_factory, check_memory, yaml_manager):
        self.check_memory = check_memory
        self.check_factory = check_factory
        self.yaml_manager = yaml_manager

    def refresh_checks(self):
        checks = []
        for y in self.yaml_manager.get_yamls():
            c = self.check_factory.create_check(y)
            if c:
                checks.append(c)
        self.check_memory.set_checks(checks)

    def run_check_by_name(self, check_name):
        results = []
        check = self.check_memory.get_check_by_name(check_name)
        if check:
            results.append(check.run_check())
        return CheckSuite(check_name, results)             

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

    def get_check_names(self):
        return self.check_memory.get_check_names()

    def get_check_suites(self):
        return self.check_memory.get_check_suites()