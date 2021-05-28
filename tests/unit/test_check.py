from checkrunner.check import Check
from checkrunner.executors import SQLServerExecutor
from tests import config as cfg

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

# def test_check_eq():
#     c1 = Check("test-check", "sqlserver", "1", "1", None)
#     c2 = Check("test-check", "s", "2", "2", None)

#     assert c1 == c2

# def test_check_hash():
#     c1 = Check("test-check", "1", "1", "1", "1")
#     c2 = Check("test-check", "a", "a", "a", "a")

#     assert hash(c1) == hash(c2)