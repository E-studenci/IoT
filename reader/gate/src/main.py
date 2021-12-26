from config import Environment
from datetime import datetime
from redis import Redis
import logging
import asyncio
import random
import json

logging.basicConfig(level=logging.INFO)

SLEEP_TIME = 20

ENV = Environment()

CLIENTS = [
    "f91a61e515d1fc6a7fa9986473b6d0ff",
    "9827bce49e2b5b9ea09f69db59c20e85",
    "85bc3f25732df73426aa44f59c6ec78c",
    "bdef2adeeede3e4502c6d891b0a0e3e4",
    "44963461cf009e75c11447da27aec4ed"
]

REDIS = Redis(
    host     = ENV.redis_host, 
    port     = ENV.redis_port,
    db       = ENV.redis_db,
    username = ENV.redis_user,
    password = ENV.redis_pass
)


async def publish(client: str):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "client": client
    }
    
    logging.info(json.dumps(data))
    REDIS.publish(ENV.rfid, json.dumps(data))


async def main():
    while True:
        await asyncio.sleep(SLEEP_TIME)
        await publish(random.choice(CLIENTS))


if __name__ == '__main__':
    asyncio.run(main())
