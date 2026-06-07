import { useState, useEffect, useCallback } from 'react';
import api from '../services/api';

export function useContentHistory() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchHistory = useCallback(async (params = {}) => {
    setLoading(true);
    setError(null);
    try {
      const query = new URLSearchParams(params).toString();
      const data = await api.get(`/api/v1/content?${query}`);
      setItems(data.items || data);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  }, []);

  const deleteItem = useCallback(async (id) => {
    setError(null);
    try {
      await api.delete(`/api/v1/content/${id}`);
      setItems((prev) => prev.filter((item) => item.id !== id));
    } catch (err) {
      setError(err.message);
      throw err;
    }
  }, []);

  return { items, loading, error, fetchHistory, deleteItem };
}
