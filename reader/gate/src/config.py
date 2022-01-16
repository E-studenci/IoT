from os import getenv
import dotenv

dotenv.load_dotenv()

class Environment:
    def __init__(self) -> None:
        self.rfid       = getenv("RFID", "94fe310b4ec17fd218da48cc14ccbb5d")
        self.redis_host = getenv("REDIS_HOST", "127.0.0.1")
        self.redis_port = int(getenv("REDIS_PORT", "6379"))
        self.redis_db   = getenv("REDIS_DB", "0")
        self.redis_crt   = getenv("REDIS_CRT", "redis.crt")
        self.redis_user = getenv("REDIS_USER", "default")
        self.redis_pass = getenv("REDIS_PASS", "admin")