// Header.js
import React from 'react';
import { Link } from 'react-router-dom';

export default function Header() {
  return (
    <header style={styles.header}>
      <div style={styles.container}>
        <div style={styles.logo}>
          <Link to="/" style={styles.logoText}>Izotoff.ru</Link>
        </div>
        <nav style={styles.nav}>
          <Link to="/" style={styles.navLink}>Главная</Link>
          <Link to="/services" style={styles.navLink}>Услуги</Link>
          <Link to="/portfolio" style={styles.navLink}>Портфолио</Link>
          <Link to="/contacts" style={styles.navLink}>Контакты</Link>
        </nav>
      </div>
    </header>
  );
}

const styles = {
  header: {
    backgroundColor: '#2C3E50',
    padding: '15px 0',
    color: '#fff',
    position: 'sticky',
    top: 0,
    zIndex: 1000,
  },
  container: {
    width: '90%',
    maxWidth: '1200px',
    margin: '0 auto',
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  logo: {
    fontSize: '24px',
    fontWeight: 'bold',
  },
  logoText: {
    color: '#fff',
    textDecoration: 'none',
  },
  nav: {
    display: 'flex',
    gap: '20px',
  },
  navLink: {
    color: '#fff',
    textDecoration: 'none',
    fontWeight: '500',
    transition: '0.3s',
  },
};
