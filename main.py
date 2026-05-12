from src.repository.taskRepo import TaskRepository
from src.service.taskService import TaskService
from src.api.aitask import AiTask
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if __name__ == "__main__":
    repo = TaskRepository()
    aiserv = AiTask(api_key=api_key)
    service = TaskService(repo, aitask=aiserv)
date_obj = datetime.strptime("2026-05-09", "%Y-%m-%d")
tache = service.create_task(
    1, "Finaliser le projet", "Refactoring complet", "high", date_obj
)
print("\n" + " "*10)
print("Gestion des taches: ")

print(f"Tâche créée : {tache.title} (ID: {tache.id})")
print(f"Liste des tâches : {service.read_all_tasks()}")
