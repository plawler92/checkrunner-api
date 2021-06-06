from checkrunner.core.check_result import CheckResult
from datetime import datetime

def test_check_result_serialization():
    vals = {
        "check_name": "test-1",
        "check_type": "sqlserver",
        "check_result": True,
        "check": "SELECT 'PASS'",
        "check_pass_value": "PASS",
        "execution_time": datetime(2021, 1, 1, 12, 30, 0), # 1/1/2021 @ 12:30.0
        "error": "test error"
    }
    cr = CheckResult(**vals)
    s = cr.serialize()
    assert s["check_name"] == vals["check_name"]
    assert s["check_type"] == vals["check_type"]
    assert s["check_result"] == vals["check_result"]
    assert s["check"] == vals["check"]
    assert s["check_pass_value"] == vals["check_pass_value"]
    assert s["execution_time"] == "2021-01-01 12:30:00"
    assert s["error"] == "test error"