from sqlalchemy.orm import Session
from models.project_models import ProjectModel
from uuid import uuid4
from domain.project import Project

class ProjectRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, name: str, description: str) -> Project:
        db_project = ProjectModel(id=str(uuid4()), name=name, description=description)
        self.db.add(db_project)
        self.db.commit()
        self.db.refresh(db_project)
        return Project(id=db_project.id, name=db_project.name, description=db_project.description)

    def get_all(self):
        return self.db.query(ProjectModel).all()