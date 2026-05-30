import asyncio
import pytest
from src.task import Task
from src.async_task_queue import AsyncTaskQueue
from src.async_executor import AsyncExecutor


class OkHandler:
    name = "ok"

    async def handle(self, task: Task) -> None:
        task.status = "running"
        task.status = "completed"


class FailHandler:
    name = "fail"

    async def handle(self, task: Task) -> None:
        raise RuntimeError("ошибка обработчика")


class NotAHandler:
    pass


class TestAsyncExecutor:
    def setup_method(self):
        self.queue = AsyncTaskQueue()
        self.task = Task(1, "task1", 3)

    @pytest.mark.asyncio
    async def test_process_sets_completed(self):
        executor = AsyncExecutor(self.queue, OkHandler())
        result = await executor.process(self.task)
        assert result.status == "completed"

    @pytest.mark.asyncio
    async def test_process_no_handler_returns_task(self):
        executor = AsyncExecutor(self.queue, handler=None)
        result = await executor.process(self.task)
        assert result.status == "pending"

    @pytest.mark.asyncio
    async def test_process_bad_handler_returns_task(self):
        executor = AsyncExecutor(self.queue, handler=NotAHandler())
        result = await executor.process(self.task)
        assert result.status == "pending"

    @pytest.mark.asyncio
    async def test_process_fail_sets_failed(self):
        executor = AsyncExecutor(self.queue, FailHandler())
        with pytest.raises(RuntimeError):
            await executor.process(self.task)
        assert self.task.status == "failed"

    @pytest.mark.asyncio
    async def test_worker_stops_after_stop_called(self):
        executor = AsyncExecutor(self.queue, OkHandler())
        executor.stop()
        await asyncio.wait_for(executor.worker(), timeout=1.0)