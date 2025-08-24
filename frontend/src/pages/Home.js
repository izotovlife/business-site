// frontend/src/pages/Home.js
// Главная страница с героем и логотипом
import React from "react";
import { useOrderModal } from "../OrderModalContext";
import "./Home.css";

export default function Home() {
  const { openModal } = useOrderModal();
  return (
    <section className="home-hero">
      <div className="container center">
        <div className="home-content">
          <h1 className="home-title">Александр Изотов</h1>
          <p className="home-tagline">
            Администрирование сайтов, контент и SMM
          </p>
          <div className="home-actions">
            <button className="btn" onClick={() => openModal("home") }>
              Оставить заявку
            </button>
          </div>
        </div>
      </div>
    </section>
  );
}

