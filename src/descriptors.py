from src.logger import log
from src.exceptions import IDError, DeskriptionError, PrioraError, StatusError


class IDDescriptor:

    def __set_name__(self, owner, name):
        self.store = '_' + name
    

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.store, None)
    

    def __set__(self, obj, value):
        log.debug(f"проверка id: {value}")

        if not isinstance(value, int):
            log.error(f"id должен быть int, получен {type(value).__name__}")

            raise IDError(f"id должен быть int, получен {type(value).__name__}")
        
        if value <= 0:
            log.error(f"id должен быть > 0, получен {value}")

            raise IDError(f"id должен быть > 0, получен {value}")
        setattr(obj, self.store, value)



class DescriptionDescriptor:


    def __set_name__(self, owner, name):

        self.store = '_' + name
    

    def __get__(self, obj, objtype=None):

        if obj is None:
            return self
        return getattr(obj, self.store, None)
    

    def __set__(self, obj, value):
        log.debug(f"проверка description: {value}")

        if not isinstance(value, str):
            log.error(f"description должен быть строкой, получен {type(value).__name__}")

            raise DeskriptionError(f"description должен быть строкой, получен {type(value).__name__}")
        
        if not value.strip():
            log.error("description не может быть пустым")

            raise DeskriptionError("description не может быть пустым")
        setattr(obj, self.store, value)



class PriorityDescriptor:


    def __set_name__(self, owner, name):
        self.store = '_' + name
    

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.store, None)
    

    def __set__(self, obj, value):
        log.debug(f"проверка priority: {value}")

        if not isinstance(value, int):
            log.error(f"priority должен быть int, получен {type(value).__name__}")

            raise PrioraError(f"priority должен быть int, получен {type(value).__name__}")
        
        if value < 1 or value > 5:
            log.error(f"priority должен быть от 1 до 5, получен {value}")

            raise PrioraError(f"priority должен быть от 1 до 5, получен {value}")
        setattr(obj, self.store, value)



class StatusDescriptor:
    ALLOWED = ["pending", "running", "completed", "failed"]
    

    def __set_name__(self, owner, name):
        self.store = '_' + name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.store, None)
    
    def __set__(self, obj, value):
        log.debug(f"проверка status: {value}")

        if value not in self.ALLOWED:
            log.error(f"status должен быть одним из {self.ALLOWED}, получен {value}")

            raise StatusError(f"status должен быть одним из {self.ALLOWED}, получен {value}")
        setattr(obj, self.store, value)