import json
from app.response_parser import ResponseData, response_wrapper, ResponseError
from flask_login import login_required
import database.mongo.create as create
import database.mongo.delete as delete
import database.mongo.update as update
import database.mongo.read as read
from flask import request
from main import APP

USER_ROUTE = "/user"


@APP.route(USER_ROUTE + "/add", methods=['POST'])
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


@APP.route(USER_ROUTE + "/get/{id}", methods=['GET'])
@login_required
@response_wrapper()
def get_user(id:str):
    user = read.get_user_by_id(id)
    if user is None:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="user not found")
        )
    return ResponseData(
        code = 200,
        data = user.__dict__
    )

@APP.route(USER_ROUTE + "/edit", methods=['UPDATE'])
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
        code = 200
    )

@APP.route(USER_ROUTE + "/delete", methods=['DELETE'])
@login_required
@response_wrapper()
def delete_user():
    json_data = request.json
    result = delete.delete_user(json_data["_id"])
    if not result:
        return ResponseData(
            code = 400,
            error = ResponseError(name="Invalid Data", description="user not found")
        )
    return ResponseData(
        code = 200
    )