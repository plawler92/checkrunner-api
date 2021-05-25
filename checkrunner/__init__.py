import logging
from logging.config import dictConfig
from pathlib import Path

from flask import Flask

from checkrunner.check_manager import CheckManager
from checkrunner.check_factory import CheckFactory
from checkrunner.check_memory import CheckMemory


def create_app(config):
    app = Flask(__name__, instance_relative_config=False)

    #ma = Marshmallow(app)

    # do config stuff
    log = logging.getLogger("werkzeug")
    log.disabled = True

    app.config.from_object(config)


    check_memory = CheckMemory()
    check_factory = CheckFactory(config.databases)
    check_manager = CheckManager(config.checks_path, check_factory, check_memory)
    check_manager.refresh_checks()
    app.check_manager = check_manager

    #with app.app_context()
    from checkrunner import api
    app.register_blueprint(api.api_blueprint, url_prefix="/api")

    from checkrunner import healthchecks
    app.register_blueprint(healthchecks.healthchecks_blueprint)

    # init swagger object

    return app