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
@response_wrapper
def bad_basic_auth(code):
    if BASIC_AUTH.get_auth() is None:
        error = ResponseError(
            description='The server could not verify that you are authorized to access the URL requested. No credentials supplied.', 
            name='Authorization Missing'
        )
        return ResponseData(error=error, code=code)

    error = ResponseError(
        description='The server could not verify that you are authorized to access the URL requested. Wrong credentials supplied (e.g. a bad password).',
        name='Unauthorized Access'
    )
    return ResponseData(error=error, code=code)
