import api from './api';

export const socialAPI = {
  generate: (data) => api.post('/api/v1/generate/social', data),
};
