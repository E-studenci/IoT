from redis import Redis
import datetime
import json


class EventLoop:
    def __init__(self, redis: Redis, logger) -> None:
        self.redis = redis
        self.logger = logger
        self.thread = None
    
    def start_event_loop(self):  
        rfids = self.parsed_array(self.get_all_channels())
        pubsub = self.redis.pubsub(ignore_subscribe_messages=True)
        pubsub.subscribe(**rfids)
        
        self.logger.info(self.redis.pubsub_channels())
        
        self.thread = pubsub.run_in_thread(
            sleep_time=0.001, 
            exception_handler=self.exception_handler, 
            daemon=True
        )
    
    def parsed_array(self, array: list) -> dict:
        result = {}
        for item in array:
            result[f"{item}-gate"] = self.message_handler
        return result

    def get_all_channels(self):
        from api.database.mongo.read import get_all_visit_types
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

    def message_handler(self, message):
        import api.database.mongo.read as read
        import api.database.mongo.create as create
        import api.database.mongo.update as update
        from api.utils.card import LAST_SCANNED_CARD
        try:
            channel: str = str(message['channel'].decode()).rstrip('-gate')
            data = json.loads(message['data'].decode())
            
            visit_type = read.get_visit_type_by_rfid_scanner(channel)
            
            if visit_type.visit_type != "SCANNER":
                user = read.get_card_user(data['client'])
                if not user:
                    self.redis.publish(f"{channel}-server", 'false')
                    return
                
                if user.current_visit:
                    update.end_visit(user._id, datetime.datetime.now())
                else:
                    create.start_visit(visit_type._id, user._id)
                self.redis.publish(f"{channel}-server", 'true')
            else:
                LAST_SCANNED_CARD.rfid = data['client']
                LAST_SCANNED_CARD.scanned = datetime.datetime.now()
        except Exception as e:
            self.logger.info(e)
            
    @staticmethod
    def exception_handler(ex, pubsub, thread):
        print(ex)
        try:
            thread.stop()
            thread.join(timeout=1.0)
        except Exception as exc:
            print(exc)
