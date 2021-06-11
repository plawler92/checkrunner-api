import pytest

from checkrunner.core.check_collection import CheckSuiteCollection
from checkrunner.core.check import Check

@pytest.fixture 
def basic_checks():
    return [
        Check("one", "sqlserver", "test", "test", None, suites=["demo", "example"]),
        Check("two", "sqlserver", "idk", "pass", None, suites=["demo", "hello"])
    ]
    
def test_add_checks(basic_checks):
    csc = CheckSuiteCollection()
    csc.add_checks(basic_checks)

    suites = csc.suites

    demo = suites["demo"]
    example = suites["example"]
    hello = suites["hello"]

    assert len(demo) == 2
    assert len(example) == 1
    assert len(hello) == 1

    assert demo[0].check_name == "one"
    assert demo[1].check_name == "two"
    assert example[0].check_name == "one"
    assert hello[0].check_name == "two"

