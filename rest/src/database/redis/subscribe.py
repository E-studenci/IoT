from database.models import *
from redis import Redis
from main import APP


@APP.redis_query
def template(client: Redis):
    return True