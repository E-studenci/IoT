from pymongo import MongoClient
from database.models import *
from utils.mongo import * 
from typing import List
from main import APP


@APP.mongo_query
def list_database_names(client: MongoClient):
    return client.list_database_names()


@APP.mongo_query
def get_admin_by_id(client: MongoClient, admin_id: str) -> User:
    result = client.iot[ADMINS].find_one({"_id": ObjectId(admin_id)})
    return None if result is None else Admin.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_admin_by_login(client: MongoClient, login: str) -> User:
    result = client.iot[ADMINS].find_one({"login": login})
    return None if result is None else Admin.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_user_by_email(client: MongoClient, email: str) -> User:
    result = client.iot[USERS].find_one({"email": email})
    return None if result is None else User.from_dict(convertObjectIdsToStr(result))

@APP.mongo_query
def get_user_by_id(client: MongoClient, id: str) -> User:
    result = client.iot[USERS].find_one({"_id": ObjectId(id)})
    return None if result is None else User.from_dict(convertObjectIdsToStr(result))

@APP.mongo_query
def get_card_user(client: MongoClient, card_rfid: str) -> User:
    result = client.iot[USERS].find_one({"card": card_rfid})
    return None if result is None else User.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_visit_type_by_name(client: MongoClient, visit_type_name: str) -> VisitType:
    result = client.iot[VISIT_TYPES].find_one({"visit_type": visit_type_name})
    return None if result is None else VisitType.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_visit_type_id_by_rfidScanner(client: MongoClient, rfidScanner: str) -> VisitType:
    result = client.iot[VISIT_TYPES].find_one({"rfid_scanner": ObjectId(rfidScanner)})
    return None if result is None else VisitType.from_dict(convertObjectIdsToStr(result))


@APP.mongo_query
def get_all_visit_types(client: MongoClient) -> List[VisitType]:
    results = client.iot[VISIT_TYPES].find()
    return [VisitType.from_dict(convertObjectIdsToStr(result)) for result in results]

@APP.mongo_query
def get_ongoing_visits(client: MongoClient) -> List[User]:
    resultList = []
    for user in client.iot[USERS].find({"current_visit": {"$exists": True}}):
        resultList.append(Visit.from_dict(user["current_visit"]))
    return resultList

@APP.mongo_query
def get_current_visit(client: MongoClient, user:User) -> Visit:
    pass ## TODO

@APP.mongo_query
def get_user_visits(client: MongoClient, user_id: str) -> List[Visit]:
    result_list = []
    user = client.iot[USERS].find_one({"_id": ObjectId(user_id)})
    if user is None:
        return None
    if "current_visit" in user:
        result_list.append(Visit.from_dict(convertObjectIdsToStr(user["current_visit"])))
    for visit in client.iot[VISIT_ARCHIVE].find({"user": ObjectId(user_id)}):
        result_list.append(Visit.from_dict(convertObjectIdsToStr(visit)))
    return result_list