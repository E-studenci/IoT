import bcrypt
from bson import ObjectId
from pymongo import MongoClient, results
from datetime import datetime


salt = b'$2b$12$pzEs7Xy4xlrgcpLSrcN71O'

HOSTNAME = ""
PORT = "27017"
USERNAME = "root"
PASSWORD = "mongo"
DB_NAME = "rental"

USERS = "Users"
VISIT_TYPES = "VisitTypes"
VISIT_ARCHIVE = "VisitArchive"

DATE_FORMAT = "%Y/%m/%d %H:%M:%S"


client = MongoClient("mongodb://" + USERNAME + ":" + PASSWORD + "@" + HOSTNAME + ":" + PORT + "/", connect=True)


def convertObjectIdsToStr(object_):
    if isinstance(object_, ObjectId):
        return str(object_)
    if isinstance(object_, list):
        for i in range(len(object_)):
            if isinstance(object_[i], ObjectId):
                object_[i] = str(object_[i])
            else:
                convertObjectIdsToStr(object_[i])
    elif isinstance(object_, dict):
       for key in object_.keys():
            if isinstance(object_[key], ObjectId):
                object_[key] = str(object_[key])
            else:
                convertObjectIdsToStr(object_[key])
    return object_

class MongoQueries:
    def __init__(self):
        self.iotDB = client[DB_NAME]
    
    def email_in_database(self, email):
        return self.iotDB[USERS].find_one({"email": email}) is not None

    def register_user(self, user):
        return self.iotDB[USERS].insert_one(user).inserted_id

    def set_user_status(self, user_id, status):
        return self.iotDB[USERS].find_one_and_update({"_id": ObjectId(user_id)}, {"$set": {"status": status}}) is not None

    def change_user_balance(self, user_id, amount):
        return self.iotDB[USERS].find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$inc": {"balance": amount}}
        ) is not None

    def assign_card(self, user_id, card_rfid):
        result = self.iotDB[USERS].find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$push": {"cards": bcrypt.hashpw(card_rfid.encode('utf8'), salt)}})
        return result is not None

    def unassign_card(self, user_id, card_rfid):
        result = self.iotDB[USERS].find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$pull": {"cards": bcrypt.hashpw(card_rfid.encode('utf8'), salt)}})
        return result is not None
    
    def get_card_user_id(self, card_rfid):
        result = self.iotDB[USERS].find_one({"cards": bcrypt.hashpw(card_rfid.encode('utf8'), salt)})
        if result is None:
            return None
        return convertObjectIdsToStr(result["_id"])

    def create_visit_type(self, visit_type):
        return self.iotDB[VISIT_TYPES].insert_one(visit_type).inserted_id

    def get_visit_type_id_by_name(self, visit_type_name):
        result = self.iotDB[VISIT_TYPES].find_one({"visitType": visit_type_name})
        if result is None:
            return None
        return convertObjectIdsToStr(result["_id"])

    def get_visit_type_id_by_rfidScanner(self, rfidScanner):
        result = self.iotDB[VISIT_TYPES].find_one({"RFIDScanner": rfidScanner})
        if result is None:
            return None
        return convertObjectIdsToStr(result["_id"])

    def start_visit(self, visit_type_id, user_id):
        visit_type = self.iotDB[VISIT_TYPES].find_one({"_id": ObjectId(visit_type_id)})

        result = self.iotDB[USERS].find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$set": {"currentVisit": {
                    "visitStart": datetime.now().strftime(DATE_FORMAT),
                    "costPerMin": visit_type["costPerMin"],
                    "visitType":  ObjectId(visit_type_id)}}})
        return result is not None
    
    def end_visit(self, user_id):
        user = self.iotDB[USERS].find_one_and_update(
            {"_id": ObjectId(user_id)},
            {"$unset": {"currentVisit": ""}})
        if user is None or "currentVisit" not in user:
            return None
        curr_visit = user["currentVisit"]
        visit_end = datetime.now()
        total_cost = (visit_end - datetime.strptime(curr_visit["visitStart"], DATE_FORMAT)).total_seconds()/60 * int(curr_visit["costPerMin"])

        result = self.iotDB[VISIT_ARCHIVE].insert_one({
            "visitStart": curr_visit["visitStart"],
            "visitEnd": visit_end.strftime(DATE_FORMAT),
            "costPerMin": curr_visit["costPerMin"],
            "totalCost": total_cost,
            "visitType": curr_visit["visitType"],
            "user": ObjectId(user_id)
        })
        return total_cost
        
