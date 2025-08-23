import React, { useState } from "react";
import { Link } from "react-router-dom";
import OrderModal from "./OrderModal";
import "./Header.css";

export default function Header() {
  const [modal, setModal] = useState(false);

  return (
    <header className="site-header">
      <div className="container header-row">
        <Link to="/" className="brand">
          <img src="/logo.png" alt="IZOTOVLIFE" className="site-logo" />
        </Link>
        <div className="header-actions">
          <button className="btn" onClick={() => setModal(true)}>
            Заказать услугу
          </button>
          <button className="btn" onClick={() => setModal(true)}>
            Заказать услугу
          </button>
        </div>
      </div>
      <OrderModal open={modal} onClose={() => setModal(false)} preset="header" />
    </header>
  );
}
