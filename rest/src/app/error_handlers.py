from app.response_parser import ResponseError, ResponseData, data_wrapper
from flask import Response
from main import APP


@APP.errorhandler(400)
@data_wrapper
def page_not_found(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 400, error = error)


@APP.errorhandler(401)
@data_wrapper
def unauthorized(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 401, error = error)


@APP.errorhandler(404)
@data_wrapper
def page_not_found(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 404, error = error)


@APP.errorhandler(405)
@data_wrapper
def method_not_allowed(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 405, error = error)


@APP.errorhandler(500)
@data_wrapper
def internal_server_error(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 500, error = error)