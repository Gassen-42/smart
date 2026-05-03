from src.repository.taskRepo import TaskRepository
from src.domain.task import Task
from src.domain.priority import Priority

class TaskService:
    def __init__(self, taskrepo: TaskRepository):
        self.taskrepo = taskrepo

    def create_task(self, id: int, title: str, description: str, priority: str, due_date: str) -> Task:
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
        return task

    def read_all_tasks(self)->list[Task]:
        return self.taskrepo.read_all_tasks()

    def delete_task(tasks: list[Task], taskid: int) -> Task:
        for i, task in enumerate(tasks):
            if task.id == taskid:
                return tasks.pop(i)
            raise ValueError("Task not found")
