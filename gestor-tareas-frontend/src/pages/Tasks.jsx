import { useEffect, useState } from "react";
import axios from "axios";

function Tasks() {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [newTask, setNewTask] = useState({ name: "", status: "pendiente" });

  // 📌 Cargar tareas desde FastAPI
  useEffect(() => {
    fetchTasks();
  }, []);

  const fetchTasks = () => {
    setLoading(true);
    axios.get("http://localhost:8000/tasks")
      .then((res) => {
        setTasks(res.data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error al obtener tareas:", error);
        setLoading(false);
      });
  };

  // 📌 Manejar envío del formulario para agregar tarea
  const handleAddTask = (e) => {
    e.preventDefault();

    axios.post("http://localhost:8000/tasks", newTask)
      .then(() => {
        setNewTask({ name: "", status: "pendiente" }); // Limpiar formulario
        fetchTasks(); // Recargar tareas
      })
      .catch((error) => console.error("Error al agregar tarea:", error));
  };

  if (loading) {
    return <div className="container mt-5">⏳ Cargando tareas...</div>;
  }

  return (
    <div className="container mt-5">
      <h1>📋 Lista de Tareas</h1>

      {/* 📌 Formulario para agregar tarea */}
      <form className="mt-4 mb-4" onSubmit={handleAddTask}>
        <div className="row g-2">
          <div className="col-md-5">
            <input
              type="text"
              className="form-control"
              placeholder="Nombre de la tarea"
              value={newTask.name}
              onChange={(e) => setNewTask({ ...newTask, name: e.target.value })}
              required
            />
          </div>
          <div className="col-md-4">
            <select
              className="form-select"
              value={newTask.status}
              onChange={(e) => setNewTask({ ...newTask, status: e.target.value })}
            >
              <option value="pendiente">Pendiente</option>
              <option value="en progreso">En Progreso</option>
              <option value="completada">Completada</option>
            </select>
          </div>
          <div className="col-md-3">
            <button type="submit" className="btn btn-primary w-100">
              ➕ Agregar
            </button>
          </div>
        </div>
      </form>

      {/* 📌 Lista de tareas */}
      {tasks.length === 0 ? (
        <p>No hay tareas registradas.</p>
      ) : (
        <ul className="list-group">
          {tasks.map((task) => (
            <li
              key={task.id}
              className={`list-group-item ${
                task.status === "completada" ? "list-group-item-success" : ""
              }`}
            >
              <strong>{task.name}</strong> — {task.status}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default Tasks;