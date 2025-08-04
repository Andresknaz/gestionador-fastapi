from typing import Optional
from uuid import UUID
from datetime import datetime

class Task:
    def __init__(self, id: UUID, project_id: UUID, title: str, description: Optional[str] = None, completed: bool = False, due_date: Optional[datetime] = None):
        self.id = id
        self.project_id = project_id
        self.title = title
        self.description = description
        self.completed = completed
        self.due_date = due_date