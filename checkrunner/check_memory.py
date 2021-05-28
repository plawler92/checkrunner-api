
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
        checks = [x for x in self._checks if x.check_type == check_type]
        return checks

    def get_checks_by_suite(self, check_suite):
        checks = [x for x in self._checks if check_suite in x.suites]
        return checks

    def get_check_names(self):
        names = [x.check_name for x in self._checks]
        return names

    def get_check_suites(self):
        check_suites = [suit for checks in self._checks for suit in checks.suites]
        suites = {s for s in check_suites}
        return suites