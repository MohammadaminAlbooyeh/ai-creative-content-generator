import authService from './auth';

const BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

class ApiService {
  getAuthHeaders() {
    const token = authService.getToken();
    const headers = { 'Content-Type': 'application/json' };
    if (token) {
      headers['Authorization'] = `Bearer ${token}`;
    }
    return headers;
  }

  async request(method, endpoint, data = null) {
    const config = {
      method,
      headers: this.getAuthHeaders(),
    };
    if (data) config.body = JSON.stringify(data);

    const response = await fetch(`${BASE_URL}${endpoint}`, config);
    if (!response.ok) {
      if (response.status === 401) {
        authService.logout();
        window.location.href = '/login';
        throw new Error('Session expired. Please log in again.');
      }
      const err = await response.json().catch(() => ({}));
      throw new Error(err.detail || `API error: ${response.statusText}`);
    }
    return response.json();
  }

  async get(endpoint) {
    return this.request('GET', endpoint);
  }

  async post(endpoint, data) {
    return this.request('POST', endpoint, data);
  }

  async put(endpoint, data) {
    return this.request('PUT', endpoint, data);
  }

  async delete(endpoint) {
    return this.request('DELETE', endpoint);
  }
}

export default new ApiService();
