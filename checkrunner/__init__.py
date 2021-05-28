import logging

from flask import Flask

from checkrunner.check_manager import CheckManager
from checkrunner.check_factory import CheckFactory
from checkrunner.check_memory import CheckMemory
from checkrunner.file_manager import FileManager


def create_app(config):
    app = Flask(__name__, instance_relative_config=False)

    log = logging.getLogger("werkzeug")
    log.disabled = True

    app.config.from_object(config)

    check_memory = CheckMemory()
    check_factory = CheckFactory(config.databases)
    file_manager = FileManager(config.checks_path)

    check_manager = CheckManager(check_factory=check_factory, check_memory=check_memory, yaml_manager=file_manager)
    check_manager.refresh_checks()
    app.check_manager = check_manager

    from checkrunner import api
    app.register_blueprint(api.api_blueprint, url_prefix="/api")

    from checkrunner import healthchecks
    app.register_blueprint(healthchecks.healthchecks_blueprint)

    return app