from checkrunner.executors import SQLServerExecutor
import tests.config as cfg

def test_execute():
    test_sql = "SELECT 'PASS'"
    s = SQLServerExecutor(cfg.databases["TestDB"])
    result = s.execute(test_sql)
    assert result == "PASS"