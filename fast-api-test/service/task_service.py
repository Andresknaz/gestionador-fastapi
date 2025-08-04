from repository.task_repository import TaskRepository

class TaskService:
    def __init__(self, repo: TaskRepository):
        self.repo = repo

    def create_task(self, project_id: str, title: str, description: str):
        return self.repo.create(project_id, title, description)