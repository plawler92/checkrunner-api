import logging
from datetime import datetime

from checkrunner.core.check_result import CheckResult

class Check:
    def __init__(self, check_name, check_type, check, check_pass_value, executor, suites=[]):
        self.check_name = check_name
        self.check_type = check_type
        self.check = check
        self.check_pass_value = check_pass_value
        self.executor = executor
        self.suites = suites if suites else []

    def run_check(self):
        error_msg = None
        executor_output = None
        try:
            executor_output = self.executor.execute(self.check)
        except Exception as e:
            error_msg = str(e)
            executor_output = False
        finally:  
            return CheckResult(
                self.check_name,
                self.check_type,
                True if executor_output == self.check_pass_value else False,
                self.check,
                self.check_pass_value,
                datetime.now(), 
                error_msg
            )