import json
from app.response_parser import ResponseData, response_wrapper, ResponseError
from flask_login import login_required
import database.mongo.create as create
import database.mongo.delete as delete
import database.mongo.update as update
import database.mongo.read as read
from flask import request
from main import APP

VISIT_ROUTE = "/visit"

@APP.route(VISIT_ROUTE + "/get_ongoing", methods=['GET'])
@login_required
@response_wrapper()
def get_ongoing_visits():
    users = read.get_ongoing_visits()
    return ResponseData(
        code = 200,
        data = users
    )

@APP.route(VISIT_ROUTE + "/get_pending", methods=['GET'])
@login_required
@response_wrapper()
def get_pending_visits():
    visits = read.get_pending_visits()
    return ResponseData(
        code = 200,
        data = visits
    )

@APP.route(VISIT_ROUTE + "/confirm/<id>", methods=['POST'])
@login_required
@response_wrapper()
def confirm_visit(id: str):
    result = update.confirm_visit(id)
    return ResponseData(
        code = 200,
        data = result
    )
    