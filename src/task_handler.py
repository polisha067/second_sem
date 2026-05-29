from typing import Protocol, runtime_checkable, Iterable
from src.task import Task

@runtime_checkable
class TaskHandler(Protocol):
    name: str
    async def handle(self, task: Task) -> None: ...
