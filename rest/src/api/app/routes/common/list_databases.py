from flask_login import login_required

from api.app.response_parser import ResponseData, response_wrapper
from api.database.mongo.read import list_database_names
from api import APP


@APP.route("/list_databases")
@login_required
@response_wrapper()
def list_databases():
    data = list_database_names()
    
    return ResponseData(
        data = {'database_names': data},
        code = 200
    )
