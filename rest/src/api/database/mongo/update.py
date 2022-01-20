from pymongo import MongoClient, ReturnDocument
from datetime import datetime

from api.database.models import *
from api.utils.mongo import *
from api import APP


@APP.mongo_query
def edit_user(client: MongoClient,id:str, changes:dict) -> str:
    return convertObjectIdsToStr(client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": changes}, 
        return_document=ReturnDocument.AFTER))

@APP.mongo_query
def assign_card(client: MongoClient, user_id: str, card_rfid: str) -> bool:
    result = client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$set": {"card": card_rfid}})
    return result is not None


@APP.mongo_query
def end_visit(client: MongoClient, user_id: str, visit_end:datetime) -> int:
    user = client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$unset": {"current_visit": ""}})
    if user is None or "current_visit" not in user:
        return None
    curr_visit = user["current_visit"]
    total_cost = int((visit_end - datetime.strptime(curr_visit["visit_start"], DATE_FORMAT)).total_seconds()/60 * int(curr_visit["cost_per_min"]))

    result = client.iot[VISIT_ARCHIVE].insert_one({
        "_id": curr_visit["_id"],
        "visit_start": curr_visit["visit_start"],
        "visit_end": visit_end.strftime(DATE_FORMAT),
        "cost_per_min": curr_visit["cost_per_min"],
        "total_cost": total_cost,
        "visit_type": curr_visit["visit_type"],
        "user": ObjectId(user_id),
        "status": "PENDING"
    })
    return convertObjectIdsToStr(result.inserted_id)

@APP.mongo_query
def confirm_visit(client: MongoClient, visit_id:str) -> bool:
    visit = client.iot[VISIT_ARCHIVE].find_one({"_id": ObjectId(visit_id)})
    if "status" in visit and visit["status"] == "PENDING":
        result = client.iot[VISIT_ARCHIVE].find_one_and_update(
            {"_id": ObjectId(visit_id)},
            {"$set": {"status": "CONFIRMED"}},
            return_document=ReturnDocument.AFTER)
        return True
    return False

TEST=False
if TEST:
    client = MongoClient("mongodb://root:mongo@130.61.111.97:27017/?authSource=iot&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
    end_visit(client,"61e4362b045097543aebb758", datetime.utcnow())
    