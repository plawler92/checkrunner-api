from checkrunner.core.factories import SQLServerCheckFactory
from checkrunner.infra.executors.sql_server_executor import SQLServerExecutor

def test_database_not_found(basic_sqlserver_yaml, dummy_sql_server_executor):
    dbs = {"asdfasdfasdf": "adsf"}
    s = SQLServerCheckFactory(dbs, dummy_sql_server_executor)
    c = s.create_check(basic_sqlserver_yaml)

    assert c == None

def test_check_creation(basic_sqlserver_yaml):
    dbs = {"TestDB": "asdf"}
    s = SQLServerCheckFactory(dbs, SQLServerExecutor)
    c = s.create_check(basic_sqlserver_yaml)

    assert c.check_name == basic_sqlserver_yaml["checkName"]
    assert c.suites == basic_sqlserver_yaml["checkSuites"]
    assert c.check == basic_sqlserver_yaml["checkType"]["sql"]
    assert c.check_pass_value == basic_sqlserver_yaml["checkType"]["passValue"]
    assert c.executor.conn == dbs["TestDB"]
    assert isinstance(c.executor, SQLServerExecutor)
    