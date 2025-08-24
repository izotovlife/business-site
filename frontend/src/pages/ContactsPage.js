import React from "react";
import { useOrderModal } from "../OrderModalContext";

export default function ContactsPage() {
  const { openModal } = useOrderModal();
  return (
    <div className="container">
      <h1>Контакты</h1>
      <p>Телефон: <a href="tel:+79267769268">+7 (926) 776-92-68</a></p>
      <p>Email: <a href="mailto:izotovlife@yandex.ru">izotovlife@yandex.ru</a></p>
      <p>Адрес: Москва, м. Орехово</p>
      <div>
        <button className="btn" onClick={() => openModal("page") }>
          Заказать услугу
        </button>
      </div>
    </div>
  );
}
