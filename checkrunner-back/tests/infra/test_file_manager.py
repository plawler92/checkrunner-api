from checkrunner.infra.yaml_managers.file_manager import FileManager
from tests.config import Config

cfg = Config()

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