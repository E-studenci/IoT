from app.response_parser import ResponseData, response_wrapper
from utils.json_stuff.json_methods import validate_json
from flask_login import login_required
from flask import request
from main import APP

import database.mongo.create as create
import database.mongo.delete as delete
import database.mongo.read as read

USER_ROUTE = "/user"


@APP.route(USER_ROUTE + "/add", methods=['POST'])
@login_required
@response_wrapper
def add_user():
    request_json = request.json
    valid, error_message = validate_json(None, request_json)
    if not valid:
        return ResponseData(
            code = 400,
            error = error_message
        )

    if read.get_user_by_email(request_json["email"]):
        return ResponseData(
            code = 400,
            error = "email already used"
        )
    result = create.register_user(request_json)
    return ResponseData(
        code = 200,
        data = result
    )


@APP.route(USER_ROUTE + "/get", methods=['GET'])
@login_required
@response_wrapper
def get_user():
    request_json = request.json
    valid, error_message = validate_json(None, request_json)
    if not valid:
        return ResponseData(
            code = 400,
            error = error_message
        )
    user = read.get_user_by_id(request_json["_id"])
    if user is None:
        return ResponseData(
            code = 400,
            error = "user not found"
        )
    return ResponseData(
        code = 200,
        data = user.__dict__
    )

# @APP.route(USER_ROUTE + "/edit", methods=['UPDATE'])
# @login_required
# @response_wrapper
# def update_user():
#     pass ## TODO check new against existing

@APP.route(USER_ROUTE + "/delete", methods=['DELETE'])
@login_required
@response_wrapper
def delete_user():
    request_json = request.json
    valid, error_message = validate_json(None, request_json)
    if not valid:
        return ResponseData(
            code = 400,
            error = error_message
        )
    result = delete.delete_user(request_json["_id"])
    if not result:
        return ResponseData(
            code = 400,
            error = "user not found"
        )
    return ResponseData(
        code = 200
    )