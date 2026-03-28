import pytest
from src.task import Task

def test_full_lifecycle():
    t = Task(1, "сделать лабу", 3)
    
    assert t.status == "pending"
    assert t.readiness_to_perform == True
    
    t.status = "running"
    assert t.readiness_to_perform == False
    
    t.status = "completed"
    assert t.status == "completed"

def test_multiple_tasks():
    t1 = Task(1, "задача 1", 3)
    t2 = Task(2, "задача 2", 5)
    
    t1.status = "running"
    t2.status = "completed"
    
    assert t1.status == "running"
    assert t2.status == "completed"