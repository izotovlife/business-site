// Назначение: страница редиректа в админку; path: frontend/src/pages/AdminRedirect.jsx; запрашивает ссылку и перенаправляет.
import { useEffect, useState } from "react";
import axios from "axios";

export default function AdminRedirect() {
  const [error, setError] = useState(null);

  useEffect(() => {
    axios
      .get("/api/admin-link", { withCredentials: true })
      .then((res) => {
        window.location.replace(res.data.admin_url);
      })
      .catch(() => {
        setError("Войдите как администратор");
      });
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  return <p>Перенаправление...</p>;
}
