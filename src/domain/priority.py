from dataclasses import dataclass
from enum import Enum
@dataclass
class Priority(Enum):
    LOW = "low"
    Medium = "medium"
    High =   "high"