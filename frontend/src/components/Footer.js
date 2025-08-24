import React from "react";
import { NavLink } from "react-router-dom";
import { useOrderModal } from "../OrderModalContext";
import "./Footer.css";

export default function Footer() {
  const { openModal } = useOrderModal();
  const year = new Date().getFullYear();

  return (
    <footer className="site-footer">
      <div className="container footer-grid">
        <div className="footer-brand">
          <img src="/logo.svg" alt="IZOTOVLIFE" className="footer-brand-img" />
          <span className="footer-brand-title">IZOTOVLIFE</span>
        </div>

        <ul className="list">
          <li><NavLink to="/services">Услуги</NavLink></li>
          <li><NavLink to="/portfolio">Портфолио</NavLink></li>
          <li><NavLink to="/contacts">Контакты</NavLink></li>
        </ul>

        <div className="list">
          <p>Москва, м. Орехово</p>
          <a href="tel:+79267769268">+7 (926) 776-92-68</a>
          <a href="mailto:izotovlife@yandex.ru">izotovlife@yandex.ru</a>
          <div className="social">
            <a href="https://m.vk.com/itactprint" target="_blank" rel="noreferrer">VK</a>
            <a href="https://ok.ru/itactprint" target="_blank" rel="noreferrer">OK</a>
            <a href="https://t.me/copyzongroup" target="_blank" rel="noreferrer">TG</a>
          </div>
          <button className="btn" onClick={() => openModal("footer")}>Заказать услугу</button>
        </div>
      </div>
      <div className="container footbar">© {year} IZOTOVLIFE</div>
    </footer>
  );
}
