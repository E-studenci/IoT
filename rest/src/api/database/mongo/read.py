from pymongo import MongoClient
from typing import List

from api.database.models import *
from api.utils.mongo import * 
from api import APP


@APP.mongo_query
def list_database_names(client: MongoClient):
    return client.list_database_names()


@APP.mongo_query
def get_admin_by_id(client: MongoClient, admin_id: str) -> User:
    result = client.iot[ADMINS].find_one({"_id": ObjectId(admin_id)})
    return None if result is None else Admin.from_dict(result)


@APP.mongo_query
def get_admin_by_login(client: MongoClient, login: str) -> User:
    result = client.iot[ADMINS].find_one({"login": login})
    return None if result is None else Admin.from_dict(result)


@APP.mongo_query
def get_user_by_email(client: MongoClient, email: str) -> User:
    result = client.iot[USERS].find_one({"email": email})
    if result is None:
        return None
    if "current_visit" in result:
        visit_type = client.iot[VISIT_TYPES].find_one({"_id": result["current_visit"]["visit_type"]})
        result["current_visit"]["visit_type"] = visit_type
    return User.from_dict(result)

@APP.mongo_query
def get_user_by_id(client: MongoClient, id: str) -> User:
    result = client.iot[USERS].find_one({"_id": ObjectId(id)})
    if "current_visit" in result:
        visit_type = client.iot[VISIT_TYPES].find_one({"_id": result["current_visit"]["visit_type"]})
        result["current_visit"]["visit_type"] = visit_type
    return User.from_dict(result)

@APP.mongo_query
def get_card_user(client: MongoClient, card_rfid: str) -> User:
    result = client.iot[USERS].find_one({"card": card_rfid})
    if result is None:
        return None
    if "current_visit" in result:
        visit_type = client.iot[VISIT_TYPES].find_one({"_id": result["current_visit"]["visit_type"]})
        result["current_visit"]["visit_type"] = visit_type
    return User.from_dict(result)


@APP.mongo_query
def get_visit_type_by_name(client: MongoClient, visit_type_name: str) -> VisitType:
    result = client.iot[VISIT_TYPES].find_one({"visit_type": visit_type_name})
    return None if result is None else VisitType.from_dict(result)


@APP.mongo_query
def get_visit_type_by_rfid_scanner(client: MongoClient, rfid_scanner: str) -> VisitType:
    result = client.iot[VISIT_TYPES].find_one({"rfid_scanner": rfid_scanner})
    return None if result is None else VisitType.from_dict(result)

@APP.mongo_query
def get_all_visit_types(client: MongoClient) -> List[VisitType]:
    results = client.iot[VISIT_TYPES].find()
    return [VisitType.from_dict(result) for result in results]

@APP.mongo_query
def get_all_users(client: MongoClient) -> List[User]:
    resultList = []
    visit_types = get_all_visit_types()
    for user in client.iot[USERS].find():
        try:
            # get visit type    
            visit_type = next(x for x in visit_types if ObjectId(x._id) == user["current_visit"]["visit_type"])
            # add visit type to current visit
            user["current_visit"]["visit_type"] = visit_type.__dict__
        except:
            pass
        # append user to list
        resultList.append(User.from_dict(user))
    return resultList


@APP.mongo_query
def get_ongoing_visits(client: MongoClient) -> List[User]:
    resultList = []
    visit_types = get_all_visit_types()
    for user in client.iot[USERS].find({"current_visit": {"$exists": True}}):
        # get visit type
        visit_type = next(x for x in visit_types if ObjectId(x._id) == user["current_visit"]["visit_type"])
        # add visit type to current visit
        user["current_visit"]["visit_type"] = visit_type
        # append user to list
        resultList.append(User.from_dict(user))
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
    for visit in client.iot[VISIT_ARCHIVE].find({"user": ObjectId(user_id)}):
        result_list.append(Visit.from_dict(visit))
    return result_list

@APP.mongo_query
def get_pending_visits(client: MongoClient) -> List[Visit]:
    result_list = []
    visit_types = get_all_visit_types()
    for visit in client.iot[VISIT_ARCHIVE].find({"status": "PENDING"}):
        visit_type = next(x for x in visit_types if ObjectId(x._id) == visit["visit_type"])
        visit["visit_type"] = visit_type
        visit["user"] = client.iot[USERS].find_one({"_id": visit["user"]})
        result_list.append(Visit.from_dict(visit))
    return result_list

TEST=False
if TEST:
    client = MongoClient("mongodb://root:mongo@130.61.111.97:27017/?authSource=iot&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
    x = get_ongoing_visits(client)
    print(x)
    x = get_card_user(client, "f91a61e515d1fc6a7fa9986473b6d0ff")
    print(x)
    