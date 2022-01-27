from flask_login import login_required
from flask import request

from api.app.response_parser import ResponseData, response_wrapper, ResponseError
import api.utils.json_validation.json_schemas as json_schemas
import api.database.mongo.create as create
import api.database.mongo.delete as delete
import api.database.mongo.update as update
import api.database.mongo.read as read
from api import APP

USER_ROUTE = "/user"


@APP.route(USER_ROUTE + "/add", methods=['PUT'])
@login_required
@response_wrapper(json_schemas.ADD_USER_SCHEMA)
def add_user():
    json_data = request.json
    if read.get_user_by_email(json_data["email"]):
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="email already used")
        )
    result = create.register_user(json_data)
    return ResponseData(
        code = 200,
        data = result
    )


@APP.route(USER_ROUTE + "/get/<id>", methods=['GET'])
@login_required
@response_wrapper()
def get_user(id: str):
    user = read.get_user_by_id(id)
    if user is None:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="user not found")
        )
    return ResponseData(
        code = 200,
        data = user
    )


@APP.route(USER_ROUTE + "/get", methods=['GET'])
@login_required
@response_wrapper()
def get_users():
    users = read.get_all_users()
    return ResponseData(
        code = 200,
        data = users
    )


@APP.route(USER_ROUTE + "/edit/<id>", methods=['PATCH'])
@login_required
@response_wrapper(json_schemas.EDIT_USER_SCHEMA)
def update_user(id: str):
    json_data = request.json
    if "email" in json_data:
        if read.get_user_by_email(json_data["email"]):
            return ResponseData(
                code = 400,
                error = ResponseError(name="Invalid Data", description="email already used")
            )
    result = update.edit_user(id, json_data)
    if not result:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="user not found")
        )
    return ResponseData(
        code = 200,
        data=result
    )


@APP.route(USER_ROUTE + "/delete/<id>", methods=['DELETE'])
@login_required
@response_wrapper()
def delete_user(id: str):
    result = delete.delete_user(id)
    if not result:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="user not found")
        )
    return ResponseData(
        code = 200
    )
