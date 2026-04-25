from datetime import datetime
from src.logger import log
from src.descriptors import IDDescriptor,DescriptionDescriptor,PriorityDescriptor,StatusDescriptor


class Task:
    """моделька таска"""

    id = IDDescriptor()
    deskriptor = DescriptionDescriptor()
    priority = PriorityDescriptor()
    status = StatusDescriptor()


    def __init__(self, task_id: int, description: str, priority: int = 3, logger= None):
            
            self.logger = logger or log
            self.logger.debug(f"создан таск: id = {task_id}")

            self.id = task_id
            self.deskriptor = description
            self.priority = priority
            self.status = "pending"
            self.created_at = datetime.now()
        
            self.logger.info(f"таск {self.id} создан, приоритет={priority}")

     
    @property
    def readiness_to_perform(self) -> bool:

        return self.status == "pending"
    

    def __repr__(self):

        return f"таск(id={self.id}, status={self.status}, priority={self.priority})"
    