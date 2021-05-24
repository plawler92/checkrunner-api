from checkrunner.check_memory import CheckMemory
from checkrunner.check import Check

def create_checks(num_checks):
    return [
        Check(
            str(i),
            "sqlserver" if i % 2 == 0 else "unknown",
            None,
            None,
            None,
            suites=["tests" if i % 2 == 0 else "hello"]
        )
        for i in range(0, num_checks)
    ]

def test_set_checks():
    cm = CheckMemory()
    cm.set_checks(create_checks(3))
    assert len(cm._checks) == 3

def test_get_checks_by_type():
    cm = CheckMemory()
    cm.set_checks(create_checks(7))
    checks = cm.get_checks_by_type("sqlserver")
    assert len(checks) == 4

def test_get_check_by_name():
    cm = CheckMemory()
    cm.set_checks(create_checks(7))
    check = cm.get_check_by_name("0")
    assert check.check_name == "0" 

def test_get_checks_by_suite():
    cm = CheckMemory()
    cm.set_checks(create_checks(3))
    checks = cm.get_checks_by_suite("tests")
    assert len(checks) == 2