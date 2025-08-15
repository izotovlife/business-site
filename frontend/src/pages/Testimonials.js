import React from 'react';
import './Testimonials.css';

const testimonials = [
  { id: 1, name: 'Иван Иванов', text: 'Отличные услуги! Рекомендую.', avatar: 'https://via.placeholder.com/80' },
  { id: 2, name: 'Мария Петрова', text: 'Очень профессионально и быстро.', avatar: 'https://via.placeholder.com/80' },
  { id: 3, name: 'Алексей Сидоров', text: 'Спасибо, результат превзошел ожидания.', avatar: 'https://via.placeholder.com/80' },
];

export default function Testimonials() {
  return (
    <div className="testimonials-section container">
      <h2>Отзывы клиентов</h2>
      <div className="testimonials-grid">
        {testimonials.map(t => (
          <div className="testimonial-card" key={t.id}>
            <img src={t.avatar} alt={t.name} />
            <p className="testimonial-text">"{t.text}"</p>
            <p className="testimonial-name">- {t.name}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
