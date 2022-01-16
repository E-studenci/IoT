from app.response_parser import ResponseData, response_wrapper
from main import APP


@APP.route("/")
@response_wrapper()
def index():
    return ResponseData(
        data = 'OK',
        code = 200
    )

