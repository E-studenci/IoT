from pymongo import MongoClient
from database.models import *
from utils.mongo import *
from main import APP

@APP.mongo_query
def delete_user(client:MongoClient, user_id:str) -> bool:
    return client.iot[USERS].find_one_and_update({"_id": ObjectId(user_id)}, {"$set": {"status": "DELETED"}}) is not None

@APP.mongo_query
def unassign_card(client:MongoClient, user_id:str, card_rfid:str) -> bool:
    result = client.iot[USERS].find_one_and_update(
        {"_id": ObjectId(user_id)},
        {"$unset": {"card": ""}})
    return result is not None


TEST=False
if TEST:
    client = MongoClient("mongodb://root:mongo@130.61.111.97:27017/?authSource=iot&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
    