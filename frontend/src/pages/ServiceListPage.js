import React, { useEffect, useState } from "react";
import OrderModal from "../components/OrderModal";
import api from "../Api";

export default function ServiceListPage() {
  const [services, setServices] = useState([]);
  const [active, setActive] = useState(null);

  const defaults = [
    { id: 1, title: "Администрирование сайтов" },
    { id: 2, title: "Контент‑менеджмент" },
    { id: 3, title: "SMM и ведение соцсетей" },
    { id: 4, title: "Обработка фото и видео" },
    { id: 5, title: "Работа с маркетплейсами" },
    { id: 6, title: "Управление отзывами" },
    { id: 7, title: "SEO и реклама" },
    { id: 8, title: "Консультации по принтерам" },
  ];

  useEffect(() => {
    api
      .get("/services/")
      .then((res) => {
        if (res.data && res.data.length) setServices(res.data);
        else setServices(defaults);
      })
      .catch(() => setServices(defaults));
  }, []);

  return (
    <div className="container">
      <h1>Услуги</h1>
      <div className="grid cols-2">
        {services.map((s) => (
          <div key={s.id} className="card service-card">
            <h3>{s.title}</h3>
            {s.short && <p>{s.short}</p>}
            {s.price_from && <p>от {s.price_from} ₽</p>}
            <button className="btn" onClick={() => setActive(s.id)}>
              Заказать услугу
            </button>
          </div>
        ))}
      </div>
      <OrderModal
        open={active !== null}
        onClose={() => setActive(null)}
        preset="page"
        serviceId={active}
      />
    </div>
  );
}
