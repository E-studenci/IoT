from app.response_parser import ResponseError, response_wrapper, ResponseData
from flask import Response
from main import APP


@APP.errorhandler(400)
@response_wrapper
def page_not_found(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 400, error = error)


@APP.errorhandler(401)
@response_wrapper
def page_not_found(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 401, error = error)


@APP.errorhandler(404)
@response_wrapper
def page_not_found(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 404, error = error)


@APP.errorhandler(405)
@response_wrapper
def page_not_found(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 405, error = error)


@APP.errorhandler(500)
@response_wrapper
def internal_server_error(error) -> Response:
    error = ResponseError(error = error)
    return ResponseData(code = 500, error = error)