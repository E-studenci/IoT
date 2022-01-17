from utils.json_validation.json_methods import validate_json
from utils.errors import MongoConnectionError
from flask import Response, abort, request
from flask.wrappers import BadRequest
from bson.errors import InvalidId
from functools import wraps
import json

RESPONSE_CODES = [
    (100, 199, 'info'),
    (200, 299, 'success'),
    (300, 399, 'redirect'),
    (400, 499, 'client-error'),
    (500, 599, 'server-error')
]

def parse_code(code: int) -> str:
    for tup in RESPONSE_CODES:
        if tup[0] <= code <= tup[1]:
            return tup[2]
    return 'unknown'


class ResponseError(dict):
    def __init__(self, description: str = '', name: str = '', error = None) -> None:
        if error is None:
            dict.__init__(self, description=description, name=name)
            self.description = description
            self.name = name
        else:
            dict.__init__(self, description=error.description, name=error.name)
            self.description = error.description
            self.name = error.name


class ResponseData:
    def __init__(self, data: dict = {}, code: int = 200, error: ResponseError = None) -> None:
        self.data = data
        self.code = code
        self.error = error

def data_wrapper(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        response: ResponseData = func(*args, **kwargs)
        return Response(
            response=json.dumps({
                'data': response.data,
                'error': response.error,
                'status': parse_code(response.code)
            }),
            status=response.code,
            mimetype='application/json'
        )
    return wrapper

def response_wrapper(json_schema=None):
    def called(func):
        @data_wrapper
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if json_schema:
                    if not request.is_json:
                        response_data = ResponseData(
                            code = 400,
                            error = ResponseError(
                                description='Provide application/json or application/*+json content type.',
                                name='Mimetype error'
                            )
                        )
                        return response_data
                    
                    
                    valid, error = validate_json(json_schema, request.json)
                    if not valid:
                        response_data = ResponseData(
                            code = 400,
                            error = ResponseError(
                                description=error,
                                name='Invalid JSON schema'
                            )
                        )
                        return response_data
                    
                response_data: ResponseData = func(*args, **kwargs)
            except MongoConnectionError:
                abort(500)
            except InvalidId as error:
                response_data = ResponseData(
                    code = 400,
                    error = ResponseError(
                        description=error.__str__(),
                        name='Invalid JSON'
                    )
                )
            except BadRequest as error:
                response_data = ResponseData(
                    code = error.code,
                    error = ResponseError(
                        description=error.description,
                        name='Invalid JSON'
                    )
                )
                return response_data
            return response_data
        return wrapper
    return called
