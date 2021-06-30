import pytest

from checkrunner.core.check_manager import CheckManager
from tests.config import Config

cfg = Config()

def test_check_manager_creation(dummy_check_factory, dummy_yaml_manager):
    cm = CheckManager(dummy_check_factory, dummy_yaml_manager)

    assert cm.check_factory == dummy_check_factory
    assert cm.yaml_manager == dummy_yaml_manager

def test_create_checks(basic_sqlserver_yaml, dummy_check_factory):
    cm = CheckManager(dummy_check_factory, None)
    checks = cm.create_checks([basic_sqlserver_yaml])

    assert len(checks) == 1
    assert checks[0] == True

def test_create_checks_factory_class_not_found_error(basic_sqlserver_yaml, factoryclassnotfound_check_factory):
    cm = CheckManager(factoryclassnotfound_check_factory, None)
    checks = cm.create_checks([basic_sqlserver_yaml])

    assert checks == []

def test_get_check_suites(dummy_yaml_manager, basic_sqlserver_check_factory):
    cm = CheckManager(basic_sqlserver_check_factory, dummy_yaml_manager)
    suite = cm.get_check_suites()

    assert len(suite.suites) == 2
    assert len(suite.suites["demo"]) == 2
    assert len(suite.suites["test"]) == 2

    assert suite.suites["demo"][0].check_name == "1"
    assert suite.suites["demo"][1].check_name == "2"

    assert suite.suites["test"][0].check_name == "1"
    assert suite.suites["test"][1].check_name == "2"

# add tests for runchecksuites and run check by name