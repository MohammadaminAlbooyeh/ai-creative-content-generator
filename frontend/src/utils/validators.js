export function validatePrompt(prompt) {
  if (!prompt || prompt.trim().length === 0) {
    return 'Prompt is required';
  }
  if (prompt.length < 3) {
    return 'Prompt must be at least 3 characters';
  }
  if (prompt.length > 5000) {
    return 'Prompt must be less than 5000 characters';
  }
  return null;
}
