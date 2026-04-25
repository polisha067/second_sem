from typing import Optional, Iterator, Iterable, List
from src.task import Task
from src.logger import log


class TaskQueue:
    """очередь задач с поддержкой итерации и фильтрации"""

    def __init__(self, logger=None):

        self._tasks: List[Task] = []
        self.logger = logger or log

    def add(self, task: Task) -> None:

        self.logger.debug(f"добавлена задача {task.id}")
        self._tasks.append(task)

    def remove(self, task_id: int) -> bool:

        for i, task in enumerate(self._tasks):

            if task.id == task_id:
                self._tasks.pop(i)
                self.logger.info(f"удалена задача {task_id}")
                return True
            
        self.logger.warning(f"задача {task_id} не найдена")
        return False

    def get_by_id(self, task_id: int) -> Optional[Task]:

        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def __len__(self) -> int:
        return len(self._tasks)

    def __iter__(self) -> Iterator[Task]:
        return iter(self._tasks)

    def filter(self, status: Optional[str] = None, priority: Optional[int] = None) -> Iterator[Task]:

        for task in self._tasks:
            if status is not None and task.status != status:
                continue
            if priority is not None and task.priority != priority:
                continue
            yield task

    def pending_tasks(self) -> Iterator[Task]:
        yield from self.filter(status="pending")

    def by_priority(self, priority: int) -> Iterator[Task]:
        yield from self.filter(priority=priority)

    def __repr__(self) -> str:
        return f"TaskQueue(tasks={len(self._tasks)})"