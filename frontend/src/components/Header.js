// C:\Users\ASUS Vivobook\PycharmProjects\izotoff.ru\business_site\frontend\src\components\Header.js
import React, { useState } from "react";
import { NavLink } from "react-router-dom";
import "./Header.css";

export default function Header(){
  const [open, setOpen] = useState(false);

  return (
    <header className="site-header">
      <div className="container header-row">
        <NavLink to="/" className="brand" onClick={()=>setOpen(false)}>
          Изотов
        </NavLink>

        <button className="burger" aria-label="Меню" onClick={()=>setOpen(v=>!v)}>
          <span/><span/><span/>
        </button>

        <nav className={`nav ${open ? "open" : ""}`}>
          <NavLink to="/services" className="nav-link" onClick={()=>setOpen(false)}>Услуги</NavLink>
          <NavLink to="/portfolio" className="nav-link" onClick={()=>setOpen(false)}>Портфолио</NavLink>
          <NavLink to="/testimonials" className="nav-link" onClick={()=>setOpen(false)}>Отзывы</NavLink>
        </nav>
      </div>
    </header>
  );
}

