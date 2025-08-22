// frontend/src/components/Header.js

// Шапка сайта с логотипом из public/logo.svg
import React, { useState } from "react";
import { NavLink, Link } from "react-router-dom";
import "./Header.css";

export default function Header() {
  const [open, setOpen] = useState(false);

  return (
    <header className="site-header">
      <div className="container header-row">
        <Link to="/" className="brand" onClick={() => setOpen(false)}>
          <img
            className="brand-img"
            src="/logo.svg"
            alt="IZOTOVLIFE"
            height="36"
            width="auto"
            decoding="async"
          />
          <span className="brand-title">IZOTOVLIFE</span>
        </Link>

        <button
          className="burger"
          aria-label="Меню"
          onClick={() => setOpen(v => !v)}
        >
          <span /><span /><span />
        </button>

        <nav className={`nav ${open ? "open" : ""}`}>
          <NavLink to="/services" className="nav-link" onClick={() => setOpen(false)}>Услуги</NavLink>
          <NavLink to="/portfolio" className="nav-link" onClick={() => setOpen(false)}>Портфолио</NavLink>
          <NavLink to="/testimonials" className="nav-link" onClick={() => setOpen(false)}>Отзывы</NavLink>
        </nav>
      </div>
    </header>
  );
}
