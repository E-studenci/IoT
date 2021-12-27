from redis import Redis

class EventLoop:
    def __init__(self, redis: Redis, logger) -> None:
        self.redis = redis
        self.logger = logger
        self.thread = None
    
    def start_event_loop(self):  
        rfids = self.parsed_array(self.get_all_channels())
        pubsub = self.redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(**rfids)
        
        self.thread = pubsub.run_in_thread(
            sleep_time=0.001, 
            exception_handler=self.exception_handler, 
            daemon=True
        )
    
    def parsed_array(self, array: list) -> dict:
        result = {}
        for item in array:
            result[item] = self.message_handler
        return result

    def get_all_channels(self):
        from database.mongo.read import get_all_visit_types
        visit_types = get_all_visit_types()
        return [visit_type.rfid_scanner for visit_type in visit_types] 
    
    def stop_event_loop(self):
        try:
            self.thread.stop()
            self.thread.join(timeout=1.0)
        except Exception as e:
            print(e)
        
    def is_running(self):
        return self.thread._running.is_set()

    @staticmethod
    def message_handler(message):
        print(message)
    
    @staticmethod
    def exception_handler(ex, pubsub, thread):
        try:
            thread.stop()
            thread.join(timeout=1.0)
        except Exception:
            pass
