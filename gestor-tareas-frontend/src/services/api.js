import axios from "axios";

const API_URL = "http://127.0.0.1:8000/"; // URL del backend FastAPI

export const getTasks = () => axios.get(`${API_URL}/tasks/`);
export const createTask = (task) => axios.post(`${API_URL}/tasks/`, task);