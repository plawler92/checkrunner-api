from checkrunner.check import Check
from checkrunner.executors import SQLServerExecutor
from tests import test_config as cfg

class ExampleExecutor:
    def __init__(self, pass_value):
        self.pass_value = pass_value

    def execute(self, check):
        return self.pass_value

def test_check_run():
    e = ExampleExecutor("PASS")
    c = Check("test-check", "sqlserver", "SELECT 'PASS'", "PASS", e)
    result = c.run_check()
    assert result.check_name == "test-check"
    assert result.check_type == "sqlserver"
    assert result.check_result == True