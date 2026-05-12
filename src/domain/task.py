from dataclasses import dataclass, field
from src.domain.priority import Priority
from datetime import datetime
@dataclass
class Task:
    id: int
    title: str
    description: str
    priority: Priority
    due_date: datetime
    created_at:datetime = field(default_factory=datetime.now)
    completed: bool = False
    
    
    def __str__(self)->str:
        format_date = self.due_date.strftime("%y-%m-%d")
        return(
            f"Id: {self.id} | {self.title} |" 
            f"Priority: {self.priority} | {format_date}"
        )
        
    @staticmethod   
    def date_remaining(self):
        return Task.due_date - datetime.now()
    
    
    @staticmethod
    def check_priority_per_date(created: datetime, duedate: datetime):
         diff_days:int = (created - duedate).days
         return diff_days
    
    
    

    
    
    
    