from main import APP

@APP.redis_query
def custom_query():
    return None