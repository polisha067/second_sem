import pytest
from src.file_source import FileSource


def test_file_not_found():

    source = FileSource("no.json")
    assert len(list(source.get_tasks())) == 0

def test_file_reads_tasks(tmp_path):

    file = tmp_path / "dt.json"
    file.write_text('[{"id": 1, "payload": "task1"}]')
    
    source = FileSource(str(file))
    tasks = list(source.get_tasks())
    
    assert len(tasks) == 1
    assert tasks[0].payload == "task1"