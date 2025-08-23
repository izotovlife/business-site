// Путь: frontend/src/components/Header.js
// Назначение: Шапка сайта-услуг с логотипом, навигацией и одной CTA-кнопкой

import React from "react";
import { Link } from "react-router-dom";
import "./Header.css";

function Header() {
  return (
    <header className="header">
      <div className="container header__row">
        {/* ЛОГО */}
        <Link to="/" className="logoLink" aria-label="На главную">
          <img src="/logo.png" alt="IZOTOVLIFE" className="logoImg" />
        </Link>

        {/* НАВИГАЦИЯ */}
        <nav className="nav" aria-label="Основная навигация">
          <Link to="/about" className="nav__link">О нас</Link>
          <Link to="/services" className="nav__link">Услуги</Link>
          <Link to="/portfolio" className="nav__link">Портфолио</Link>
          <Link to="/contact" className="nav__link">Контакты</Link>
        </nav>

        {/* ЕДИНСТВЕННАЯ CTA-КНОПКА */}
        <div className="cta">
          <Link to="/contact" className="btn btn--primary">Заказать услугу</Link>
        </div>

        {/* Мобильный бургер */}
        <input id="navToggle" type="checkbox" className="navToggle" />
        <label htmlFor="navToggle" className="burger" aria-label="Меню">
          <span />
          <span />
          <span />
        </label>

        {/* Мобильное меню */}
        <div className="mobileMenu">
          <nav className="mobileMenu__nav" aria-label="Мобильная навигация">
            <Link to="/about" className="mobileMenu__link">О нас</Link>
            <Link to="/services" className="mobileMenu__link">Услуги</Link>
            <Link to="/portfolio" className="mobileMenu__link">Портфолио</Link>
            <Link to="/contact" className="mobileMenu__link">Контакты</Link>
          </nav>
          <div className="mobileMenu__cta">
            <Link to="/contact" className="btn btn--primary">Заказать услугу</Link>
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;
