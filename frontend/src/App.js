import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import Services from './pages/Services';
import Portfolio from './pages/Portfolio';
import Testimonials from './pages/Testimonials';
import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="header">
          <div className="container header-container">
            <h1>Ваше Имя / Бренд</h1>
            <nav>
              <a href="#services">Услуги</a>
              <a href="#portfolio">Портфолио</a>
              <a href="#testimonials">Отзывы</a>
              <a href="#contacts">Контакты</a>
            </nav>
          </div>
        </header>

        <main>
          <section id="services">
            <Services />
          </section>

          <section id="portfolio">
            <Portfolio />
          </section>

          <section id="testimonials">
            <Testimonials />
          </section>
        </main>

        <footer className="footer">
          <div className="container footer-container">
            <p>© 2025 Ваше Имя. Все права защищены.</p>
            <p>Email: info@example.com | Телефон: +7 (999) 123-45-67</p>
          </div>
        </footer>
      </div>
    </Router>
  );
}

export default App;
