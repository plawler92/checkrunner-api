from checkrunner.infra.executors import SQLServerExecutor
from checkrunner.core.factories import CheckFactory, SQLServerCheckFactory
from tests.config import Config

cfg = Config()

def create_check_factory():
    s = SQLServerCheckFactory(cfg.databases)
    cf = CheckFactory()
    cf.add_factory(s)
    return cf

def test_check_creation():
    sample_check = {
        "checkName": "three",
        "checkType": "sqlserver",
        "checkSuites": ["examples", "test"],
        "database": "TestDB", 
        "passValue": "Pass",
        "sql": "SELECT 'Pass'"
    }
    cf = create_check_factory()
    test = cf.create_check(sample_check) 

    assert test.suites == ["examples", "test"]
    assert test.check_type == "sqlserver"
    assert isinstance(test.executor, SQLServerExecutor) == True

def test_check_creation_no_suite():
    sample_check = {
        "checkName": "three",
        "checkType": "sqlserver",
        "database": "TestDB", 
        "passValue": "Pass",
        "sql": "SELECT 'Pass'"
    }
    cf = create_check_factory()
    test = cf.create_check(sample_check) 

    assert test.suites == []
    assert test.check_type == "sqlserver"
    assert isinstance(test.executor, SQLServerExecutor) == True