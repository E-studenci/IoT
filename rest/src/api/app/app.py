from api.utils.errors import MongoConnectionError
from pymongo.errors import PyMongoError
from pymongo import MongoClient
from functools import wraps
from redis import Redis
from flask import Flask
import typing as t
import os

from api.app.event_loop import EventLoop
from api.utils.config import Environment


class App(Flask):
    def __init__(
            self, 
            import_name: str, 
            env: Environment, 
            static_url_path: t.Optional[str] = None, 
            static_folder: t.Optional[t.Union[str, os.PathLike]] = "static", 
            static_host: t.Optional[str] = None, 
            host_matching: bool = False, 
            subdomain_matching: bool = False, 
            template_folder: t.Optional[str] = "templates", 
            instance_path: t.Optional[str] = None, 
            instance_relative_config: bool = False,
            root_path: t.Optional[str] = None
        ) -> None:
        super().__init__(
            import_name, 
            static_url_path=static_url_path, 
            static_folder=static_folder, 
            static_host=static_host, 
            host_matching=host_matching,
            subdomain_matching=subdomain_matching,
            template_folder=template_folder, 
            instance_path=instance_path, 
            instance_relative_config=instance_relative_config,
            root_path=root_path
        )
        self.env = env
        
        self.mongo = MongoClient(
            host=env.mongo_host,
            port=env.mongo_port,
            username=env.mongo_user,
            password=env.mongo_pass,
            maxPoolSize=env.mongo_max_connections,
            connectTimeoutMS=5000,
            serverSelectionTimeoutMS=5000,
            maxIdleTimeMS=6000
        )
        
        self.redis = Redis(
            host=env.redis_host,
            port=env.redis_port,
            db=env.redis_db,
            max_connections=env.redis_max_connections,
            ssl_keyfile  = os.path.join(env.key_folder, env.client_key),
            ssl_certfile = os.path.join(env.key_folder, env.client_crt),
            ssl_ca_certs = os.path.join(env.key_folder, env.redis_crt),
            ssl=True
        )
        
        self.redis_loop = EventLoop(self.redis, self.logger)
        
    def start_redis_loop(self) -> None:
        self.redis_loop.start_event_loop()
    
    def mongo_query(self, func) -> t.Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> t.Any:
            try:
                with self.mongo.start_session() as session:
                    with session.start_transaction():
                        result = func(session.client, *args , **kwargs)
                        return result
            except PyMongoError as pymongo_error:
                self.logger.error(pymongo_error)
                raise MongoConnectionError()
        return wrapper
    
    def __del__(self) -> None:
        if self.mongo:
            self.mongo.close()
        if self.redis_loop:
            self.redis_loop.stop_event_loop()
