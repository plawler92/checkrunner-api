import logging

from checkrunner.infra.executors import SQLServerExecutor
from checkrunner.core.check import Check
from checkrunner.core.exceptions import FactoryClassTypeNotFoundError

class CheckFactory:
    def __init__(self, factory_classes=None):
        self.factory_classes = factory_classes if factory_classes else dict()

    def add_factory(self, factory_key, factory_class):
        if self.factory_classes.get(factory_key):
            logging.warning(f"CheckFactory overwriting existing entry for {factory_key} type.")
        self.factory_classes[factory_key] = factory_class

    def create_check(self, check_params):
        factory = self.factory_classes.get(check_params["checkType"]["type"])
        if not factory:
            raise FactoryClassTypeNotFoundError(f"Check type {check_params['checkType']['type']} not found in CheckFactory")
        else: 
            return factory.create_check(check_params)

