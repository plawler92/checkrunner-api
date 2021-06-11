from checkrunner.core.check import Check

class ExampleExecutor:
    def __init__(self, pass_value):
        self.pass_value = pass_value

    def execute(self, _):
        return self.pass_value

class ErrorExecutor:
    def execute(self, _):
        raise Exception("test exception")

def test_check_run():
    e = ExampleExecutor("PASS")
    c = Check("test-check", "sqlserver", "SELECT 'PASS'", "PASS", e)
    result = c.run_check()
    assert result.check_name == "test-check"
    assert result.check_type == "sqlserver"
    assert result.check_result == True
    assert result.error == None

def test_run_check_error():
    e = ErrorExecutor()
    c = Check("test-check", "sqlserver", "SELECT 'PASS'", "PASS", e)
    result = c.run_check()

    assert result.error == "test exception"
    assert result.check_result == False
