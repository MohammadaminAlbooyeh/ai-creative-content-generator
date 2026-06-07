import React from 'react';
import { render, screen } from '@testing-library/react';
import SuccessMessage from '../components/SuccessMessage';

test('shows success message', () => {
  render(<SuccessMessage message="Done!" />);
  expect(screen.getByText('Done!')).toBeInTheDocument();
});

test('shows default success message', () => {
  render(<SuccessMessage />);
  expect(screen.getByText('Content generated successfully!')).toBeInTheDocument();
});
