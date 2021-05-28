from checkrunner.check import Check
from checkrunner.executors.sql_server_executor import SQLServerExecutor
from checkrunner.check_factory import CheckFactory
from tests import config as cfg


def test_check_creation():
    sample_check = {
        "checkName": "three",
        "checkType": "sqlserver",
        "checkSuites": ["examples", "test"],
        "database": "TestDB", 
        "passValue": "Pass",
        "sql": "SELECT 'Pass'"
    }
    tf = CheckFactory(cfg.databases)
    test = tf.create_check(sample_check) 
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
    tf = CheckFactory(cfg.databases)
    test = tf.create_check(sample_check) 
    assert test.suites == []
    assert test.check_type == "sqlserver"
    assert isinstance(test.executor, SQLServerExecutor) == True