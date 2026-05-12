from src.repository.taskRepo import TaskRepository
from src.domain.task import Task
from src.domain.priority import Priority
from src.api.aitask import AiTask
from datetime import datetime

class TaskService:
    def __init__(self, taskrepo: TaskRepository, aitask: AiTask):
        self.taskrepo = taskrepo
        self.aitask = aitask

    def create_task(self, id: int, title: str, description: str, priority: str, due_date: datetime) -> Task:
        subtasks = []
        if not title.strip():
            raise ValueError("Title cannot be empty")

        if not description.strip():
            raise ValueError("description cannot be empty!")
        try:
            priori = Priority(priority.lower())
        except ValueError:
            priority_value = [p.value for p in priori]
            raise ValueError(f"invalid priority. choose in: {priority_value}")
        task = Task(id = 0, title=title, description=description, priority=priori, due_date=due_date)
        self.taskrepo.create_task(task)
        
        if self.aitask:
            try:
                subtasks = self.aitask.generate_sub_tasks(title=title, description=description)
                task.subtasks = subtasks
            except Exception as e:
                print(f"Erreur Ia: {e}")
        return task

    def read_all_tasks(self)->list[Task]:
        the_tasks = self.taskrepo.read_all_tasks()
        for t in the_tasks:
            print(t)
        
    
    def delete_task(tasks: list[Task], taskid: int) -> Task:
        for i, task in enumerate(tasks):
            if task.id == taskid:
                return tasks.pop(i)
            raise ValueError("Task not found")
