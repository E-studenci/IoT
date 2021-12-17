from pymongo import MongoClient
from main import APP


@APP.mongo_query
def list_database_names(client: MongoClient):
    return client.list_database_names()