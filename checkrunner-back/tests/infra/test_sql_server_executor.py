from checkrunner.infra.executors import SQLServerExecutor
from tests.config import Config

cfg = Config()

def test_execute():
    test_sql = "SELECT 'PASS'"
    s = SQLServerExecutor(cfg.databases["TestDB"])
    result = s.execute(test_sql)
    assert result == "PASS"