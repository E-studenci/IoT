from flask_login import login_required
from flask import request

from api.app.response_parser import ResponseData, response_wrapper, ResponseError
from api import APP
import api.database.mongo.create as create
import api.database.mongo.delete as delete
import api.database.mongo.update as update
import api.database.mongo.read as read

USER_ROUTE = "/user"


@APP.route(USER_ROUTE + "/add", methods=['PUT'])
@login_required
@response_wrapper()
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

@APP.route(USER_ROUTE + "/edit", methods=['POST'])
@login_required
@response_wrapper()
def update_user():
    json_data = request.json
    changes = dict(json_data)
    changes.pop("_id")
    result = update.edit_user(json_data["_id"], changes)
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
    