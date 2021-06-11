import pytest

from checkrunner.core.check import Check
from checkrunner.core.check_manager import CheckManager
from checkrunner.core.factories import CheckFactory, SQLServerCheckFactory, check_factory
from checkrunner.core.check_memory import CheckMemory
from checkrunner.core.check import Check    
from tests.config import Config

cfg = Config()

class ExampleExecutor:
    def __init__(self, pass_value):
        self.pass_value = pass_value

    def execute(self, check):
        return self.pass_value

class ExampleSQLServerCheckFactory:
    def __init__(self, databases):
        self.databases = databases

    def create_check(self, check_params):
        db = self.databases.get(check_params["database"])
        if db:
            return Check(
                check_name=check_params["checkName"],
                check_type=check_params["checkType"],
                check = check_params["sql"],
                check_pass_value = check_params["passValue"],
                executor = ExampleExecutor("pass"),
                suites=check_params.get("checkSuites")
            )
        else: 
            logging.warning(f"Tried to create Check with database {check_params['database']} but a matching connection string does not exist. Check will not be created.")
            return None

class TestYamlManager:
    def get_yamls(self):
        return [
            create_yaml("three", "sqlserver", ["demo", "hello"], "TestDB", "pass", "select 'pass'"),
            create_yaml("four", "sqlserver", ["demo"], "TestDB", "pass", "select 'pass'")
        ]

class EmptySuiteYamlManager:
    def get_yamls(self):
        return [
            create_yaml("three", "sqlserver", None, "TestDB", "pass", "select 'pass'"),
            create_yaml("four", "sqlserver", None, "TestDB", "pass", "select 'pass'")
        ]

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
    
def create_yaml(check_name, check_type, check_suites, database, passValue, sql):
    return {
        "checkName": check_name,
        "checkType": check_type,
        "checkSuites": check_suites,
        "database": database,
        "passValue": passValue,
        "sql": sql
    }

@pytest.fixture
def basic_yamls():
    return [
        create_yaml("three", "sqlserver", None, "TestDB", "pass", "select 'pass'"),
        create_yaml("four", "sqlserver", None, "TestDB", "pass", "select 'pass'")
    ]

@pytest.fixture 
def wrong_type_yamls():
    return [
        create_yaml("three", "???", None, "TestDB", "pass", "select 'pass'"),
        create_yaml("four", "???", None, "TestDB", "pass", "select 'pass'")
    ]

@pytest.fixture
def basic_yaml_manager():
    return TestYamlManager()

@pytest.fixture
def empty_suite_yaml_manager():
    return EmptySuiteYamlManager()
    
# @pytest.fixture
# def basic_sql_server_check_factory():
#     #return SQLServerCheckFactory(cfg.databases)
#     return 

@pytest.fixture 
def basic_mock_check_factory():
    return ExampleSQLServerCheckFactory(cfg.databases)

@pytest.fixture
def basic_check_factory(basic_mock_check_factory):
    cf = CheckFactory()
    cf.add_factory("sqlserver", basic_mock_check_factory)
    return cf

@pytest.fixture
def basic_check_manager(basic_check_factory, basic_yaml_manager):
    return CheckManager(
        check_factory=basic_check_factory,
        yaml_manager=basic_yaml_manager
    )

@pytest.fixture
def empty_suite_check_manager(basic_check_factory, empty_suite_yaml_manager):
    return CheckManager(
        check_factory=basic_check_factory,
        yaml_manager=empty_suite_yaml_manager
    )

def test_create_checks(basic_check_manager, basic_yamls):
    checks = basic_check_manager.create_checks(basic_yamls)

    assert len(checks) == 2

    assert_check_equality(checks[0], "three", "sqlserver")
    assert_check_equality(checks[1], "four", "sqlserver")

def test_create_checks_no_matching_factory(basic_check_manager, wrong_type_yamls):
    checks = basic_check_manager.create_checks(wrong_type_yamls)
    
    assert checks == []

def test_create_checks_no_yamls(basic_check_manager):
    checks = basic_check_manager.create_checks([])

    assert checks == []

def test_get_check_suites_no_files(empty_suite_check_manager):
    suite_collection = empty_suite_check_manager.get_check_suites()
    suites = suite_collection.suites

    assert False == bool(suites)

def test_get_check_suites(basic_check_manager):
    suite_collection = basic_check_manager.get_check_suites()
    suites = suite_collection.suites

    assert "demo" in suites
    assert "hello" in suites
    

