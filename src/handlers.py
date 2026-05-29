import asyncio
from src.dependencies import DatabaseStub, NotifierStub
from src.task import Task
from src.logger import log

class SleepHandler:
    """
    обработчик оркестрирует зависимости (заглушки),
    потом выполняет задачу
    """

    name = "sleep"

    def __init__(self, delay=1.0, logger=None):
        self.delay = delay
        self.logger = logger or log

    async def handle(self, task: Task) -> None:
        db = DatabaseStub(logger=self.logger)
        notifier = NotifierStub(logger=self.logger)

        await db.connect()
        await notifier.notify(task.id, "start")

        task.status = "running"
        self.logger.info(f"task {task.id}: выполнение...")
        await asyncio.sleep(self.delay)

        await db.save_task(task.id)
        await notifier.notify(task.id, "done")

        task.status = "completed"
        self.logger.info(f"task {task.id} -> completed")
