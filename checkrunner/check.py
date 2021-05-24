from datetime import datetime

from checkrunner.check_result import CheckResult

class Check:
    def __init__(self, check_name, check_type, check, check_pass_value, executor, suites=None):
        self.check_name = check_name
        self.check_type = check_type
        self.check = check
        self.check_pass_value = check_pass_value
        self.executor = executor
        self.suites = suites

    def run_check(self):
        executor_output = self.executor.execute(self.check)
        return CheckResult(
            self.check_name,
            self.check_type,
            True if executor_output == self.check_pass_value else False,
            self.check,
            self.check_pass_value,
            datetime.now()
        )

