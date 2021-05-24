from checkrunner.check import Check
from checkrunner.check_manager import CheckManager
from checkrunner.check_factory import CheckFactory
from checkrunner.check_memory import CheckMemory
from checkrunner.check import Check
import tests.test_config as cfg

class ExampleExecutor:
    def __init__(self, pass_value):
        self.pass_value = pass_value

    def execute(self, check):
        return self.pass_value

def test_refresh_checks():
    cf = CheckFactory(cfg.databases)
    cm = CheckManager(cfg.checks_path, cf)
    cm.refresh_checks()
    checks = cm.check_memory._checks
    check_result = checks[0]
    assert len(checks) == 1
    assert check_result.check_name == "three"
    assert check_result.check_type == "sqlserver"
    assert check_result.check.strip().lower() == "select 'pass'"
    assert check_result.check_pass_value.lower() == "pass"

def test_run_check_by_name():
    cf = CheckFactory(cfg.databases)
    cm = CheckManager(cfg.checks_path, cf)
    cmem = CheckMemory()
    cmem._checks = create_checks(3)
    cm.check_memory = cmem

    result = cm.run_check_by_name("0")
    assert result.check_name == "0"
    assert result.check_type == "sqlserver"
    assert result.check_result == True

def test_run_checks_by_type():
    cf = CheckFactory(cfg.databases)
    cm = CheckManager(cfg.checks_path, cf)
    cmem = CheckMemory()
    cmem._checks = create_checks(3)
    cm.check_memory = cmem

    for i, c in enumerate(cm.run_checks_by_type("sqlserver")):
        assert c.check_name == str(i)
        assert c.check_type == "sqlserver"
        assert c.check_result == True

def test_run_checks_by_suite():
    cf = CheckFactory(cfg.databases)
    cm = CheckManager(cfg.checks_path, cf)
    cmem = CheckMemory()
    cmem._checks = create_checks(3)
    cm.check_memory = cmem

    results = cm.run_checks_by_suite("tests")
    assert len(results) == 2
    assert results[0].check_name == "0"
    assert results[0].check_type == "sqlserver"
    assert results[0].check_result == True
    
    assert results[1].check_name == "2"
    assert results[1].check_type == "sqlserver"
    assert results[1].check_result == True


def create_checks(num_checks):
    return [
        Check(
            str(i),
            "sqlserver",
            "SELECT 'Pass'",
            "Pass",
            ExampleExecutor("Pass"),
            suites=["tests" if i % 2 == 0 else "hello"]
        )
        for i in range(num_checks)
    ]