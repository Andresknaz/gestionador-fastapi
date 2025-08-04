from typing import Optional
from uuid import UUID

class Project:
    def __init__(self, id: UUID, name: str, description: Optional[str] = None):
        self.id = id
        self.name = name
        self.description = description