from utils.config import Environment
from app.app import App

env = Environment()

app = App(
    "Iot", 
    env.redis_host, 
    env.redis_port, 
    env.redis_db, 
    env.mongo_host, 
    env.mongo_port
)

app.run()