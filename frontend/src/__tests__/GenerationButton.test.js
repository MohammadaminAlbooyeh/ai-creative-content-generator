import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import GenerationButton from '../components/GenerationButton';

test('renders generate button', () => {
  render(<GenerationButton />);
  expect(screen.getByText('Generate')).toBeInTheDocument();
});

test('shows loading text when loading', () => {
  render(<GenerationButton loading={true} />);
  expect(screen.getByText('Generating...')).toBeInTheDocument();
  expect(screen.getByRole('button')).toBeDisabled();
});

test('calls onClick when clicked', () => {
  const handleClick = jest.fn();
  render(<GenerationButton onClick={handleClick} />);
  fireEvent.click(screen.getByRole('button'));
  expect(handleClick).toHaveBeenCalled();
});
