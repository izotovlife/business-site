// src/Api.js
import axios from "axios";

// CRA dev-server с "proxy" в package.json отправит запросы на бэкенд.
// В проде можно заменить baseURL на ваш домен, например '/api/v1'.
const api = axios.create({
  baseURL: "/api/v1",
});

export default api;


