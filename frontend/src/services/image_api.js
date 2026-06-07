import api from './api';

export const imageAPI = {
  generate: (data) => api.post('/api/v1/generate/image', data),
};
