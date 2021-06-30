from checkrunner.core.check_results import CheckResults
from checkrunner.core.check_result import CheckResult

def test_check_suite():
    check_results = create_check_results(2)
    cs = CheckResults("test-suite", check_results)

    assert cs.name == "test-suite"
    assert cs.successes == 1
    assert cs.failures == 1
    assert len(cs.check_results) == 2

def test_check_suite_serialization():
    check_results = create_check_results(2)
    cs = CheckResults("test-suite", check_results)
    
    s = cs.serialize()

    assert s["name"] == "test-suite"
    assert s["successes"] == 1
    assert s["failures"] == 1
    

def create_check_results(num):
    return [
        CheckResult(str(i), "sqlserver", True if i % 2 == 0 else False, "test", "test", "2021")
        for i in range(num)
    ]