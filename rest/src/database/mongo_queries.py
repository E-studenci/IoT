from pymongo import MongoClient
from main import APP


@APP.mongo_query
def test_query(client: MongoClient):
    print(client.list_database_names())