class CheckResult:
    def __init__(self, check_name, check_type, 
    check_result, check, check_pass_value, execution_time):
        self.check_name = check_name
        self.check_type = check_type
        self.check_result = check_result
        self.check = check
        self.check_pass_value = check_pass_value
        self.execution_time = execution_time

    def serialize(self):
        return {
            "check_name": self.check_name,
            "check_type": self.check_type,
            "check_result": self.check_result,
            "check": self.check,
            "check_pass_value": self.check_pass_value,
            "execution_time": str(self.execution_time)
        }
