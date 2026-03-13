from typing import Iterable
from task import Task
from task_source import TaskSource
from logger import log

class GeneratorSource:
    def __init__(self, count: int):
        self.count = count
        self.name = f"generator"
    
    def get_tasks(self) -> Iterable[Task]:
        log.info(f"generating {self.count} tasks")
        if self.count <= 0:
            log.error("count must be > 0")
            return
        for i in range(1, self.count + 1):
            yield Task(i, f"task data {i}")