def assert_check_equality(check, exp_name, exp_type):
    assert check.check_name == exp_name
    assert check.check_type == exp_type

def test_run_checks_by_suite(basic_check_manager):
    results = basic_check_manager.run_check_suite("demo")

    assert results.successes == 2
    assert results.failures == 0
    assert len(results.check_results) == 2
    assert_check_equality(results.check_results[0], "three", "sqlserver")
    assert_check_equality(results.check_results[1], "four", "sqlserver")

def test_run_checks_by_name(basic_check_manager):
    results = basic_check_manager.run_check_by_name("three")

    assert results.successes == 1
    assert results.failures == 0
    assert len(results.check_results) == 1
    assert_check_equality(results.check_results[0], "three", "sqlserver")



# def create_check_manager(check_factory=None, check_memory=None, yaml_manager=None):
#     sf = SQLServerCheckFactory(cfg.databases)
#     cf = check_factory or CheckFactory()
#     if check_factory is None:
#         cf.add_factory(sf.factory_type, sf)
#     cmem = check_memory or CheckMemory()
#     fm = yaml_manager or TestYamlManager()
#     return CheckManager(cf, cmem, fm)    

# def test_refresh_checks():
#     cm = create_check_manager()

#     cm.refresh_checks()
#     checks = cm.check_memory._checks
#     check_result = checks[0]

#     assert len(checks) == 2
#     assert check_result.check_name == "three"
#     assert check_result.check_type == "sqlserver"
#     assert check_result.check.strip().lower() == "select 'pass'"
#     assert check_result.check_pass_value.lower() == "pass"

# def test_refresh_checks_no_none():
#     sf = SQLServerCheckFactory({"No": "no"})
#     cf = CheckFactory()
#     cf.add_factory(sf.factory_type, sf)
#     cm = create_check_manager(check_factory=cf)

#     cm.refresh_checks()
#     checks = cm.check_memory._checks
    
#     assert checks == []

# def test_run_check_by_name():
#     cmem = CheckMemory()
#     cmem._checks = create_checks(3)

#     cm = create_check_manager(check_memory=cmem)
#     result = cm.run_check_by_name("0")

#     assert result.successes == 1
#     assert result.failures == 0
#     assert result.check_results[0].check_name == "0"
#     assert result.check_results[0].check_type == "sqlserver"
#     assert result.check_results[0].check_result == True

# def test_run_checks_by_type():
#     cmem = CheckMemory()
#     cmem._checks = create_checks(3)

#     cm = create_check_manager(check_memory=cmem)
#     result = cm.run_checks_by_type("sqlserver")

#     assert result.successes == 3
#     assert result.failures == 0
    
#     for i, c in enumerate(result.check_results):
#         assert c.check_name == str(i)
#         assert c.check_type == "sqlserver"
#         assert c.check_result == True

# def test_run_checks_by_suite():
#     cmem = CheckMemory()
#     cmem._checks = create_checks(3)

#     cm = create_check_manager(check_memory=cmem)
#     results = cm.run_checks_by_suite("tests")

#     assert results.successes == 2
#     assert results.failures == 0
#     assert len(results.check_results) == 2
#     assert results.check_results[0].check_name == "0"
#     assert results.check_results[0].check_type == "sqlserver"
#     assert results.check_results[0].check_result == True
    
#     assert results.check_results[1].check_name == "2"
#     assert results.check_results[1].check_type == "sqlserver"
#     assert results.check_results[1].check_result == True

# def test_get_check_names():
#     cmem = CheckMemory()
#     cmem._checks = create_checks(2)

#     cm = create_check_manager(check_memory=cmem)
#     results = cm.get_check_names()

#     assert len(results) == 2
#     for i in range(2):
#         assert results[i] == str(i)

# def test_get_check_suites():
#     cmem = CheckMemory()
#     cmem._checks = create_checks(3)
    
#     cm = create_check_manager(check_memory=cmem)
#     results = cm.get_check_suites()

#     assert len(results) == 2
#     assert "tests" in results
#     assert "hello" in results

# def test_check_name_doesnt_exist():
#     cmem = CheckMemory()
#     cmem._checks = create_checks(3)

#     cm = create_check_manager(check_memory=cmem)
#     results = cm.run_check_by_name("asdlfkjasdlfkja")

#     assert results.successes == 0
#     assert results.failures == 0
#     assert results.check_results == []

