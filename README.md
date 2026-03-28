# лабораторная работа 2

## структура


    ├── src/         
    │   ├── descriptors.py           #дескрипторы для проверки     
    │   ├── exceptions.py            #исключения
    │   ├── logger.py                #логирование
    │   ├── task.py                  #класс Task
    │   ├── main.py                  #запуск   
    ├── test/  
    │   ├── ├── test_exceptions.py
    │   ├── ├── test_integration.py
    │   ├── ├── test_task.py

##  пользовательские дескрипторы для валидации
- IdDescriptor - проверяет что id целое число и > 0
- DescriptionDescriptor - проверяет что описание строка и не пустое
- PriorityDescriptor -  проверяет что приоритет число от 1 до 5
- StatusDescriptor - проверяет что статус из списка
в файле descriptors.py

все дескрипторы имеют get и set 

## класс Task
использует дескрипторы
использование property для вычисляемых свойств
readiness_to_perform в task.py
логирование всех действий

## предотвращение некорректных состояний объекта
проверки в дескрипторах

## исключения
- TaskError - базовое исключение
- IDError - ошибка id
- DeskriptionError - ошибка описания
- PrioraError - ошибка приоритета
- StatusError - ошибка статуса
в exceptions.py

## логирование 
все действия пишутся в polisha.log
формат: время + сообщение

## аннотации типов
task_id: int, description: str, -> bool
