// Путь: frontend/src/components/Header.js
// Назначение: Шапка с логотипом, навигацией и ОДНОЙ кнопкой, открывающей глобальную модалку

import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { useOrderModal } from "../OrderModalContext";
import "./Header.css";

export default function Header() {
  const [open, setOpen] = useState(false);
  const { open: openOrder } = useOrderModal();        // глобальная модалка
  const closeMenu = () => setOpen(false);

  return (
    <header className="site-header">
      <div className="container header-row">
        {/* Логотип */}
        <NavLink to="/" className="brand" onClick={closeMenu} aria-label="На главную">
          {/* В репозитории есть logo.svg — используем его, чтобы не ловить 404 */}
          <img src="/logo.svg" alt="IZOTOVLIFE" className="brand-img" />
          <span className="brand-title">IZOTOVLIFE</span>
        </NavLink>

        {/* Навигация */}
        <nav className={`nav ${open ? "open" : ""}`} aria-label="Основная навигация">
          <NavLink to="/services" className={({isActive}) => `nav-link${isActive ? " active" : ""}`} onClick={closeMenu}>
            Услуги
          </NavLink>
          <NavLink to="/portfolio" className={({isActive}) => `nav-link${isActive ? " active" : ""}`} onClick={closeMenu}>
            Портфолио
          </NavLink>
          <NavLink to="/contacts" className={({isActive}) => `nav-link${isActive ? " active" : ""}`} onClick={closeMenu}>
            Контакты
          </NavLink>
        </nav>

        {/* ОДНА CTA-кнопка — открывает глобальную форму */}
        <button className="btn" onClick={openOrder}>Заказать услугу</button>

        {/* Бургер для мобилок */}
        <button className="burger" aria-label="Меню" onClick={() => setOpen(!open)}>
          <span></span><span></span><span></span>
        </button>
      </div>
    </header>
  );
}
