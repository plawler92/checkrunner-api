from checkrunner.infra.yaml_managers.s3_manager import S3YamlManager
import logging

from flask import Flask
from flask_cors import CORS

from checkrunner.core.check_manager import CheckManager
from checkrunner.core.factories import CheckFactory, SQLServerCheckFactory
from checkrunner.core.check_memory import CheckMemory
from checkrunner.infra.yaml_managers.file_manager import FileManager


def create_app(config) -> Flask:
    app = Flask(__name__, instance_relative_config=False)

    log = logging.getLogger("werkzeug")
    log.disabled = True

    app.config.from_object(config)

    CORS(app)

    check_memory = CheckMemory()
    sql_server_check_factory = SQLServerCheckFactory(config.databases)
    check_factory = CheckFactory()
    check_factory.add_factory(sql_server_check_factory)
    file_manager = FileManager(config.checks_path)
    # file_manager = S3YamlManager(config.aws_access_key, config.aws_secret_access_key, config.s3_bucket)

    check_manager = CheckManager(check_factory=check_factory, check_memory=check_memory, yaml_manager=file_manager)
    check_manager.refresh_checks()
    app.check_manager = check_manager

    from checkrunner.api import api
    app.register_blueprint(api.api_blueprint, url_prefix="/api")

    from checkrunner.api import healthchecks
    app.register_blueprint(healthchecks.healthchecks_blueprint)

    return app