import pytest
from src.task import Task
from src.task_queue import TaskQueue


class TestTaskQueue:
    def setup_method(self):
        self.queue = TaskQueue()
        self.t1 = Task(1, "task1", 3)
        self.t2 = Task(2, "task2", 5)
        self.t3 = Task(3, "task3", 1)

    def test_add_and_len(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        assert len(self.queue) == 2

    def test_remove_exists(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        assert self.queue.remove(1) == True
        assert len(self.queue) == 1
        assert self.queue.get_by_id(1) is None

    def test_remove_not_exists(self):
        self.queue.add(self.t1)
        assert self.queue.remove(99) == False
        assert len(self.queue) == 1

    def test_get_by_id(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        assert self.queue.get_by_id(2) == self.t2
        assert self.queue.get_by_id(99) is None

    def test_iteration(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        self.queue.add(self.t3)
        ids = [task.id for task in self.queue]
        assert ids == [1, 2, 3]

    def test_filter_by_status(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        self.queue.add(self.t3)
        self.t1.status = "running"

        pending = list(self.queue.filter(status="pending"))
        assert len(pending) == 2

    def test_filter_by_priority(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        self.queue.add(self.t3)
        high = list(self.queue.filter(priority=5))
        assert len(high) == 1
        assert high[0].id == 2

    def test_pending_tasks(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        self.t1.status = "running"
        pending = list(self.queue.pending_tasks())
        assert len(pending) == 1
        assert pending[0].id == 2

    def test_by_priority(self):
        self.queue.add(self.t1)
        self.queue.add(self.t2)
        self.queue.add(self.t3)
        priority_3 = list(self.queue.by_priority(3))
        assert len(priority_3) == 1
        assert priority_3[0].id == 1