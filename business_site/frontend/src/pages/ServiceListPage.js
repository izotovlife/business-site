import React from "react";
import { useOrderModal } from "../OrderModalContext";

export default function ServiceListPage() {
  const { open } = useOrderModal();
  return (
    <section className="container" style={{padding: "24px 0"}}>
      <h2>Услуги</h2>
      <ul>
        <li>Разработка лендингов</li>
        <li>Интеграция с CRM</li>
        <li>Поддержка и доработка</li>
      </ul>
      <button className="btn" onClick={open}>Заказать услугу</button>
    </section>
  );
}
