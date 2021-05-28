import logging
from flask import request, Blueprint, current_app, make_response
from flask.json import jsonify

from checkrunner.route_models import CheckRequest

api_blueprint = Blueprint("api_blueprint", __name__)

@api_blueprint.route("/test", methods=["GET"])
def test():
    return jsonify(Test=True)

@api_blueprint.route("/check", methods=["GET"])
def check():
    cr = CheckRequest(
        request.args.get("name"),
        request.args.get("suite"),
        request.args.get("type")
    )
    validation = cr.validate()
    if validation[0] == False:
        pass

    check_result = None
    if cr.check_name:
        check_result = current_app.check_manager.run_check_by_name(cr.check_name)
    elif cr.check_suite:
        check_result = current_app.check_manager.run_checks_by_suite(cr.check_suite)
    elif cr.check_type:
        check_result = current_app.check_manager.run_checks_by_type(cr.check_type)

    if check_result:
        return jsonify(check_suite=check_result.serialize())
    else:
        return make_response(jsonify(check_results=[]), 404)

@api_blueprint.route("/refresh_checks", methods=["POST"])
def refresh_checks():
    current_app.check_manager.refresh_checks()
    return jsonify(success=True)

@api_blueprint.route("/check_names", methods=["GET"])
def check_names():
    check_names = current_app.check_manager.get_check_names()

    if check_names:
        return jsonify(check_names=check_names)
    else: 
        return make_response(jsonify(check_names=[]), 404)

@api_blueprint.route("/check_suites", methods=["GET"])
def check_suites():
    check_suites = list(current_app.check_manager.get_check_suites())

    if check_suites:
        return jsonify(check_suites=check_suites)
    else:
        return make_response(jsonify(check_suites=[]), 404)