import { render, screen } from '@testing-library/react';
import App from './App';

test('renders services heading', () => {
  render(<App />);
  expect(screen.getByText(/Наши услуги/i)).toBeInTheDocument();
});
