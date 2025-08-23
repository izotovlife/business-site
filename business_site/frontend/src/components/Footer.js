// Footer.js
// Путь: frontend/src/components/Footer.js
// Назначение: Нижний колонтитул сайта с логотипом и копирайтом

import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="container footer-container">
        {/* Логотип в футере */}
        <a href="/" className="footer-logo-link">
          <img src="/logo.png" alt="IZOTOVLIFE Logo" className="footer-logo" />
        </a>

        {/* Копирайт */}
        <p className="footer-text">© 2025 IZOTOVLIFE. Все права защищены.</p>
      </div>
    </footer>
  );
}

export default Footer;
