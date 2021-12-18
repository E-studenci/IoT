from pymongo import MongoClient
from database.models import *
from main import APP

@APP.mongo_query
def list_database_names(client: MongoClient):
    return client.list_database_names()


@APP.mongo_query
def get_user_by_email(client: MongoClient, email: str):
    return User(email, 'password')