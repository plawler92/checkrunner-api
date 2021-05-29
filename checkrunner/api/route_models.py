
class CheckRequest:
    def __init__(self, check_name=None, check_suite=None, check_type=None):
        self.check_name = check_name
        self.check_suite = check_suite
        self.check_type = check_type

    def validate(self):
        errors = []
        if self.check_name == None and self.check_suite == None and self.check_type == None:
            errors.append("One of name, suite, or type needs to be not empty.")
        
        if errors == []:
            return (True, errors)
        else:
            return (False, errors)
