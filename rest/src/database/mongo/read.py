from rest.src.database.models.visit_type import VisitType
from rest.src.database.models.visit import Visit
from rest.src.database.models.user import User
from pymongo import MongoClient
from database.models import *
from utils.mongo import * 
from typing import List
from main import APP


@APP.mongo_query
def list_database_names(client: MongoClient):
    return client.list_database_names()


@APP.mongo_query
def get_user_by_email(client: MongoClient, email: str) -> User:
    result = client.iotDB[USERS].find_one({"email": email})
    return None if result is None else User.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_card_user(client: MongoClient, card_rfid: str) -> User:
    result = client.iotDB[USERS].find_one({"cards": card_rfid})
    return None if result is None else User.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_visit_type_by_name(client: MongoClient, visit_type_name: str) -> VisitType:
    result = client.iotDB[VISIT_TYPES].find_one({"visitType": visit_type_name})
    return None if result is None else VisitType.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_visit_type_id_by_rfidScanner(client: MongoClient, rfidScanner: str) -> VisitType:
    result = client.iotDB[VISIT_TYPES].find_one({"RFIDScanner": ObjectId(rfidScanner)})
    return None if result is None else VisitType.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_all_visit_types(client: MongoClient) -> List[VisitType]:
    results = client.iotDB[VISIT_TYPES].find()
    return [VisitType.from_dict(convertObjectIdsToStr(result)) for result in results]


@APP.mongo_query
def get_user_visits(client: MongoClient, user_id: str) -> List[Visit]:
    result_list = []
    user = client.iotDB[USERS].find_one({"_id": ObjectId(user_id)})
    if user is None:
        return None
    if "currentVisit" in user:
        result_list.append(Visit.from_dict(convertObjectIdsToStr(user["currentVisit"])))
    for visit in client.iotDB[VISIT_ARCHIVE].find({"user": ObjectId(user_id)}):
        result_list.append(Visit.from_dict(convertObjectIdsToStr(visit)))
    return result_list