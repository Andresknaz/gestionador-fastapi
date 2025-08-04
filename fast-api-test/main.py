from fastapi import FastAPI
from api import project_controller, task_controller
from infrastructure.database import Base, engine
from fastapi.middleware.cors import CORSMiddleware


# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

# Configuración de CORS
origins = [
    "http://localhost:5173",  # Frontend en desarrollo con Vite
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,       # Permite solo estos orígenes
    allow_credentials=True,
    allow_methods=["*"],         # Permite todos los métodos
    allow_headers=["*"],         # Permite todas las cabeceras
)

# Incluir rutas
app.include_router(project_controller.router)
app.include_router(task_controller.router)


# Ruta de prueba
@app.get("/")
def read_root():
    return {"message": "API funcionando correctamente 🚀"}