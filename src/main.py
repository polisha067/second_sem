from src.task import Task
from src.task_queue import TaskQueue

def main():

    queue = TaskQueue()

    queue.add(Task(1, "сделать лабу", 5))
    queue.add(Task(2, "проверить код", 2))
    queue.add(Task(3, "написать тесты", 1))

    print(f"всего задач: {len(queue)}")
    print("\nвсе задачи")

    for task in queue:
        print(task)

    print("\nприоритет 5:")

    for task in queue.by_priority(5):
        print(task)


    task = queue.get_by_id(1)

    if task:
        task.status = "running"

    print("\nзадачи со статусом pending")

    for task in queue.pending_tasks():
        print(task)

    queue.remove(2)

    print(f"\nпосле удаления: {len(queue)} задач")


if __name__ == "__main__":
    main()