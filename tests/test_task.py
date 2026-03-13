import pytest
from src.task import Task

def test_task_creation():

    task = Task(id=1, payload="test")
    assert task.id == 1
    assert task.payload == "test"