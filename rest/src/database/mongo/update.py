from datetime import datetime
from pymongo import MongoClient, ReturnDocument
from database.models import *
from utils.mongo import *
from main import APP


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
def change_user_balance(client: MongoClient, user_id: str, amount: int) -> bool:
    return client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$inc": {"balance": amount}}
    ) is not None


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
        "user": ObjectId(user_id)
    })
    return convertObjectIdsToStr(result.inserted_id)


TEST=False
if TEST:
    client = MongoClient("mongodb://root:mongo@130.61.111.97:27017/?authSource=iot&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
    end_visit(client,"61e4362b045097543aebb758", datetime.utcnow())