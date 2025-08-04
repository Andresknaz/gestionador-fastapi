from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from infrastructure.database import Base

# Modelo de proyectos
class ProjectModel(Base):
    __tablename__ = "project"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)

    # Relación con tareas
    tasks = relationship("Task", back_populates="project")



