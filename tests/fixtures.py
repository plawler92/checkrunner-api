import pytest

from checkrunner.core.exceptions import FactoryClassTypeNotFoundError
from checkrunner.core.check import Check

@pytest.fixture 
def create_yaml_func(name, suites):
    return {
        "checkName": name,
        "checkSuites": suites
    }

@pytest.fixture 
def basic_sqlserver_yaml():
    return {
        "checkName": "example-name",
        "checkSuites": ["example1, example2"],
        "checkType": {
            "type": "sqlserver",
            "database": "TestDB",
            "sql": "SELECT 'Fail'",
            "passValue": "Pass"
        }
    }

@pytest.fixture
def dummy_sql_server_executor():
    class DummySQLServerExecutor:
        def __init__(self, db):
            self.db = db
        
        def execute(self, check):
            return 'Pass'
    return DummySQLServerExecutor

@pytest.fixture 
def dummy_factory_class():
    class DummyFactoryClass:
        def create_check(self):
            return True
    return DummyFactoryClass

@pytest.fixture 
def dummy_check_factory():
    class DummyCheckFactory:
        def create_check(self, val):
            return True
    return DummyCheckFactory()

@pytest.fixture 
def factoryclassnotfound_check_factory():
    class FactoryClassNotFoundCheckFactory:
        def create_check(self, val):
            raise FactoryClassTypeNotFoundError()
    return FactoryClassNotFoundCheckFactory()

@pytest.fixture
def basic_sqlserver_check_factory():
    class BasicSqlServerCheckFactory:
        def __init__(self):
            self.counter = 0
        def create_check(self, val):
            self.counter = self.counter + 1
            return Check(
                str(self.counter),
                "sqlserver",
                "select 'pass'",
                "Pass",
                None,
                suites=["demo", "test"]
            )
    return BasicSqlServerCheckFactory()

@pytest.fixture
def dummy_yaml_manager():
    class DummyYamlManager:
        def get_yamls(self):
            return [True, True]
    return DummyYamlManager()