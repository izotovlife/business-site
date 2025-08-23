import React, { useEffect, useState } from "react";
import OrderModal from "../components/OrderModal";
import api from "../Api";

export default function ServiceListPage() {
  const [services, setServices] = useState([]);
  const [active, setActive] = useState(null);

  useEffect(() => {
    api.get("/services/").then((res) => setServices(res.data));
  }, []);

  return (
    <div className="container">
      <h1>Услуги</h1>
      <div className="services-grid">
        {services.map((s) => (
          <div key={s.id} className="service-card">
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
