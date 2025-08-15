import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './Services.css';

export default function Services() {
  const [sections, setSections] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:8000/api/sections/')
      .then(res => setSections(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="services-section container">
      <h2>Наши услуги</h2>
      <div className="services-grid">
        {sections.map(s => (
          <div className="service-card" key={s.id}>
            <h3>{s.title}</h3>
            <p>{s.content}</p>
            <button className="order-button">Заказать</button>
          </div>
        ))}
      </div>
    </div>
  );
}
