import React from 'react';
import './Portfolio.css';

const portfolioItems = [
  { id: 1, title: 'Проект 1', image: 'https://via.placeholder.com/300', description: 'Описание проекта 1' },
  { id: 2, title: 'Проект 2', image: 'https://via.placeholder.com/300', description: 'Описание проекта 2' },
  { id: 3, title: 'Проект 3', image: 'https://via.placeholder.com/300', description: 'Описание проекта 3' },
];

export default function Portfolio() {
  return (
    <div className="portfolio-section container">
      <h2>Портфолио</h2>
      <div className="portfolio-grid">
        {portfolioItems.map(item => (
          <div className="portfolio-card" key={item.id}>
            <img src={item.image} alt={item.title} />
            <h3>{item.title}</h3>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
