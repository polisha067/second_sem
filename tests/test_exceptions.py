import pytest
from src.exceptions import TaskError, IDError, DeskriptionError, PrioraError, StatusError

def test_exceptions_inheritance():
    assert issubclass(IDError, TaskError)
    assert issubclass(DeskriptionError, TaskError)
    assert issubclass(PrioraError, TaskError)
    assert issubclass(StatusError, TaskError)