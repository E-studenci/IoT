from app.response_parser import ResponseData, response_wrapper
from flask_login import login_user
from main import APP, BASIC_AUTH


@APP.route('/login', methods=['GET'])
@BASIC_AUTH.login_required
@response_wrapper
def login():
    login_user(BASIC_AUTH.current_user())
    return ResponseData()
