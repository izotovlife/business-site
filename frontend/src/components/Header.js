import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import { useOrderModal } from "../OrderModalContext";
import "./Header.css";

export default function Header() {
  const [open, setOpen] = useState(false);
  const { openModal } = useOrderModal();

  const closeMenu = () => setOpen(false);

  return (
    <header className="site-header">
      <div className="container header-row">
        <NavLink to="/" className="brand" onClick={closeMenu}>
          <img src="/logo.svg" alt="IZOTOVLIFE" className="brand-img" />
          <span className="brand-title">IZOTOVLIFE</span>
        </NavLink>

        <nav className={`nav ${open ? "open" : ""}`}>
          <NavLink
            to="/services"
            className={({ isActive }) =>
              `nav-link${isActive ? " active" : ""}`
            }
            onClick={closeMenu}
          >
            Услуги
          </NavLink>
          <NavLink
            to="/portfolio"
            className={({ isActive }) =>
              `nav-link${isActive ? " active" : ""}`
            }
            onClick={closeMenu}
          >
            Портфолио
          </NavLink>
          <NavLink
            to="/contacts"
            className={({ isActive }) =>
              `nav-link${isActive ? " active" : ""}`
            }
            onClick={closeMenu}
          >
            Контакты
          </NavLink>
        </nav>

        <button className="btn" onClick={() => openModal("header") }>
          Заказать услугу
        </button>

        <button className="burger" onClick={() => setOpen(!open)}>
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </header>
  );
}
