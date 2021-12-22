from pymongo import MongoClient
from database.models import *
from main import APP
from rest.src.utils.mongo import *
from datetime import datetime

@APP.mongo_query
def assign_card(client:MongoClient, user_id:str, card_rfid:str) -> bool:
    result = client.iotDB[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$push": {"cards": card_rfid}})
    return result is not None

def change_user_balance(client:MongoClient, user_id:str, amount:int) -> bool:
    return client.iotDB[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$inc": {"balance": amount}}
    ) is not None

def end_visit(client:MongoClient, user_id:str) -> int:
    user = client.iotDB[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$unset": {"currentVisit": ""}})
    if user is None or "currentVisit" not in user:
        return None
    curr_visit = user["currentVisit"]
    visit_end = datetime.now()
    total_cost = (visit_end - datetime.strptime(curr_visit["visitStart"], DATE_FORMAT)).total_seconds()/60 * int(curr_visit["costPerMin"])

    result = client.iotDB[VISIT_ARCHIVE].insert_one({
        "visitStart": curr_visit["visitStart"],
        "visitEnd": visit_end.strftime(DATE_FORMAT),
        "costPerMin": curr_visit["costPerMin"],
        "totalCost": total_cost,
        "visitType": curr_visit["visitType"],
        "user": ObjectId(user_id)
    })
    return total_cost
    