from redis import BlockingConnectionPool
from app.query_holder import QueryHolder
from pymongo import MongoClient
from flask import Flask
import typing as t
import os

class App(Flask):
    def __init__(
            self, 
            import_name: str, 
            redis_host: str, 
            redis_port: int, 
            redis_db: int,
            redis_user: str, 
            redis_pass: str,
            redis_max_connections: int,
            mongo_host: str, 
            mongo_port: int,
            mongo_user: str, 
            mongo_pass: str, 
            mongo_max_connections: int,
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
            maxPoolSize=mongo_max_connections,
            maxIdleTimeMS=6000
        )
        self.mongo_queries = QueryHolder()
        
        self.redis = BlockingConnectionPool(
                host=redis_host,
                port=redis_port,
                db=redis_db,
                username=redis_user,
                password=redis_pass,
                max_connections=redis_max_connections
        )
        self.redis_queries = QueryHolder()
        
    def __del__(self):
        self.mongo.close()
        self.redis.disconnect()
    
    def mongo_query(self, func):
        def wrapper():
            with self.mongo.start_session() as session:
                with session.start_transaction():
                    func(session.client)
        self.mongo_queries._add_query(func.__name__, wrapper)
        return wrapper
    
    def redis_query(self, func):
        def wrapper():
            connection = self.redis.get_connection()
            func(connection)
            self.redis.release(connection)
        self.redis_queries._add_query(func.__name__, wrapper)
        return wrapper