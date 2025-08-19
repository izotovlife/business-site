import { useEffect, useState } from "react";
import api from "../Api";
import "./Portfolio.css";

export default function Portfolio() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let ignore = false;
    (async () => {
      try {
        setLoading(true);
        setError("");
        const res = await api.get("/portfolio/");
        const data = Array.isArray(res.data) ? res.data : res.data.results ?? [];
        if (!ignore) setItems(data);
      } catch (e) {
        console.error(e);
        if (!ignore) setError("Не удалось загрузить портфолио.");
      } finally {
        if (!ignore) setLoading(false);
      }
    })();
    return () => { ignore = true; };
  }, []);

  if (loading) return <div className="container"><p>Загрузка…</p></div>;
  if (error)   return <div className="container"><p className="error">{error}</p></div>;
  if (!items.length) return <div className="container"><p>Портфолио пока пусто.</p></div>;

  return (
    <main className="container">
      <h1>Портфолио</h1>
      <div className="grid">
        {items.map(it => (
          <article key={it.id} className="card">
            {it.image_url && <img src={it.image_url} alt={it.title} />}
            <h3>{it.title}</h3>
            {it.description && <p>{it.description}</p>}
            {it.link && (
              <p><a href={it.link} target="_blank" rel="noreferrer">Перейти к работе →</a></p>
            )}
          </article>
        ))}
      </div>
    </main>
  );
}
