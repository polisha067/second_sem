import pytest
from src.generator_source import GeneratorSource

def test_generator_creates_tasks():

    source = GeneratorSource(4)  
    tasks = list(source.get_tasks())
    
    assert len(tasks) == 4
    assert tasks[0].id == 1


def test_generator_zero():

    source = GeneratorSource(0)
    tasks = list(source.get_tasks())
    assert len(tasks) == 0


def test_generator_negative():

    source = GeneratorSource(-1)
    tasks = list(source.get_tasks())
    assert len(tasks) == 0
