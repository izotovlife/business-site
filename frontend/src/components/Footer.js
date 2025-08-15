// Footer.js
import React from 'react';

export default function Footer() {
  return (
    <footer style={styles.footer}>
      <div style={styles.container}>
        <p>© 2025 Izotoff.ru. Все права защищены.</p>
        <p>Телефон: +7 (999) 123-45-67 | Email: info@izotoff.ru</p>
      </div>
    </footer>
  );
}

const styles = {
  footer: {
    backgroundColor: '#2C3E50',
    color: '#fff',
    padding: '20px 0',
    marginTop: '50px',
    textAlign: 'center',
  },
  container: {
    width: '90%',
    maxWidth: '1200px',
    margin: '0 auto',
  },
};
