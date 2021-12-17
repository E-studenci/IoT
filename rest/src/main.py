from utils.config import Environment
from pymongo import MongoClient
from app.app import App

env = Environment()

APP = App(
    "Iot", 
    env.redis_host, 
    env.redis_port, 
    env.redis_db, 
    env.redis_user,
    env.redis_pass,
    env.redis_max_connections,
    env.mongo_host, 
    env.mongo_port,
    env.mongo_user,
    env.mongo_pass,
    env.mongo_max_connections
)

import initialize_modules