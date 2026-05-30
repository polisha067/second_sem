import pytest
from src.executor_resource import ExecutorResource


class TestExecutorResource:

    @pytest.mark.asyncio
    async def test_enter_returns_self(self):
        res = ExecutorResource()
        async with res as r:
            assert r is res

    @pytest.mark.asyncio
    async def test_does_not_suppress_exception(self):
        with pytest.raises(ValueError):
            async with ExecutorResource():
                raise ValueError("тест")

    @pytest.mark.asyncio
    async def test_can_be_used_twice(self):
        res = ExecutorResource()
        async with res:
            pass
        async with res:
            pass