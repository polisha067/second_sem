import asyncio
from src.logger import log

class DatabaseStub:
    """заглушка БД"""

    def __init__(self, logger=None):
        self.logger = logger or log

    async def connect(self):
        self.logger.info("db: connect")
        await asyncio.sleep(0.01)

    async def save_task(self, task_id: int):
        self.logger.info(f"db: save task {task_id}")
        await asyncio.sleep(0.01)


class NotifierStub:
    """заглушка уведомлений"""

    def __init__(self, logger=None):
        self.logger = logger or log

    async def notify(self, task_id: int, message: str):
        self.logger.info(f"notify {task_id}: {message}")
        await asyncio.sleep(0.01)
