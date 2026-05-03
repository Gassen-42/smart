from src.repository.taskRepo import TaskRepository
from src.service.taskService import TaskService

if __name__== "__main__":
    repo = TaskRepository()
    service = TaskService(repo)
tache = service.create_task(1,"Finaliser le projet", "Refactoring complet", "high","tr")

print(f"Tâche créée : {tache.title} (ID: {tache.id})")
print(f"Liste des tâches : {service.read_all_tasks()}")