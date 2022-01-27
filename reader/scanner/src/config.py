from os import getenv
import dotenv

dotenv.load_dotenv()

class Environment:
    def __init__(self) -> None:
        self.rfid       = getenv("RFID", "dac9630aec642a428cd73f4be0a03569")
        self.redis_host = getenv("REDIS_HOST", "127.0.0.1")
        self.redis_port = int(getenv("REDIS_PORT", "6379"))
        self.redis_db   = getenv("REDIS_DB", "0")
        self.client_key = getenv("CLIENT_KEY", "client.key")
        self.client_crt = getenv("CLIENT_CRT", "client.crt")
        self.redis_crt  = getenv("REDIS_CRT", "redis.crt")
        self.key_folder = getenv("KEY_FOLDER", "tls")
        self.redis_pass = getenv("REDIS_PASS", "admin")