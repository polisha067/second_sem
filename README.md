# лабораторная работа 4
асинхронный исполнитель задач, обрабатывающий задачи из очереди с использованием расширяемых обработчиков
## структура

    ├── src/         
    │   ├── main.py               #запуск 
    │   ├── api_source.py         
    │   ├── async_executor.py     #асинхронный исполнитель 
    │   ├── async_task_queue.py   #асинхронная очередь
    │   ├── async_task_runner.py  #event loop в фоновом потоке
    │   ├── dependencies.py       #заглуш
    │   ├── task.py               #модель задачи
    │   ├── descriptors.py       
    │   ├── exceptions.py         #исключения
    │   ├── executor_resource.py  #контекстный менеджер
    │   ├── file_source.py
    │   ├── generator_source.py
    │   ├── handlers.py           #обработчик
    │   ├── logger.py 
    │   ├── task_handler.py       #протокол обработчика
    │   ├── task_source.py
    │   ├── task_queue.py  #очередь задач      
    ├── test/  
    │   ├── ├── test_task_queue.py   #тесты для очереди
    │   ├── ├── test_integration.py  #интеграционные тесты
    │   ├── data.json

## реализация требований
### асинхронная очередь задач
реализована в `async_task_queue.py`
- `async put(task: Task) -> None` - добавление задачи в очередь
- `async get() -> Task` - извлечение задачи из очереди
- `task_done() -> None` - сигнал завершения обработки задачи
- `async join() -> None` - ожидание завершения всех задач
- `qsize() -> int` - текущий размер очереди
- `empty() -> bool` - проверка на пустоту

### описание контракта обработчика через Protocol
в `task_handler.py` объявлен структурный протокол с декоратором `@runtime_checkable`
- любой объект с атрибутом name: str и асинхронным методом handle(task: Task) -> None удовлетворяет контракту
- проверка isinstance(handler, TaskHandler) выполняется во время выполнения в AsyncExecutor.process()

### централизованное логирование и обработка ошибок
- единый логгер polisha используется во всех модулях
- все события пишутся в polisha.log на уровне DEBUG
- вспомогательная функция log_error() для единообразной записи ошибок
- валидация полей через дескрипторы в descriptors.py
- в exceptions.py:
TaskError - баз
IDError - ошибка id
DeskriptionError - ошибка описания
StatusError - ошибка статуса
PrioraError - ошибка приоритета
ExecutorError - ошибка исполнителя

### отсутствие блокирующих операций в event loop
- asyncio.sleep() используется вместо time.sleep()
- asyncio.wait_for() с таймаутом 0.2 предотвращает вечное ожидание и позволяет циклу обрабатывать флаг _stop
- разделение потоков: синхронная TaskQueue и интерактивное меню работают в основном потоке, асинхронная обработка в фоновом потоке через AsyncTaskRunner

### архитектура, допускающая добавление новых типов задач и обработчиков
существующие источники подключаются через меню без изменения main.py FileSource - загрузка из JSON-файла,GeneratorSource - генерация задач, APISource - заглушка API

новые обработчики
создать класс, удовлетворяющий протоколу TaskHandler

### механизмы
- протокол (Protocol) в task_handler.py - TaskHandler
- event loop в фоновом потоке в async_task_runner.py - AsyncTaskRunner
- асинхронный контекстный менеджер в executor_resource.py - ExecutorResource
- дескрипторы валидации	в descriptors.py - IDDescriptor, StatusDescriptor и др.
- duck typing источников в task_source.py - базовый класс, проверка isinstance в main.py
- заглушки зависимостей	в dependencies.py - DatabaseStub, NotifierStub
- централизованный логгер в logger.py
