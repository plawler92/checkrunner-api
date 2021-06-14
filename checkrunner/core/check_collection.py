from collections import defaultdict

from checkrunner.core.check import Check

class CheckSuiteCollection:
    def __init__(self):
        self.suites = defaultdict(list)

    def add_checks(self, checks):
        for check in checks:
            for suite in check.suites:
                if check.check_name not in self.suites[suite]:
                    self.suites[suite].append(check)
