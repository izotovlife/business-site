// frontend/src/pages/AdminRedirect.jsx
// Назначение: страница перенаправления в админку. Путь: frontend/src/pages/AdminRedirect.jsx.
// Изменения: запрос на /api/admin-link и редирект на полученный URL;
// при 401/403 показывается подсказка "Войдите как администратор".
import { useEffect, useState } from "react";
import axios from "axios";

export default function AdminRedirect() {
  const [error, setError] = useState(false);

  useEffect(() => {
    async function fetchLink() {
      try {
        const resp = await axios.get("/api/admin-link", { withCredentials: true });
        window.location.replace(resp.data.admin_url);
      } catch (e) {
        setError(true);
      }
    }
    fetchLink();
  }, []);

  if (error) {
    return <p>Войдите как администратор</p>;
  }
  return <p>Перенаправляем в админку...</p>;
}
