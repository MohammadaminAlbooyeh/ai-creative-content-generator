import api from './api';

export const contentAPI = {
  getAll: () => api.get('/api/v1/content'),
  getById: (id) => api.get(`/api/v1/content/${id}`),
  generate: (data) => api.post('/api/v1/content/generate', data),
  update: (id, data) => api.put(`/api/v1/content/${id}`, data),
  delete: (id) => api.delete(`/api/v1/content/${id}`),
};
