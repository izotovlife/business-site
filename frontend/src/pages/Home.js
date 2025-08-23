// frontend/src/pages/Home.js
// Главная страница с героем и логотипом
import React from "react";
import "./Home.css";

export default function Home(){
  return (
    <section className="home-hero">
      <div className="container center">
        <div className="home-content">
          <img src="/logo.svg" alt="IZOTOVLIFE" className="home-logo" />
          <h1 className="home-title">IZOTOVLIFE</h1>
          <p className="home-tagline">Digital solutions crafted with passion</p>
        </div>
      </div>
    </section>
  );
}

