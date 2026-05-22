from src.repository.taskRepo import TaskRepository
from src.service.taskService import TaskService
from src.api.aitask import AiTask
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

def show_menu():
    print("\n" + "="*25)
    print("Task management")
    print("1.  Create a task")
    print("2. show tasks")
    print("3. update task")
    print("4. delete task")
    print("5. Quit the program")

def main():
    repo = TaskRepository()
    aiserv = AiTask(api_key=api_key)
    service = TaskService(repo, aitask=aiserv)
    
    while True:
        show_menu()
        choice = input("Make a choice in the menu from 1 to 5").strip()
        if(choice == "1"):
            print("\n create a task: ")
            try:
                 taskid = int(input("Add an id: "))
                 title = input("Add a title: ")
                 description = input("Add a description")
                 priority = input("The priority must be in(low, medium, high)")
                 date_str = input("Enter the due date:")
                 
                 date_str = datetime.strptime(date_str, "%Y-%m-%d")
                 new_task = service.create_task(taskid,title,description,priority,date_str)
                 print(f"the task is created. {new_task}")
            except ValueError as e:
                print(f"Erreur de saisie: {e}")
                
        elif choice == "2":
            print("show the tasks: ")
            the_tasks = service.read_all_tasks()
            if not the_tasks:
                print("empty")
            else:
                for t in the_tasks:
                    print(t)
        elif choice == "3":
            print("Update a task: ")
            print(the_tasks)
            try:
                 taskid = int(input("Enter the id: "))
                 title = input("Enter the new title: ")
                 description = input("enter the new description")
                 priority = input("The priority must be in(low, medium, high)")
                 date_str = input("Enter the due date:")
                 date_str = datetime.strptime(date_str, "%Y-%m-%d")
                 task_update = service.update_tasks(taskid,title,description,priority,date_str)
                 print(f"The task is updated: {task_update}")
            except ValueError as e:
                 print(f"service error: {e}")
                 
        elif choice == "4":
            print("Delete a task: ")
            print(the_tasks)
            try:
                 taskid = int(input("Enter the id: "))
                 title = input("Enter the new title: ")
                 description = input("enter the new description")
                 priority = input("The priority must be in(low, medium, high)")
                 date_str = input("Enter the due date:")
                 date_str = datetime.strptime(date_str, "%Y-%m-%d")
                 delete_task = service.delete_tasks(taskid)
                 print(f"The task is deleted: {delete_task}")
            except ValueError as e:
                print(f"Service error: {e}")
                
        elif choice =="5":
            print("Thank you")
            break
        else:
            print("Invalid option")
if __name__ =="__main__":
    main()
                
           
                
   
        
