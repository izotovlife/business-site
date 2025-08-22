// Footer.js
// frontend/src/components/Footer.js
// Футер сайта с логотипом из public/logo.svg
import React from "react";
import "./Footer.css";

export default function Footer(){
  return (
    <footer className="site-footer">
      <div className="container footer-grid">
        <div className="footer-brand">
          <img
            className="footer-brand-img"
            src="/logo.svg"
            alt="IZOTOVLIFE"
            height="32"
            width="auto"
            decoding="async"
          />
          <span className="footer-brand-title">IZOTOVLIFE</span>
          <p className="muted">
            Разработка сайтов и автоматизация для вашего бизнеса.
          </p>
        </div>

        <div>
          <h4>Контакты</h4>
          <ul className="list">
            <li><a href="mailto:izotovlife@yandex.ru">izotovlife@yandex.ru</a></li>
            <li><a href="https://t.me/izotovlife" target="_blank" rel="noreferrer">Telegram</a></li>
          </ul>
        </div>

        <div>
          <h4>Навигация</h4>
          <ul className="list">
            <li><a href="/services">Услуги</a></li>
            <li><a href="/portfolio">Портфолио</a></li>
            <li><a href="/testimonials">Отзывы</a></li>
          </ul>
        </div>
      </div>

      <div className="footbar">
        <div className="container">
          © {new Date().getFullYear()} Изотов. Все права защищены.
        </div>
      </div>
    </footer>
  );
}
