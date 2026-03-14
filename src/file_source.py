import json
from pathlib import Path
from typing import Iterable
from src.task import Task
from src.task_source import TaskSource
from src.logger import log

class FileSource:
    def __init__(self, path: str):
        self.path = Path(path)
        self.name = f"file-{self.path.name}"
    
    def get_tasks(self) -> Iterable[Task]:
        log.info(f"reading {self.path}")
        try:
            with open(self.path) as f:
                for item in json.load(f):
                    if 'id' in item and 'payload' in item:
                        yield Task(item['id'], item['payload'])
        except Exception as e:
            log.error(f"error: {e}")