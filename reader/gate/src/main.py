from config import Environment
from event_loop import EventLoop
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

CLIENTS = [
    "f91a61e515d1fc6a7fa9986473b6d0ff",
    "4ab47e54c2f73ad4c0eb3974709721cd",
    "9827bce49e2b5b9ea09f69db59c20e85",
    "85bc3f25732df73426aa44f59c6ec78c",
    "bdef2adeeede3e4502c6d891b0a0e3e4",
    "44963461cf009e75c11447da27aec4ed",
    "ad4338accfdbd2bf2d5d559a6ff31561",
    "fbdab93478256eda11a7e173935e621c"
]

import os.path

os.path.join('/reader/gate/tls', 'client_1.crt')

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

EVENT_LOOP = EventLoop(REDIS, ENV, window)
EVENT_LOOP.start_event_loop()

def create_main_window():
    window.geometry("220x100")
    window.title("SENDER")

    # intro_label = tkinter.Label(window, text="rfid:")
    # intro_label.grid(row=0)
    rfid_input = tkinter.Entry(window, width=35)
    rfid_input.grid(row=0, column=1)

    button_1 = tkinter.Button(window, text="send",
                              command=lambda: publish(rfid_input.get()), width= 30)
    button_1.grid(row=2, column=1)
    
    indicator = tkinter.Text(name="indicator",width=27, height=1, state="disabled")
    indicator.grid(row=4,column=1)
    button_stop = tkinter.Button(window, text="Stop", command=window.quit, width=30)
    button_stop.grid(row=5, column=1)
    


def publish(client: str):
    data = {
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "client": client
    }
    
    logging.info(f"Client {client} wants to OPEN THE GATE!")
    REDIS.publish(f"{ENV.rfid}-gate", json.dumps(data))



async def main():
    create_main_window()
    window.mainloop()
    # while True:
    #     await asyncio.sleep(SLEEP_TIME)
    #     await publish(random.choice(CLIENTS))


if __name__ == '__main__':
    asyncio.run(main())
