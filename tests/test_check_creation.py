from checkrunner.check import Check
from checkrunner.executors.sql_server_executor import SQLServerExecutor
from checkrunner.check_factory import CheckFactory
from tests import test_config as cfg

def test_check_creation():
    sample_check = {
        "checkName": "three",
        "checkType": "sqlserver",
        "database": "TestDB", 
        "passValue": "Pass",
        "sql": "SELECT 'Pass'"
    }
    tf = CheckFactory(cfg.databases)
    test = tf.create_check(sample_check) 
    assert test.check_type == "sqlserver"
    assert isinstance(test.executor, SQLServerExecutor) == True

     