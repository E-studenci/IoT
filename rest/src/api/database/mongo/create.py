from pymongo import MongoClient
from datetime import datetime

from api.database.models import *
from api.utils.mongo import * 
from api import APP


@APP.mongo_query
def register_user(client: MongoClient, user:dict) -> str:
    return convertObjectIdsToStr(client.iot[USERS].insert_one(user).inserted_id)


@APP.mongo_query
def create_visit_type(client:MongoClient, visit_type:dict) -> str:
    return convertObjectIdsToStr(client.iot[VISIT_TYPES].insert_one(visit_type).inserted_id)


@APP.mongo_query
def start_visit(client:MongoClient, visit_type_id:str, user_id:str) -> str:
    visit_type = client.iot[VISIT_TYPES].find_one({"_id": ObjectId(visit_type_id)})
    result = client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": {"current_visit": {
                "_id": ObjectId(),
                "visit_start": datetime.now().strftime(DATE_FORMAT),
                "cost_per_min": int(visit_type["cost_per_min"]),
                "visit_type":  ObjectId(visit_type_id)}}})
    return result is None 


TEST=False
if TEST:
    client = MongoClient("mongodb://root:mongo@130.61.111.97:27017/?authSource=iot&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
    start_visit(client,"61e4361a045097543aebb74f" ,"61e4362b045097543aebb754")