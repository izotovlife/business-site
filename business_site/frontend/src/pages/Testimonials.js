// C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\frontend\src\pages\Testimonials.js
import { useEffect, useState } from "react";
import api from "../Api";
import "./Testimonials.css";

export default function Testimonials() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;
    (async () => {
      try {
        setLoading(true);
        setError("");
        const res = await api.get("/testimonials/");
        const data = Array.isArray(res.data) ? res.data : res.data.results ?? [];
        if (!ignore) setItems(data);
      } catch (e) {
        console.error(e);
        if (!ignore) setError("Не удалось загрузить отзывы.");
      } finally {
        if (!ignore) setLoading(false);
      }
    })();
    return () => { ignore = true; };
  }, []);

  if (loading) return <div className="container"><p>Загрузка…</p></div>;
  if (error)   return <div className="container"><p className="error">{error}</p></div>;
  if (!items.length) return <div className="container"><p>Отзывы пока отсутствуют.</p></div>;

  return (
    <main className="container">
      <h1>Отзывы</h1>
      <ul className="list">
        {items.map(t => (
          <li key={t.id} className="testimonial">
            {t.avatar_url && <img className="avatar" src={t.avatar_url} alt={t.author} />}
            <div className="content">
              <p className="text">“{t.text}”</p>
              <p className="meta">— {t.author}{t.role ? `, ${t.role}` : ""}</p>
            </div>
          </li>
        ))}
      </ul>
    </main>
  );
}
