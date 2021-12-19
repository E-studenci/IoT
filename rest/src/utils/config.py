from utils.singleton import Singleton
from os import getenv


class Environment(metaclass=Singleton):
    def __init__(self) -> None:
        self.mongo_host = getenv("MONGO_HOST", "127.0.0.1")
        self.mongo_port = int(getenv("MONGO_PORT", "27017"))
        self.mongo_user = getenv("MONGO_USER", "root")
        self.mongo_pass = getenv("MONGO_PASS", "admin")
        self.mongo_max_connections = int(getenv("MONGO_MAX_CONNECTIONS", "20"))
        self.redis_host = getenv("REDIS_HOST", "127.0.0.1")
        self.redis_port = int(getenv("REDIS_PORT", "6379"))
        self.redis_db   = getenv("REDIS_DB", "0")
        self.redis_user = getenv("REDIS_USER", "default")
        self.redis_pass = getenv("REDIS_PASS", "admin")
        self.redis_max_connections = int(getenv("REDIS_MAX_CONNECTIONS", "20"))
        self.flask_secret_key = getenv("SECRET_KEY", "SECRET_KEY")
