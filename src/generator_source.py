from typing import Iterable
from src.task import Task
from src.task_source import TaskSource
from src.logger import log

class GeneratorSource:
    def __init__(self, count: int, logger=None):
        self.count = count
        self.name = "generator"
        self.logger = logger or log

    def get_tasks(self) -> Iterable[Task]:
        self.logger.info(f"generating {self.count} tasks")
        if self.count <= 0:
            self.logger.error("count must be > 0")
            return
        for i in range(1, self.count + 1):
            yield Task(
                task_id=i,
                description=f"task data {i}",
                priority=3
            )