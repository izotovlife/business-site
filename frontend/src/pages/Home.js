// frontend/src/pages/Home.js
// Главная страница с героем и логотипом
import React, { useState } from "react";
import OrderModal from "../components/OrderModal";
import "./Home.css";

export default function Home() {
  const [open, setOpen] = useState(false);

  return (
    <section className="home-hero">
      <div className="container center">
        <div className="home-content">
          <h1 className="home-title">Александр Изотов</h1>
          <p className="home-tagline">
            Администрирование сайтов, контент и SMM
          </p>
          <div className="home-actions">
            <button className="btn" onClick={() => setOpen(true)}>
              Оставить заявку
            </button>
          </div>
        </div>
      </div>
      <OrderModal open={open} onClose={() => setOpen(false)} preset="home" />
    </section>
  );
}

