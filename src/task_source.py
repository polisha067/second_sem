from typing import Protocol, runtime_checkable, Iterable
from src.task import Task

@runtime_checkable
class TaskSource(Protocol):
    name: str
    def get_tasks(self) -> Iterable[Task]: ...