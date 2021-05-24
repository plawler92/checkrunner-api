
class CheckMemory:
    def __init__(self):
        self._checks = []

    def set_checks(self, checks):
        self._checks = checks

    def get_check_by_name(self, check_name):
        for c in self._checks:
            if c.check_name == check_name:
                return c
    
    def get_checks_by_type(self, check_type):
        return [x for x in self._checks if x.check_type == check_type]

    def get_checks_by_suite(self, check_suite):
        return [x for x in self._checks if check_suite in x.suites]