from config import Environment
from event_loop import EventLoop
from datetime import datetime
from redis import Redis
import logging
import asyncio
import random
import json

FORMAT = '[%(levelname)s]:[%(asctime)s]:[%(message)s]'

logging.basicConfig(level=logging.INFO, format=FORMAT)

SLEEP_TIME = 10

ENV = Environment()


CLIENTS = [
    "f91a61e515d1fc6a7fa9986473b6d0ff",
    "4ab47e54c2f73ad4c0eb3974709721cd",
    "9827bce49e2b5b9ea09f69db59c20e85",
    "85bc3f25732df73426aa44f59c6ec78c",
    "bdef2adeeede3e4502c6d891b0a0e3e4",
    "44963461cf009e75c11447da27aec4ed",
    "ad4338accfdbd2bf2d5d559a6ff31561",
    "fbdab93478256eda11a7e173935e621c"
]

REDIS = Redis(
    host         = ENV.redis_host, 
    port         = ENV.redis_port,
    db           = ENV.redis_db,
    ssl_ca_certs = ENV.redis_crt,
    ssl          = True
)

EVENT_LOOP = EventLoop(REDIS, ENV)
EVENT_LOOP.start_event_loop()

async def publish(client: str):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "client": client
    }
    
    logging.info(f"Client {client} wants to OPEN THE GATE!")
    
    REDIS.publish(f"{ENV.rfid}-gate", json.dumps(data))


async def main():
    while True:
        await asyncio.sleep(SLEEP_TIME)
        await publish(random.choice(CLIENTS))


if __name__ == '__main__':
    asyncio.run(main())
