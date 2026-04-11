from src.file_source import FileSource
from src.generator_source import GeneratorSource
from src.api_source import APISource
from src.task_source import TaskSource
from src.logger import log

def main():

    sources = [
        FileSource("data.json"),
        GeneratorSource(3),
        APISource("https://api.example.com/tasks"),
        FileSource("bad.json"),
        GeneratorSource(0),
    ]

    log.info("start")
    for src in sources:
        print(f"\n{src.name}")

        if not isinstance(src, TaskSource):
            log.error(f"not a source: {type(src).__name__}")
            print("not a source")
            continue
        tasks = list(src.get_tasks())
        print(f"{len(tasks)} tasks")
        
        for t in tasks:
            print(f"   {t}")
        log.info(f"ok: {src.name} - {len(tasks)} tasks")
    log.info("end")


if __name__ == "__main__":
    main()
