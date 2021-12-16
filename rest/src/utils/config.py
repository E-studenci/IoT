from utils.singleton import Singleton
from os import getenv


class Environment(metaclass=Singleton):
    def __init__(self) -> None:
        self.mongo_host = getenv("MONGO_HOST", "127.0.0.1")
        self.mongo_port = getenv("MONGO_PORT", "27017")
        self.mongo_user = getenv("MONGO_USER", "root")
        self.mongo_pass = getenv("MONGO_PASS", "admin")
        self.redis_host = getenv("REDIS_HOST", "127.0.0.1")
        self.redis_port = getenv("REDIS_PORT", "6379")
        self.redis_db   = getenv("REDIS_DB", "0")
        self.mongo_user = getenv("REDIS_USER", "root")
        self.mongo_pass = getenv("REDIS_PASS", "admin")
        