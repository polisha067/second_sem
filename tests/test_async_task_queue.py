import pytest
import asyncio
from src.task import Task
from src.async_task_queue import AsyncTaskQueue


class TestAsyncTaskQueue:
    def setup_method(self):
        self.queue = AsyncTaskQueue()
        self.t1 = Task(1, "task1", 3)
        self.t2 = Task(2, "task2", 3)

    @pytest.mark.asyncio
    async def test_put_increases_size(self):
        await self.queue.put(self.t1)
        assert self.queue.qsize() == 1

    @pytest.mark.asyncio
    async def test_get_returns_task(self):
        await self.queue.put(self.t1)
        task = await self.queue.get()
        assert task.id == 1

    @pytest.mark.asyncio
    async def test_fifo_order(self):
        await self.queue.put(self.t1)
        await self.queue.put(self.t2)
        first = await self.queue.get()
        second = await self.queue.get()
        assert first.id == 1
        assert second.id == 2

    @pytest.mark.asyncio
    async def test_empty_initially(self):
        assert self.queue.empty() is True

    @pytest.mark.asyncio
    async def test_not_empty_after_put(self):
        await self.queue.put(self.t1)
        assert self.queue.empty() is False

    @pytest.mark.asyncio
    async def test_task_done_and_join(self):
        await self.queue.put(self.t1)
        await self.queue.get()
        self.queue.task_done()
        await asyncio.wait_for(self.queue.join(), timeout=1.0)