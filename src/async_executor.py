import asyncio
from src.async_task_queue import AsyncTaskQueue
from src.executor_resource import ExecutorResource
from src.logger import log, log_error
from src.task import Task
from src.task_handler import TaskHandler

class AsyncExecutor:
    """берёт задачу из очереди, отдаёт обработчику (он оркестрирует зависимости)"""

    def __init__(self, queue: AsyncTaskQueue, handler=None, logger=None):
        self.queue = queue
        self.handler = handler
        self.logger = logger or log
        self._stop = False

    async def process(self, task: Task) -> Task:
        async with ExecutorResource(logger=self.logger):
            if self.handler is None:
                self.logger.warning("обработчик не задан")
                return task

            if not isinstance(self.handler, TaskHandler):
                self.logger.warning(f"not a handler: {type(self.handler).__name__}")
                return task

            try:
                await self.handler.handle(task)
            except Exception as e:
                log_error(f"handler {self.handler.name}: {e}")
                task.status = "failed"
                raise
        return task

    async def worker(self):
        while not self._stop:
            try:
                task = await asyncio.wait_for(self.queue.get(), timeout=0.2)
            except asyncio.TimeoutError:
                continue

            try:
                await self.process(task)
            except Exception:
                pass
            finally:
                self.queue.task_done()

    def stop(self):
        self._stop = True
