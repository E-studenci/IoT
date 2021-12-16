from redis import Redis, ConnectionPool
from pymongo import MongoClient
from flask import Flask
import typing as t
import os

class App(Flask):
    def __init__(
            self, 
            import_name: str, 
            redis_host: str = '127.0.0.1', 
            redis_port: int = 6379, 
            redis_db: int = 0,
            redis_user: str = 'root', 
            redis_pass: str = 'admin',
            mongo_host: str = '127.0.0.1', 
            mongo_port: int = 27017,
            mongo_user: str = 'root', 
            mongo_pass: str = 'admin', 
            static_url_path: t.Optional[str] = None, 
            static_folder: t.Optional[t.Union[str, os.PathLike]] = "static", 
            static_host: t.Optional[str] = None, 
            host_matching: bool = False, 
            subdomain_matching: bool = False, 
            template_folder: t.Optional[str] = "templates", 
            instance_path: t.Optional[str] = None, 
            instance_relative_config: bool = False, 
            root_path: t.Optional[str] = None
        ):
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
        self.mongo = MongoClient(
            host=mongo_host,
            port=mongo_port,
            username=mongo_user,
            password=mongo_pass,
            maxIdleTimeMS=30000
        )
        self.redis = Redis(
            connection_pool=ConnectionPool(
                host=redis_host,
                port=redis_port,
                db=redis_db,
                username=redis_user,
                password=redis_pass
            )
        )
