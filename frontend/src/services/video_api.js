import api from './api';

export const videoAPI = {
  generate: (data) => api.post('/api/v1/generate/video', data),
};
