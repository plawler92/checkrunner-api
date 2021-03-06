import logging
from flask import request, Blueprint, current_app, make_response
from flask.json import jsonify

from checkrunner.api.route_models import CheckRequest

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
        check_result = current_app.check_manager.run_check_suite(cr.check_suite)
    # if cr.check_name:
    #     check_result = current_app.check_manager.run_check_by_name(cr.check_name)
    # elif cr.check_suite:
    #     check_result = current_app.check_manager.run_checks_suite(cr.check_suite)
    # elif cr.check_type:
    #     check_result = current_app.check_manager.run_checks_by_type(cr.check_type)

    if check_result:
        return jsonify(check_results=check_result.serialize())
    else:
        return make_response(jsonify(check_results=[]), 404)

# @api_blueprint.route("/refresh_checks", methods=["POST"])
# def refresh_checks():
#     current_app.check_manager.refresh_checks()
#     return jsonify(success=True)

@api_blueprint.route("/check_names", methods=["GET"])
def check_names():
    check_names = current_app.check_manager.get_check_names()

    if check_names:
        return jsonify(check_names=check_names)
    else: 
        return make_response(jsonify(check_names=[]), 404)

@api_blueprint.route("/check_suites", methods=["GET"])
def check_suites():
    suites = current_app.check_manager.get_check_suites()
    response = convert_check_suite_collection(suites.suites)

    if response:
        return jsonify(check_suites=response)
    else:
        return make_response(jsonify(check_suites=[]), 404)

@api_blueprint.route("/check_suite", methods=["GET"])
def get_check_suite():
    name = request.args.get("name")
    suites = current_app.check_manager.get_check_suites()

    suite = suites.suites.get(name)

    if suite:
        return jsonify(check_suite=create_check_suite_response(suite))
    else:
        return make_response(jsonify(check_suite=None), 404)
        
def create_check_suite_response(suite):
    checks = [
        c.serialize() for c in suite
    ]
    return checks




def convert_check_suite_collection(col):
    response = dict()
    for key, val in col.items():
        new_val = [check.check_name for check in val]
        response[key] = new_val
    return response