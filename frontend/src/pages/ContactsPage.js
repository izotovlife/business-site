import React, { useState } from "react";
import OrderModal from "../components/OrderModal";

export default function ContactsPage() {
  const [open, setOpen] = useState(false);
  return (
    <div className="container">
      <h1>Контакты</h1>
      <p>Телефон: <a href="tel:+79999999999">+7 (999) 999-99-99</a></p>
      <p>Email: <a href="mailto:izotovlife@yandex.ru">izotovlife@yandex.ru</a></p>
      <div>
        <button className="btn" onClick={() => setOpen(true)}>
          Заказать услугу
        </button>
      </div>
      <OrderModal open={open} onClose={() => setOpen(false)} preset="page" />
    </div>
  );
}
