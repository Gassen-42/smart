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
    
    
    
    