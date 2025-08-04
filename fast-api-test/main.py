from fastapi import FastAPI
from api import project_controller, task_controller
from infrastructure.database import Base, engine

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Incluir rutas
app.include_router(project_controller.router)
app.include_router(task_controller.router)