import { useState } from 'react';
import api from '../services/api';

export function useContentGeneration() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  const generate = async (endpoint, payload) => {
    setLoading(true);
    setError(null);
    try {
      const data = await api.post(endpoint, payload);
      setResult(data);
      return data;
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return { generate, loading, error, result };
}
