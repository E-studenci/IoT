from app.response_parser import ResponseData, response_wrapper
from database.mongo.read import list_database_names
from flask_login import login_required
from main import APP


@APP.route("/list_databases")
@login_required
@response_wrapper()
def list_databases():
    data = list_database_names()
    
    return ResponseData(
        data = {'database_names': data},
        code = 200
    )
