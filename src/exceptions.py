class TaskError(Exception):
    """базовое исключение, все остальные будут от него"""
    pass

class IDError(TaskError): #ошибка айди
    pass

class DeskriptionError(TaskError): #ошибка описания
    pass

class StatusError(TaskError): #ошибка статуса
    pass

class PrioraError(TaskError): #ошибка приоритета
    pass

