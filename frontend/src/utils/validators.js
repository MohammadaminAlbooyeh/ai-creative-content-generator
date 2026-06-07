export function validatePrompt(prompt) {
  if (!prompt || prompt.trim().length === 0) {
    return 'Prompt is required';
  }
  if (prompt.trim().length < 3) {
    return 'Prompt must be at least 3 characters';
  }
  if (prompt.length > 5000) {
    return 'Prompt must be less than 5000 characters';
  }
  return null;
}

export function validateEmail(email) {
  if (!email || email.trim().length === 0) {
    return 'Email is required';
  }
  const pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  if (!pattern.test(email.trim())) {
    return 'Invalid email format';
  }
  return null;
}

export function validatePassword(password) {
  if (!password) {
    return 'Password is required';
  }
  if (password.length < 8) {
    return 'Password must be at least 8 characters';
  }
  return null;
}

export function validateUsername(username) {
  if (!username || username.trim().length === 0) {
    return 'Username is required';
  }
  if (username.trim().length < 3) {
    return 'Username must be at least 3 characters';
  }
  if (username.length > 50) {
    return 'Username must be less than 50 characters';
  }
  if (!/^[a-zA-Z0-9_]+$/.test(username)) {
    return 'Username can only contain letters, numbers, and underscores';
  }
  return null;
}

export function sanitizeInput(text) {
  if (!text) return '';
  return text
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#x27;');
}
