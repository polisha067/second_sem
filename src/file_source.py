import json
from pathlib import Path
from typing import Iterable
from src.task import Task
from src.task_source import TaskSource
from src.logger import log

class FileSource:

    def __init__(self, path: str, logger=None):
        self.path = Path(path)
        self.name = f"file-{self.path.name}"
        self.logger = logger or log


    def get_tasks(self) -> Iterable[Task]:
        self.logger.info(f"reading {self.path}")

        if not self.path.exists():
            self.logger.error(f"file not found: {self.path}")
            return

        try:
            with open(self.path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            self.logger.error(f"file corrupted: {self.path} - {e}")
            return
        except Exception as e:
            self.logger.error(f"error reading file: {e}")
            return

        for item in data:
            if 'id' in item and 'payload' in item:
                yield Task(
                    task_id=item['id'],
                    description=item['payload'],
                    priority=3
                )
            else:
                self.logger.error(f"bad task format: {item}")

