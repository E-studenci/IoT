from asyncio import create_task, sleep, run
from threading import Thread
import asyncio


class Event:
    def __init__(self) -> None:
        self.stop = False

    def set(self):
        self.stop = True

    def is_set(self):
        return self.stop

    def clear(self):
        self.stop = False


class EventLoop:
    def __init__(self, logger) -> None:
        self.logger = logger
        self.stop_event = Event()

    def start_loop(self) -> None:
        def start_loop_inner(self):
            run(self.exit_layer())

        thread = Thread(
            target=start_loop_inner,
            args=(self, ),
            daemon=True
        )
        thread.start()

    def stop_loop(self) -> None:        
        self.stop_event.set()

    async def exit_layer(self) -> None:
        stop_task = create_task(self.exit())
        create_task(self.main())
        await stop_task

    async def exit(self) -> None:
        while True:
            await asyncio.sleep(1)
            if self.stop_event.is_set():
                return

    async def main(self) -> None:
        worker = create_task(self.worker())
        await worker

    async def worker(self) -> None: # Example
        while True:
            self.logger.info("Working")
            await sleep(2)
