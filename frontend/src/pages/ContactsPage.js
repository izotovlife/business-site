import React, { useState } from "react";
import OrderModal from "../components/OrderModal";

export default function ContactsPage() {
  const [open, setOpen] = useState(false);
  return (
    <div className="container">
      <h1>Контакты</h1>
      <p>Телефон: <a href="tel:+79267769268">+7 (926) 776-92-68</a></p>
      <p>Email: <a href="mailto:izotovlife@yandex.ru">izotovlife@yandex.ru</a></p>
      <p>Адрес: Москва, м. Орехово</p>
      <div>
        <button className="btn" onClick={() => setOpen(true)}>
          Заказать услугу
        </button>
      </div>
      <OrderModal open={open} onClose={() => setOpen(false)} preset="page" />
    </div>
  );
}
