from dataclasses import dataclass
from src.domain.task import Task
from datetime import datetime


@dataclass
class TaskRepository:
    def __init__(self):
        self._tasks: list[Task] = []

    def create_task(self, task: Task)->list[Task]:
        return self._tasks.append(task)
     

    def read_all_tasks(self) -> list[Task]:
        return self._tasks
    
    def get_by_id(self, task_id: int) -> Task | None:
        return next((t for t in self._tasks if t.id == task_id), None)

    def remove(self, task_id: int) -> bool:
        task = self.get_by_id(task_id)
        if task:
            self._tasks.remove(task)
            return True
        return False
    
    
   
     
    def is_over_due(self)->bool:
        if Task.completed:
            return False
        return datetime.now() > Task.due_date
        
   

   


 
