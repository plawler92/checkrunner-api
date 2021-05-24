import checkrunner.file_util as file_util
import tests.test_config as cfg

def test_get_files():
    # should setup a test that creates files/folders
    files = file_util.get_files(cfg.checks_path)
    assert len(files) == 1

def test_read_yaml():
    y = file_util.read_yaml(cfg.checks_path + "three.yaml")
    assert y["checkName"] == "three"
    assert y["checkType"] == "sqlserver"
    assert y["database"] == "TestDB"
    assert y["passValue"] == "Pass"
    assert y["sql"].strip() == "SELECT 'Pass'" 