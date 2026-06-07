export const CONTENT_TYPES = {
  BLOG: 'blog',
  SOCIAL: 'social',
  EMAIL: 'email',
  IMAGE: 'image',
  VOICE: 'voice',
  VIDEO: 'video',
  BUNDLE: 'bundle',
};

export const SOCIAL_PLATFORMS = ['instagram', 'twitter', 'linkedin', 'facebook', 'tiktok', 'youtube'];
export const TONES = ['professional', 'casual', 'persuasive', 'humorous', 'authoritative', 'empathetic', 'inspirational'];
export const LENGTHS = ['short', 'medium', 'long'];

export const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';
