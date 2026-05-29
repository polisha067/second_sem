from src.api_source import APISource
from src.async_executor import AsyncExecutor
from src.async_task_queue import AsyncTaskQueue
from src.async_task_runner import AsyncTaskRunner
from src.file_source import FileSource
from src.generator_source import GeneratorSource
from src.handlers import SleepHandler
from src.task import Task
from src.task_queue import TaskQueue
from src.task_source import TaskSource

runner = None
executor = None
async_queue = None

def ensure_async():
    global runner, executor, async_queue

    if runner is None:
        async_queue = AsyncTaskQueue()
        executor = AsyncExecutor(async_queue, SleepHandler())
        runner = AsyncTaskRunner()
        runner.start()
        runner.submit(executor.worker())
        print("async-runner запущен")

    return runner, executor, async_queue


async def enqueue_task(q, task):
    await q.put(task)


async def enqueue_many(q, tasks):
    for t in tasks:
        await q.put(t)
    await q.join()


def main():
    queue = TaskQueue()

    while True:

        print("1) добавить задачи из источника (duck typing через TaskSource)")
        print("2) добавить одну задачу вручную")
        print("3) показать все задачи")
        print("4) фильтр по статусу")
        print("5) фильтр по приоритету")
        print("6) изменить статус задачи по id")
        print("7) удалить задачу по id")
        print("8) запустить обработку одной pending задачи")
        print("9) запустить обработку всех pending")
        print("10) остановить исполнитель")
        print("0) выход")
        print(f"в очереди: {len(queue)} задач")

        choice = input("~ ").strip()

        if choice == "0":
            break

        if choice == "1":
            print("\nисточники:")
            print("1) файл (например: data.json)")
            print("2) генератор (count)")
            print("3) api (учебный мок)")
            src_choice = input("> ").strip()

            if src_choice == "1":
                path = input("путь к json (enter = data.json): ").strip() or "data.json"
                src = FileSource(path)

            elif src_choice == "2":
                raw = input("сколько задач сгенерировать? ").strip()

                if not raw.isdigit():
                    print("нужно целое число")
                    continue
                count = int(raw)
                src = GeneratorSource(count)

            elif src_choice == "3":
                url = input("url (enter = https://api.example.com/tasks): ").strip() or "https://api.example.com/tasks"
                src = APISource(url)

            else:
                print("неизвестный источник")
                continue

            if not isinstance(src, TaskSource):
                print(f"not a source: {type(src).__name__}")
                continue

            added = 0
            for t in src.get_tasks():
                queue.add(t)
                added += 1

            print(f"добавлено задач: {added} (источник: {src.name})")
            continue


        if choice == "2":
            raw_id = input("id: ").strip()

            if not raw_id.isdigit():
                print("нужно целое число")
                continue
            task_id = int(raw_id)
            desc = input("описание: ").strip()

            if not desc:
                print("описание не должно быть пустым")
                continue

            raw_pr = input("приоритет (enter = 3): ").strip()

            if raw_pr == "":
                priority = 3

            elif raw_pr.isdigit():
                priority = int(raw_pr)

            else:
                print("нужно целое число")
                continue

            queue.add(Task(task_id=task_id, description=desc, priority=priority))
            print("ok")
            continue


        if choice == "3":
            print("\nвсе задачи:")
            for t in queue:
                print(t)
            continue


        if choice == "4":
            status = input("status (pending/running/completed...): ").strip()

            if not status:
                print("status не должен быть пустым")
                continue
            print(f"\nзадачи со статусом {status}:")

            for t in queue.filter(status=status):
                print(t)
            continue


        if choice == "5":
            raw_pr = input("priority: ").strip()

            if not raw_pr.isdigit():
                print("нужно целое число")
                continue
            priority = int(raw_pr)
            print(f"\nзадачи с приоритетом {priority}:")

            for t in queue.by_priority(priority):
                print(t)
            continue


        if choice == "6":
            raw_id = input("id: ").strip()

            if not raw_id.isdigit():
                print("нужно целое число")
                continue
            task_id = int(raw_id)
            task = queue.get_by_id(task_id)

            if not task:
                print("задача не найдена")
                continue
            new_status = input("новый статус: ").strip()

            if not new_status:
                print("status не должен быть пустым")
                continue
            task.status = new_status
            print("ok")
            continue


        if choice == "7":
            raw_id = input("id: ").strip()

            if not raw_id.isdigit():
                print("нужно целое число")
                continue
            task_id = int(raw_id)
            ok = queue.remove(task_id)
            print("ok" if ok else "не найдено")
            continue


        if choice == "8":
            pending = list(queue.pending_tasks())

            if not pending:
                print("нет pending задач")
                continue

            task = pending[0]
            r, ex, aq = ensure_async()
            r.submit(enqueue_task(aq, task))
            print(f"задача {task.id} в async-очереди")
            continue


        if choice == "9":
            pending = list(queue.pending_tasks())

            if not pending:
                print("нет pending задач")
                continue

            r, ex, aq = ensure_async()
            fut = r.submit(enqueue_many(aq, pending))

            def done_cb(f):
                try:
                    f.result()
                    print("все pending обработаны")
                except Exception as e:
                    print("ошибка:", e)

            fut.add_done_callback(done_cb)
            print(f"отправлено: {len(pending)}")
            continue


        if choice == "10":
            global runner, executor, async_queue

            if runner is None:
                print("runner не запущен")
                continue

            if executor is not None:
                executor.stop()
            runner.stop()
            runner = None
            executor = None
            async_queue = None
            print("async-runner остановлен")
            continue

        print("неизвестная команда")


if __name__ == "__main__":
    main()
