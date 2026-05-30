import pytest
from src.task import Task
from src.handlers import SleepHandler
from src.task_handler import TaskHandler
 
 
class TestSleepHandler:
    def setup_method(self):
        self.handler = SleepHandler(delay=0.01)
        self.task = Task(1, "task1", 3)
 
    def test_has_name(self):
        assert isinstance(self.handler.name, str)
        assert self.handler.name != ""
 
    def test_implements_protocol(self):
        assert isinstance(self.handler, TaskHandler)
 
    @pytest.mark.asyncio
    async def test_handle_sets_completed(self):
        await self.handler.handle(self.task)
        assert self.task.status == "completed"
 
    @pytest.mark.asyncio
    async def test_handle_starts_as_pending(self):
        assert self.task.status == "pending"
        await self.handler.handle(self.task)
 
    @pytest.mark.asyncio
    async def test_handle_changes_status_to_running_then_completed(self):
        statuses = []
        original_handle = self.handler.handle
 
        async def tracking_handle(task):
            task.status = "running"
            statuses.append(task.status)
            task.status = "completed"
 
        self.handler.handle = tracking_handle
        await self.handler.handle(self.task)
        assert "running" in statuses
        assert self.task.status == "completed"
 
