from flask_httpauth import HTTPBasicAuth
from flask_login import LoginManager
from flask_cors import CORS

from api.utils.config import Environment
from api.app.app import App

ENV = Environment()
APP = App(
    "Iot",
    ENV
)
APP.config["SECRET_KEY"] = ENV.flask_secret_key

CORS(
    APP,
    origins=[
        "http://127.0.0.1:5500",
        "http://localhost:8080",
        "http://127.0.0.1:8080",
        ENV.host
    ],
    supports_credentials=True
)

LOGIN_MANAGER = LoginManager()
LOGIN_MANAGER.init_app(APP)
BASIC_AUTH = HTTPBasicAuth()

import api.initialize_modules

APP.start_redis_loop()

if __name__ == '__main__':
    # If you use 'use_reloader=True' option, the event loop for redis subscriber will spawn twice
    # resulting in doubled behavior: Every time a publisher sends a new message, event loop will receive it twice.
    APP.run(port=5000, host='127.0.0.1', use_reloader=False, debug=True)