from flask_httpauth import HTTPBasicAuth
from utils.config import Environment
from flask_login import LoginManager
from app.app import App

ENV = Environment()

APP = App(
    "Iot", 
    ENV.redis_host, 
    ENV.redis_port, 
    ENV.redis_db, 
    ENV.redis_user,
    ENV.redis_pass,
    ENV.redis_max_connections,
    ENV.mongo_host, 
    ENV.mongo_port,
    ENV.mongo_user,
    ENV.mongo_pass,
    ENV.mongo_max_connections
)
APP.config["SECRET_KEY"] = ENV.flask_secret_key

LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.init_app(APP)
BASIC_AUTH = HTTPBasicAuth()

import initialize_modules

APP.start_event_loop()