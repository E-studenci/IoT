from database.models import *
from redis import Redis
from main import APP


@APP.redis_query
def subscribe(client: Redis, channel: str):
    pubsub = client.pubsub()
    pubsub.subscribe(channel)