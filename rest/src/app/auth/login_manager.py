from database.mongo.read import get_admin_by_id
from main import LOGIN_MANAGER


@LOGIN_MANAGER.user_loader
def load_user(admin_id):
    return get_admin_by_id(admin_id)
