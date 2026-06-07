import React from 'react';
import { render, screen } from '@testing-library/react';
import ErrorDisplay from '../components/ErrorDisplay';

test('shows error message', () => {
  render(<ErrorDisplay message="Something went wrong" />);
  expect(screen.getByText(/Something went wrong/)).toBeInTheDocument();
});

test('shows default error message', () => {
  render(<ErrorDisplay />);
  expect(screen.getByText(/An error occurred/)).toBeInTheDocument();
});
