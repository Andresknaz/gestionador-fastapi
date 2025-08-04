from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.database import Base

# Modelo de tareas
class TaskModel(Base):
    __tablename__ = "task"

    id = Column(String, primary_key=True, index=True)
    status = Column(Integer, default=0)  # 0 = pendiente, 1 = en progreso, 2 = completada
    name = Column(String, nullable=False)
    description = Column(String)
    proyectId = Column(String, ForeignKey("project.id"))
    userId = Column(Integer, ForeignKey("users.id"))

    # Relaciones
    project = relationship("Project", back_populates="tasks")
    user = relationship("User", back_populates="tasks")