from typing import Iterable
from src.logger import log
from src.task import Task
from src.task_source import TaskSource


class GeneratorSource:
    def __init__(self, count: int, logger=None):
        self.logger = logger or log
        self.count = count
        self.name = f"generator"
        
    
    def get_tasks(self) -> Iterable[Task]:
        self.logger.info(f"generating {self.count} tasks")
        if self.count <= 0:
            self.logger.error("count must be > 0")
            return
        for i in range(1, self.count + 1):
            yield Task(i, f"task data {i}")