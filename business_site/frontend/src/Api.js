// frontend/src/Api.js
import axios from "axios";

const api = axios.create({
  baseURL: "/api/v1",
  headers: { "Content-Type": "application/json" },
  // withCredentials: true, // включи, если бэкенд использует сессии/куки
});

export default api;


