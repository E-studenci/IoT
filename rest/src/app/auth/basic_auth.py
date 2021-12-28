from app.error_handlers import ResponseError, ResponseData, response_wrapper
from database.mongo.read import get_admin_by_login
from utils.errors import MongoConnectionError
from main import BASIC_AUTH
from flask import abort


@BASIC_AUTH.verify_password
def verify_password(username, password):
    try:
        user = get_admin_by_login(username)
    except MongoConnectionError:
        abort(500)
    if user and user.password == password:
        return user
    return None


@BASIC_AUTH.error_handler
def bad_basic_auth(code):
    abort(code)