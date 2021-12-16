import bcrypt
from pymongo import ObjectId, MongoClient

salt = b'$2b$12$pzEs7Xy4xlrgcpLSrcN71O'

HOSTNAME = ""
PORT = "27017"
USERNAME = "root"
PASSWORD = "mongo"
DB_NAME = "rental"

USERS = "Users"
VISIT_TYPES = "VisitTypes"
VISIT_ARCHIVE = "VisitArchive"

client = MongoClient("mongodb://" + USERNAME + ":" + PASSWORD + "@" + HOSTNAME + ":" + PORT + "/", connect=True)

class MongoQueries:
    def __init__(self):
        self.rentalDb = client[DB_NAME]
    
    