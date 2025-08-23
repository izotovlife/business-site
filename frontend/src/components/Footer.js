import React, { useState } from "react";
import OrderModal from "./OrderModal";
import "./Footer.css";

export default function Footer() {
  const [modal, setModal] = useState(false);

  return (
    <footer className="site-footer">
      <div className="container footer-content">
        <img src="/logo.png" alt="IZOTOVLIFE" className="site-logo" />
        <div className="contacts">
          <a href="tel:+79999999999">+7 (999) 999-99-99</a>
          <a href="mailto:izotovlife@yandex.ru">izotovlife@yandex.ru</a>
          <div className="social">
            <a href="https://vk.com" target="_blank" rel="noreferrer">VK</a>
            <a href="https://ok.ru" target="_blank" rel="noreferrer">OK</a>
            <a href="https://t.me" target="_blank" rel="noreferrer">TG</a>
          </div>
          <button className="btn" onClick={() => setModal(true)}>
            Заказать услугу
          </button>
        </div>
      </div>
      <OrderModal open={modal} onClose={() => setModal(false)} preset="footer" />
    </footer>
  );
}
