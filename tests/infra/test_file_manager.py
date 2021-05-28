from checkrunner.file_manager import FileManager
import tests.config as cfg

# def test_get_files():
#     # should setup a test that creates files/folders
#     files = file_util.get_files(cfg.checks_path)
#     assert len(files) == 2

# def test_read_yaml():
#     y = file_util.read_yaml(cfg.checks_path + "three.yaml")
#     assert y["checkName"] == "three"
#     assert y["checkType"] == "sqlserver"
#     assert y["database"] == "TestDB"
#     assert y["passValue"] == "Pass"
#     assert y["sql"].strip() == "SELECT 'Pass'" 

def create_file_manager():
    return FileManager(cfg.checks_path)

def test_get_files():
    fm = create_file_manager()
    files = fm.get_files()

    assert len(files) == 2

def test_get_yamls():
    fm = create_file_manager()
    yamls = fm.get_yamls()

    assert len(yamls) == 2
    for y in yamls:
        assert "checkName" in y
        assert "checkType" in y
        assert "passValue" in y