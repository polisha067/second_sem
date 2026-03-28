import pytest
from src.task import Task
from src.exceptions import IDError, DeskriptionError, PrioraError, StatusError


def test_task_creation():
    t = Task(1, "сделать лабу", 3)
    assert t.id == 1
    assert t.deskriptor == "сделать лабу"
    assert t.priority == 3
    assert t.status == "pending"

def test_default_priority():
    t = Task(1, "текст")
    assert t.priority == 3

def test_negative_id():
    with pytest.raises(IDError):
        Task(-1, "текст", 3)

def test_zero_id():
    with pytest.raises(IDError):
        Task(0, "текст", 3)

def test_empty_description():
    with pytest.raises(DeskriptionError):
        Task(1, "", 3)

def test_priority_below_min():
    with pytest.raises(PrioraError):
        Task(1, "текст", 0)

def test_priority_above_max():
    with pytest.raises(PrioraError):
        Task(1, "текст", 6)

def test_status_change():
    t = Task(1, "текст", 3)
    t.status = "running"
    assert t.status == "running"

def test_invalid_status():
    t = Task(1, "текст", 3)
    with pytest.raises(StatusError):
        t.status = "invalid"

def test_readiness():
    t = Task(1, "текст", 3)
    assert t.readiness_to_perform == True
    t.status = "running"
    assert t.readiness_to_perform == False

def test_very_long_description():
    long_text = "а" * 1000
    t = Task(1, long_text, 3)
    assert t.deskriptor == long_text

def test_priority_invalid_type():
    with pytest.raises(PrioraError):
        Task(1, "текст", "3")

def test_priority_changes():
    t = Task(1, "текст", 3)
    t.priority = 5
    assert t.priority == 5