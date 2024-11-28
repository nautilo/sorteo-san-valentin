import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api", // Asegúrate de usar la URL correcta
});

// Agrega el token a cada solicitud si está disponible
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default api;
