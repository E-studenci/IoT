from config import Environment
from datetime import datetime
from redis import Redis
import logging
import asyncio
import random
import json
import tkinter

FORMAT = '[%(levelname)s]:[%(asctime)s]:[%(message)s]'

logging.basicConfig(level=logging.INFO, format=FORMAT)

SLEEP_TIME = 10

ENV = Environment()

import os.path

os.path.join('/reader/scanner/tls', 'client_1.crt')

REDIS = Redis(
    host         = ENV.redis_host, 
    port         = ENV.redis_port,
    db           = ENV.redis_db,
    ssl_keyfile  = os.path.join(ENV.key_folder, ENV.client_key),
    ssl_certfile = os.path.join(ENV.key_folder, ENV.client_crt),
    ssl_ca_certs = os.path.join(ENV.key_folder, ENV.redis_crt),
    ssl          = True
)


window = tkinter.Tk()

def create_main_window():
    window.geometry("220x75")
    window.title("SCAN")

    # intro_label = tkinter.Label(window, text="rfid:")
    # intro_label.grid(row=0)
    rfid_input = tkinter.Entry(window, width=35)
    rfid_input.grid(row=0, column=1)

    button_1 = tkinter.Button(window, text="send",
                              command=lambda: publish(rfid_input.get()), width= 30)
    button_1.grid(row=2, column=1)
    
    button_stop = tkinter.Button(window, text="Stop", command=window.quit, width=30)
    button_stop.grid(row=5, column=1)
    


def publish(client: str):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "client": client
    }
    
    logging.info(f"Scanned card: {client}")
    REDIS.publish(f"{ENV.rfid}-gate", json.dumps(data))



async def main():
    create_main_window()
    window.mainloop()
    # while True:
    #     await asyncio.sleep(SLEEP_TIME)
    #     await publish(random.choice(CLIENTS))


if __name__ == '__main__':
    asyncio.run(main())
