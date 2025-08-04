from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from infrastructure.database import get_db
from repository.task_repository import TaskRepository
from service.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", )
def create_task(project_id: str, title: str, description: str, db: Session = Depends(get_db)):
    repo = TaskRepository(db)
    service = TaskService(repo)
    return service.create_task(project_id, title, description)