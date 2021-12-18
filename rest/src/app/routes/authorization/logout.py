from app.response_parser import ResponseData, response_wrapper
from flask_login import logout_user, login_required
from main import APP


@APP.route("/logout")
@login_required
@response_wrapper
def logout():
    logout_user()
    return ResponseData()