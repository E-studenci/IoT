from datetime import datetime
from pymongo import MongoClient
from database.models import *
from main import APP
from rest.src.app.app import App
from utils.mongo import * 


@APP.mongo_query
def register_user(client: MongoClient, user:dict) -> str:
    return convertObjectIdsToStr(client.iotDB[USERS].insert_one(user.__dict__).inserted_id)

@APP.mongo_query
def create_visit_type(client:MongoClient, visit_type:dict) -> str:
    return convertObjectIdsToStr(client.iotDB[VISIT_TYPES].insert_one(visit_type.__dict__).inserted_id)

@APP.mongo_query
def start_visit(client:MongoClient, visit_type_id:str, user_id:str) -> str:
    visit_type = client.iotDB[VISIT_TYPES].find_one({"_id": ObjectId(visit_type_id)})
    result = client.iotDB[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": {"currentVisit": {
                "visitStart": datetime.now().strftime(DATE_FORMAT),
                "costPerMin": visit_type["costPerMin"],
                "visitType":  ObjectId(visit_type_id)}}})
    return result is None 