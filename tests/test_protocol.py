from src.task_source import TaskSource
from src.file_source import FileSource
from src.generator_source import GeneratorSource

def test_file_follows_protocol():
    assert isinstance(FileSource("test.json"), TaskSource)

def test_generator_follows_protocol():
    assert isinstance(GeneratorSource(1), TaskSource)

class NotSource:
    pass

def test_not_source_does_not_follow():
    assert not isinstance(NotSource(), TaskSource)