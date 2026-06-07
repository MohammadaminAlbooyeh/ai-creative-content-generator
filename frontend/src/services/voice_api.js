import api from './api';

export const voiceAPI = {
  generate: (data) => api.post('/api/v1/generate/voice', data),
};
