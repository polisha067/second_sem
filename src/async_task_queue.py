import asyncio
from src.task import Task
from src.logger import log

class AsyncTaskQueue:
    """асинхронная очередь задач"""

    def __init__(self, logger=None):
        self._queue = asyncio.Queue()
        self.logger = logger or log

    async def put(self, task: Task) -> None:
        await self._queue.put(task)
        self.logger.debug(f"в async-очередь: {task.id}")

    async def get(self) -> Task:
        task = await self._queue.get()
        self.logger.debug(f"из async-очереди: {task.id}")
        return task

    def task_done(self) -> None:
        self._queue.task_done()

    async def join(self) -> None:
        await self._queue.join()

    def qsize(self) -> int:
        return self._queue.qsize()

    def empty(self) -> bool:
        return self._queue.empty()
