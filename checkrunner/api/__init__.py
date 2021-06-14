from checkrunner.infra.yaml_managers.s3_manager import S3YamlManager
import logging

from flask import Flask
from flask_cors import CORS

from checkrunner.core.check_manager import CheckManager
from checkrunner.core.factories import CheckFactory, SQLServerCheckFactory
from checkrunner.infra.yaml_managers.file_manager import FileManager
from checkrunner.infra.yaml_managers.utils import AWSS3Information
from checkrunner.infra.executors import SQLServerExecutor

def create_yaml_manager(config):
    if config.yaml_manager_type == "file":
        return FileManager(config.checks_path)
    elif config.yaml_manager_type == "s3":
        aws_info = AWSS3Information(
            config.aws_access_key, 
            config.aws_secret_access_key, 
            config.aws_role_arn, 
            config.aws_external_id, 
            config.s3_bucket, 
            config.s3_folder
        )
        return S3YamlManager(aws_info)

def create_app(config) -> Flask:
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object(config)

    CORS(app)

    sql_server_check_factory = SQLServerCheckFactory(config.databases, SQLServerExecutor)
    check_factory = CheckFactory()
    check_factory.add_factory(sql_server_check_factory.factory_type, sql_server_check_factory)

    yaml_manager = create_yaml_manager(config)
    check_manager = CheckManager(check_factory=check_factory, yaml_manager=yaml_manager)

    app.check_manager = check_manager

    from checkrunner.api import api
    app.register_blueprint(api.api_blueprint, url_prefix="/api")

    from checkrunner.api import healthchecks
    app.register_blueprint(healthchecks.healthchecks_blueprint)

    return app