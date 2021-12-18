from database.mongo.read import get_user_by_email
from main import LOGIN_MANAGER


@LOGIN_MANAGER.user_loader
def load_user(user_id):
    return get_user_by_email(user_id)
