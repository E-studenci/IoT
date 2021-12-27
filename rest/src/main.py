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

APP.start_redis_loop()

if __name__ == '__main__':
    # If you use 'use_reloader=True' option, the event loop for redis subscriber will spawn twice
    # resulting in doubled behaviour: Every time a publisher sends a new message, event loop will reacive it twice.
    APP.run(port=5000, host='127.0.0.1', use_reloader=False, debug=True)