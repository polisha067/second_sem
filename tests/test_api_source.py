import pytest
from src.api_source import APISource
from src.task import Task

def test_api_source_returns_tasks():
    source = APISource("https://test.com")
    tasks = source.get_tasks()
    
    assert len(tasks) == 3
    assert tasks[0].id == 101
    assert tasks[0].payload == "api task 1"
    assert tasks[1].id == 102
    assert tasks[2].id == 103

def test_api_source_name():
    source = APISource("https://test.com")
    assert source.name == "api-https://test.com"

def test_api_source_with_logger():
    class MockLogger:
        def info(self, msg):
            self.last_msg = msg
    
    mock = MockLogger()
    source = APISource("https://test.com", logger=mock)
    source.get_tasks()
    
    assert mock.last_msg == "received 3 tasks from API"