from src.task import Task

def main():

    task_id = int(input("id: "))
    desc = input("описание: ")
    priority = int(input("приоритет (1-5): "))

    t = Task(task_id, desc, priority)
    print(t)

    answer = input("менять статус? (y/n): ")
    if answer.lower() == "y":
        new_status = input("новый статус (pending/running/completed/failed): ")
        t.status = new_status
        print(f"статус изменен: {t.status}")
        print(t)
    else:
        print("статус не изменен")


if __name__ == "__main__":
    main()
