import asyncio
import pytest
from src.async_task_runner import AsyncTaskRunner


class TestAsyncTaskRunner:
    def setup_method(self):
        self.runner = AsyncTaskRunner()
        self.runner.start()

    def teardown_method(self):
        self.runner.stop()

    def test_submit_returns_result(self):
        async def coro():
            return 42

        fut = self.runner.submit(coro())
        assert fut.result(timeout=2.0) == 42

    def test_submit_multiple_coroutines(self):
        async def coro(n):
            return n

        futs = [self.runner.submit(coro(i)) for i in range(3)]
        results = [f.result(timeout=2.0) for f in futs]
        assert sorted(results) == [0, 1, 2]

    def test_runs_in_separate_thread(self):
        import threading
        captured = {}

        async def get_thread():
            captured["thread"] = threading.current_thread()

        self.runner.submit(get_thread()).result(timeout=1.0)
        assert captured["thread"] is not threading.main_thread()

    def test_stop_does_not_hang(self):
        # teardown уже вызовет stop(), просто проверяем что не зависает
        pass