import pytest
from src.task import Task
from src.task_queue import TaskQueue


def test_full_workflow():
    queue = TaskQueue()
    
    # добавление
    queue.add(Task(1, "задача 1", 3))
    queue.add(Task(2, "задача 2", 5))
    queue.add(Task(3, "задача 3", 1))
    
    assert len(queue) == 3
    
    # фильтрация
    high = list(queue.by_priority(5))
    assert len(high) == 1
    assert high[0].id == 2
    
    # изменение статуса
    task = queue.get_by_id(1)
    task.status = "running"
    
    pending = list(queue.pending_tasks())
    assert len(pending) == 2
    
    # удаление
    queue.remove(2)
    assert len(queue) == 2
    assert queue.get_by_id(2) is None