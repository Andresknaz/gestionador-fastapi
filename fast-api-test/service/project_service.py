from repository.project_repository import ProjectRepository

class ProjectService:
    def __init__(self, repo: ProjectRepository):
        self.repo = repo

    def create_project(self, name: str, description: str):
        return self.repo.create(name, description)

    def list_projects(self):
        return self.repo.get_all()