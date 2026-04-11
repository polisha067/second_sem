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
        
        #имитация ответа апи
        tasks = [
            Task(101, "api task 1"),
            Task(102, "api task 2"),
            Task(103, "api task 3")
        ]
        
        self.logger.info(f"received {len(tasks)} tasks from API")
        return tasks