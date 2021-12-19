from utils.errors import MongoConnectionError, RedisConnectionError
from redis import BlockingConnectionPool, Redis
from pymongo.errors import PyMongoError
from app.event_loop import EventLoop
from asyncio import get_event_loop
from pymongo import MongoClient
from redis import RedisError
from flask import Flask
import typing as t
import asyncio
import os

async def firstWorker():
    while True:
        await asyncio.sleep(1)
        print("First Worker Executed")

async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")


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
            connectTimeoutMS=5000,
            serverSelectionTimeoutMS=5000,
            maxIdleTimeMS=6000
        )
        
        self.redis = BlockingConnectionPool(
                host=redis_host,
                port=redis_port,
                db=redis_db,
                username=redis_user,
                password=redis_pass,
                max_connections=redis_max_connections
        )
        
        self.event_loop = EventLoop(self.logger)
    
    def start_event_loop(self):
        self.event_loop.start_loop()
    
    def stop_event_loop(self):
        self.event_loop.stop_loop()
    
    def mongo_query(self, func):
        def wrapper(*args , **kwargs):
            try:
                with self.mongo.start_session() as session:
                    with session.start_transaction():
                        result = func(session.client, *args , **kwargs)
                        return result
            except PyMongoError as pymongo_error:
                self.logger.error(pymongo_error)
                raise MongoConnectionError()
        return wrapper
    
    def redis_query(self, func):
        def wrapper(*args , **kwargs):
            try:
                connection = Redis(connection_pool=self.redis)
                result = func(connection, *args, **kwargs)
                connection.close()
                return result
            except RedisError as redis_error:
                self.logger.error(redis_error)
                raise RedisConnectionError()
        return wrapper
    
    def __del__(self):
        self.mongo.close()
        self.redis.disconnect()
        self.event_loop.stop_loop()