import React from 'react';
import { render, screen } from '@testing-library/react';
import ContentDisplay from '../components/ContentDisplay';

test('shows placeholder when no content', () => {
  render(<ContentDisplay />);
  expect(screen.getByText('Generated content will appear here')).toBeInTheDocument();
});

test('renders content when provided', () => {
  render(<ContentDisplay content="Hello World" />);
  expect(screen.getByText('Hello World')).toBeInTheDocument();
});
