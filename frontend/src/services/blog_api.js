import api from './api';

export const blogAPI = {
  generate: (data) => api.post('/api/v1/generate/blog', data),
};
