from app.response_parser import ResponseData, response_wrapper
from database.mongo.read import list_database_names
from flask_login import login_required
from main import APP


@APP.route("/")
@response_wrapper
def index():
    return ResponseData(
        data = 'OK',
        code = 200
    )

