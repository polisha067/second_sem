from typing import List
from src.task import Task
from src.logger import log

class APISource:
    def __init__(self, url: str, logger=None):
        self.url = url
        self.name = f"api-{url}"
        self.logger = logger or log

    def get_tasks(self) -> List[Task]:
        self.logger.info(f"request to API: {self.url}")

        tasks = [
            Task(task_id=101, description="api task 1", priority=3),
            Task(task_id=102, description="api task 2", priority=3),
            Task(task_id=103, description="api task 3", priority=3)
        ]

        self.logger.info(f"received {len(tasks)} tasks from API")
        return tasks