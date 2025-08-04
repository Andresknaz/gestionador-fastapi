from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from repository.project_repository import ProjectRepository
from service.project_service import ProjectService

router = APIRouter(prefix="/projects", tags=["projects"])

@router.post("/")
def create_project(name: str, description: str, db: Session = Depends(get_db)):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.create_project(name, description)

@router.get("/")
def list_projects(db: Session = Depends(get_db)):
    repo = ProjectRepository(db)
    service = ProjectService(repo)
    return service.list_projects()