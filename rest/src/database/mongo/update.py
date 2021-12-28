from datetime import datetime
from pymongo import MongoClient
from database.models import *
from utils.mongo import *
from main import APP


@APP.mongo_query
def assign_card(client: MongoClient, user_id: str, card_rfid: str) -> bool:
    result = client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$push": {"cards": card_rfid}})
    return result is not None


@APP.mongo_query
def change_user_balance(client: MongoClient, user_id: str, amount: int) -> bool:
    return client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$inc": {"balance": amount}}
    ) is not None


@APP.mongo_query
def end_visit(client: MongoClient, user_id: str) -> int:
    user = client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$unset": {"currentVisit": ""}})
    if user is None or "currentVisit" not in user:
        return None
    curr_visit = user["currentVisit"]
    visit_end = datetime.now()
    total_cost = (visit_end - datetime.strptime(curr_visit["visitStart"], DATE_FORMAT)).total_seconds()/60 * int(curr_visit["costPerMin"])

    result = client.iot[VISIT_ARCHIVE].insert_one({
        "visitStart": curr_visit["visitStart"],
        "visitEnd": visit_end.strftime(DATE_FORMAT),
        "costPerMin": curr_visit["costPerMin"],
        "totalCost": total_cost,
        "visitType": curr_visit["visitType"],
        "user": ObjectId(user_id)
    })
    return total_cost
    