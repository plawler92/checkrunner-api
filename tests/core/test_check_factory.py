import pytest

from checkrunner.core.factories import CheckFactory
from checkrunner.core.exceptions import FactoryClassTypeNotFoundError
# from tests.config import Config

# cfg = Config()

# def create_check_factory():
#     s = SQLServerCheckFactory(cfg.databases)
#     cf = CheckFactory()
#     cf.add_factory(s.factory_type, s)
#     return cf

def test_create_empty_check_factory():
    cf = CheckFactory()

    assert cf.factory_classes == dict()

def test_create_check_factory_with_class(dummy_factory_class):
    fc = {"dummy": dummy_factory_class}
    cf = CheckFactory(fc)

    assert cf.factory_classes == fc
    
def test_add_factory(dummy_factory_class):
    cf = CheckFactory()
    cf.add_factory("dummy", dummy_factory_class)

    assert cf.factory_classes.get("dummy") == dummy_factory_class

def test_create_check(dummy_factory_class, basic_sqlserver_yaml):
    cf = CheckFactory()
    cf.add_factory("sqlserver", dummy_factory_class)
    c = cf.create_check(basic_sqlserver_yaml)

    assert c == True

def test_create_check_type_not_found(dummy_factory_class, basic_sqlserver_yaml):
    cf = CheckFactory({"dummy": dummy_factory_class})
    
    with pytest.raises(FactoryClassTypeNotFoundError):
        cf.create_check(basic_sqlserver_yaml)