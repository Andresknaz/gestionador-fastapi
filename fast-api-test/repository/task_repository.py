from sqlalchemy.orm import Session
from models.task_models import TaskModel
from uuid import uuid4
from domain.task import Task

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, project_id: str, title: str, description: str):
        db_task = TaskModel(id=str(uuid4()), project_id=project_id, title=title, description=description)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return Task(id=db_task.id, project_id=db_task.project_id, title=db_task.title, description=db_task.description)