import React, { useEffect, useState } from "react";
import api from "../Api";

export default function PortfolioPage() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    api
      .get("/portfolio/")
      .then((res) => setItems(res.data))
      .catch(() => setItems([]));
  }, []);

  return (
    <div className="container">
      <h1>Портфолио</h1>
      <div className="grid cols-3">
        {items.map((item) => (
          <div key={item.id} className="card">
            {item.image && <img src={item.image} alt={item.title} />}
            <h3>{item.title}</h3>
            {item.description && <p className="muted">{item.description}</p>}
            {item.link && (
              <a href={item.link} target="_blank" rel="noreferrer">
                Подробнее
              </a>
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
