from database.mongo_queries import list_database_names
from main import APP
import json

@APP.route("/")
def index():
    return json.dumps(list_database_names(), indent=2)

