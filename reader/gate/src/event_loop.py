from redis import Redis
from config import Environment
import logging

class EventLoop:
    def __init__(self, redis: Redis, env: Environment, window) -> None:
        self.redis = redis
        self.env = env
        self.thread = None
        self.window = window
    
    def start_event_loop(self):  
        pubsub = self.redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(**{f"{self.env.rfid}-server": self.message_handler})
        
        self.thread = pubsub.run_in_thread(
            sleep_time=0.001, 
            exception_handler=self.exception_handler, 
            daemon=True
        )
        
    def message_handler(self, message):
        result = message['data'].decode()
        
        if result == 'true':
            logging.info('Welcome to the desert of the real!')
            self.window.nametowidget("indicator").config(background="green")
        else:
            logging.info('You shall not pass!')
            self.window.nametowidget("indicator").config(background="red")

    def stop_event_loop(self):
        try:
            self.thread.stop()
            self.thread.join(timeout=1.0)
        except Exception as e:
            logging.error(e)
        
    def is_running(self):
        return self.thread._running.is_set()
    
    @staticmethod
    def exception_handler(ex, pubsub, thread):
        try:
            thread.stop()
            thread.join(timeout=1.0)
        except Exception:
            pass
