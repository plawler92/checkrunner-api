
class CheckResults:
    def __init__(self, name, check_results):
        self.name = name
        self.check_results = check_results
        self.successes = 0
        self.failures = 0
        for cr in check_results:
            if cr.check_result == True:
                self.successes += 1
            else:
                self.failures += 1

    def serialize(self):
        return {
            "name": self.name,
            "successes": self.successes,
            "failures": self.failures,
            "check_results": [cr.serialize() for cr in self.check_results]
        }