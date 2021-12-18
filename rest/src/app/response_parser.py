from flask import Response
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


def response_wrapper(func):
    def wrapper(*args, **kwargs):
        response: ResponseData = func(*args, **kwargs)
        return Response(
            response=json.dumps({'data': response.data, 'error': response.error, 'status': parse_code(response.code)}),
            status=response.code,
            mimetype='application/json'
        )
    wrapper.__name__ = func.__name__
    return wrapper
