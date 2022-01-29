from os import getenv
import dotenv

from api.utils.singleton import Singleton

dotenv.load_dotenv()
SEPERATOR = ","


class Environment(metaclass=Singleton):
    def __init__(self) -> None:
        self.origins = get_all_origins(
            getenv("ORIGINS", "http://127.0.0.1:8080,http://localhost:8080,http://127.0.0.1:5500")
        )
        self.mongo_host = getenv("MONGO_HOST", "127.0.0.1")
        self.mongo_port = int(getenv("MONGO_PORT", "27017"))
        self.mongo_user = getenv("MONGO_USER", "root")
        self.mongo_pass = getenv("MONGO_PASS", "mongo")
        self.mongo_max_connections = int(getenv("MONGO_MAX_CONNECTIONS", "20"))
        self.redis_host = getenv("REDIS_HOST", "127.0.0.1")
        self.redis_port = int(getenv("REDIS_PORT", "6379"))
        self.redis_db   = getenv("REDIS_DB", "0")
        self.redis_crt  = getenv("REDIS_CRT", "redis.crt")
        self.redis_max_connections = int(getenv("REDIS_MAX_CONNECTIONS", "20"))
        self.client_key = getenv("CLIENT_KEY", "client.key")
        self.client_crt = getenv("CLIENT_CRT", "client.crt")
        self.key_folder = getenv("KEY_FOLDER", "tls")
        self.flask_secret_key = getenv("SECRET_KEY", "SECRET_KEY")


def get_all_origins(hosts: str):
    results = []
    for host in hosts.split(SEPERATOR):
        if host and host != "":
            results.append(host)
    return results