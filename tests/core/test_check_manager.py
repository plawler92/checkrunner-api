from checkrunner.core.check import Check
from checkrunner.core.check_manager import CheckManager
from checkrunner.core.factories import CheckFactory, SQLServerCheckFactory
from checkrunner.core.check_memory import CheckMemory
from checkrunner.core.check import Check    
from tests.config import Config

cfg = Config()

class ExampleExecutor:
    def __init__(self, pass_value):
        self.pass_value = pass_value

    def execute(self, check):
        return self.pass_value

class TestYamlManager:
    def get_yamls(self):
        return [
            create_yaml("three", "sqlserver", None, "TestDB", "pass", "select 'pass'"),
            create_yaml("four", "sqlserver", None, "TestDB", "pass", "select 'pass'")
        ]
    
def create_yaml(check_name, check_type, check_suites, database, passValue, sql):
    return {
        "checkName": check_name,
        "checkType": check_type,
        "checkSuites": check_suites,
        "database": database,
        "passValue": passValue,
        "sql": sql
    }

def create_check_manager(check_factory=None, check_memory=None, yaml_manager=None):
    sf = SQLServerCheckFactory(cfg.databases)
    cf = check_factory or CheckFactory([sf])
    cmem = check_memory or CheckMemory()
    fm = yaml_manager or TestYamlManager()
    return CheckManager(cf, cmem, fm)

def test_refresh_checks():
    cm = create_check_manager()

    cm.refresh_checks()
    checks = cm.check_memory._checks
    check_result = checks[0]

    assert len(checks) == 2
    assert check_result.check_name == "three"
    assert check_result.check_type == "sqlserver"
    assert check_result.check.strip().lower() == "select 'pass'"
    assert check_result.check_pass_value.lower() == "pass"

def test_run_check_by_name():
    cmem = CheckMemory()
    cmem._checks = create_checks(3)

    cm = create_check_manager(check_memory=cmem)
    result = cm.run_check_by_name("0")

    assert result.successes == 1
    assert result.failures == 0
    assert result.check_results[0].check_name == "0"
    assert result.check_results[0].check_type == "sqlserver"
    assert result.check_results[0].check_result == True

def test_run_checks_by_type():
    cmem = CheckMemory()
    cmem._checks = create_checks(3)

    cm = create_check_manager(check_memory=cmem)
    result = cm.run_checks_by_type("sqlserver")

    assert result.successes == 3
    assert result.failures == 0
    
    for i, c in enumerate(result.check_results):
        assert c.check_name == str(i)
        assert c.check_type == "sqlserver"
        assert c.check_result == True

def test_run_checks_by_suite():
    cmem = CheckMemory()
    cmem._checks = create_checks(3)

    cm = create_check_manager(check_memory=cmem)
    results = cm.run_checks_by_suite("tests")

    assert results.successes == 2
    assert results.failures == 0
    assert len(results.check_results) == 2
    assert results.check_results[0].check_name == "0"
    assert results.check_results[0].check_type == "sqlserver"
    assert results.check_results[0].check_result == True
    
    assert results.check_results[1].check_name == "2"
    assert results.check_results[1].check_type == "sqlserver"
    assert results.check_results[1].check_result == True

def test_get_check_names():
    cmem = CheckMemory()
    cmem._checks = create_checks(2)

    cm = create_check_manager(check_memory=cmem)
    results = cm.get_check_names()

    assert len(results) == 2
    for i in range(2):
        assert results[i] == str(i)

def test_get_check_suites():
    cmem = CheckMemory()
    cmem._checks = create_checks(3)
    
    cm = create_check_manager(check_memory=cmem)
    results = cm.get_check_suites()

    assert len(results) == 2
    assert "tests" in results
    assert "hello" in results

def test_check_name_doesnt_exist():
    cmem = CheckMemory()
    cmem._checks = create_checks(3)

    cm = create_check_manager(check_memory=cmem)
    results = cm.run_check_by_name("asdlfkjasdlfkja")

    assert results.successes == 0
    assert results.failures == 0
    assert results.check_results == []


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