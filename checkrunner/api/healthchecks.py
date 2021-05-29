import logging

from flask import Blueprint
from flask.json import jsonify

logger = logging.getLogger(__name__)

healthchecks_blueprint = Blueprint("healthchecks", __name__)

@healthchecks_blueprint.route("/alive", methods=["GET"])
@healthchecks_blueprint.route("/ready", methods=["GET"])
def alive():
    return jsonify(success=True)


def ready():
    return jsonify(success=True)
