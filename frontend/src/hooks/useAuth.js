import { useState, useEffect, useCallback } from 'react';
import authService from '../services/auth';

export function useAuth() {
  const [user, setUser] = useState(authService.getUser());
  const [token, setToken] = useState(authService.getToken());
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const isAuthenticated = !!token;

  const login = useCallback(async (username, password) => {
    setLoading(true);
    setError(null);
    try {
      const data = await authService.login(username, password);
      setUser(data.user);
      setToken(data.access_token);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const register = useCallback(async (username, email, password) => {
    setLoading(true);
    setError(null);
    try {
      const data = await authService.register(username, email, password);
      setUser(data.user);
      setToken(data.access_token);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const logout = useCallback(() => {
    authService.logout();
    setUser(null);
    setToken(null);
    setError(null);
  }, []);

  return { user, token, loading, error, isAuthenticated, login, register, logout };
}
