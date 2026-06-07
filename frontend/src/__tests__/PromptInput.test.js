import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import PromptInput from '../components/PromptInput';

test('renders textarea with placeholder', () => {
  render(<PromptInput placeholder="Enter text..." />);
  expect(screen.getByPlaceholderText('Enter text...')).toBeInTheDocument();
});

test('calls onChange when user types', () => {
  const handleChange = jest.fn();
  render(<PromptInput onChange={handleChange} />);
  const textarea = screen.getByRole('textbox');
  fireEvent.change(textarea, { target: { value: 'hello' } });
  expect(handleChange).toHaveBeenCalledWith('hello');
});

test('displays value prop', () => {
  render(<PromptInput value="test value" onChange={() => {}} />);
  expect(screen.getByRole('textbox').value).toBe('test value');
});
